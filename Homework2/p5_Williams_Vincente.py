import sys
import unittest
from datetime import datetime
from pathlib import Path
from tempfile import TemporaryDirectory


DATE_FORMAT = "%I:%M:%S %p %m/%d/%Y"
MIN_TEMPERATURE = -100.0
MAX_TEMPERATURE = 150.0


def read_observations(filename):
	"""Read observations and return (observations, errors)."""
	observations = {}
	errors = []
	seen = set()

	with open(filename, "r", encoding="utf-8") as input_file:
		for line_number, raw_line in enumerate(input_file, start=1):
			line = raw_line.strip()
			fields = line.split(",")

			if len(fields) != 3 or not all(field.strip() for field in fields):
				errors.append((line_number, "malformed line"))
				continue

			station, date_text, temperature_text = (field.strip() for field in fields)
			try:
				date = datetime.strptime(date_text, DATE_FORMAT)
			except ValueError:
				errors.append((line_number, "invalid date"))
				continue

			try:
				temperature = float(temperature_text)
			except ValueError:
				errors.append((line_number, "invalid temperature"))
				continue

			if not MIN_TEMPERATURE <= temperature <= MAX_TEMPERATURE:
				errors.append((line_number, "temperature out of range"))
				continue

			key = (station, date)
			if key in seen:
				errors.append((line_number, "duplicate observation"))
				continue

			seen.add(key)
			observations.setdefault(station, []).append((date, temperature))

	for station in observations:
		observations[station].sort(key=lambda observation: observation[0])

	return observations, errors


def station_statistics(observations):
	"""Return (minimum, maximum, mean) temperatures for each station."""
	return {
		station: (
			min(temperature for _, temperature in station_observations),
			max(temperature for _, temperature in station_observations),
			sum(temperature for _, temperature in station_observations)
			/ len(station_observations),
		)
		for station, station_observations in observations.items()
	}


def station_outliers(observations):
	"""Return stations whose latest temperature exceeds their mean."""
	statistics = station_statistics(observations)
	return {
		station: (date, temperature, statistics[station][2])
		for station, station_observations in observations.items()
		for date, temperature in [station_observations[-1]]
		if temperature > statistics[station][2]
	}


def write_statistics(filename, statistics):
	"""Write station statistics in station-name order."""
	with open(filename, "w", encoding="utf-8") as output_file:
		for station in sorted(statistics):
			minimum, maximum, mean = statistics[station]
			output_file.write(
				f"{station},{minimum:.1f},{maximum:.1f},{mean:.1f}\n"
			)


def main():
	"""Read input and output filenames from the command line."""
	if len(sys.argv) != 3:
		print("Usage: python p5_Williams_Vincente.py input_file output_file")
		return

	input_filename, output_filename = sys.argv[1:]
	try:
		observations, errors = read_observations(input_filename)
		statistics = station_statistics(observations)
		outliers = station_outliers(observations)
		write_statistics(output_filename, statistics)
	except OSError as error:
		print(f"File access error: {error}")
		return

	print("Statistics:")
	for station in sorted(statistics):
		minimum, maximum, mean = statistics[station]
		print(f"{station}: min={minimum:.1f}, max={maximum:.1f}, mean={mean:.1f}")

	print("Outliers:")
	for station in sorted(outliers):
		date, temperature, mean = outliers[station]
		print(f"{station}: {date.strftime(DATE_FORMAT)}, {temperature:.1f}, {mean:.1f}")

	for line_number, error_message in errors:
		print(f"Line {line_number}: {error_message}")


class TestTemperatureAnalysis(unittest.TestCase):
	def make_file(self, contents):
		directory = TemporaryDirectory()
		self.addCleanup(directory.cleanup)
		filename = Path(directory.name) / "observations.txt"
		filename.write_text(contents, encoding="utf-8")
		return filename

	def test_reads_several_stations_and_sorts_observations(self):
		filename = self.make_file(
			"Station B,09:28:09 AM 04/21/2026,12.0\n"
			"Station A,09:28:09 AM 04/20/2026,-4.0\n"
			"Station B,09:28:09 AM 04/20/2026,8.0\n"
		)
		observations, errors = read_observations(filename)
		self.assertEqual(errors, [])
		self.assertEqual(list(observations), ["Station B", "Station A"])
		self.assertLess(observations["Station B"][0][0], observations["Station B"][1][0])

	def test_accepts_negative_temperature(self):
		filename = self.make_file("A,09:28:09 AM 04/20/2026,-100.0\n")
		observations, errors = read_observations(filename)
		self.assertEqual(observations["A"][0][1], -100.0)
		self.assertEqual(errors, [])

	def test_rejects_duplicate_observation(self):
		contents = "A,09:28:09 AM 04/20/2026,10\nA,09:28:09 AM 04/20/2026,11\n"
		observations, errors = read_observations(self.make_file(contents))
		self.assertEqual(len(observations["A"]), 1)
		self.assertEqual(errors[0][1], "duplicate observation")

	def test_rejects_invalid_temperature_range(self):
		observations, errors = read_observations(
			self.make_file("A,09:28:09 AM 04/20/2026,150.1\n")
		)
		self.assertEqual(observations, {})
		self.assertEqual(errors[0][1], "temperature out of range")

	def test_calculates_statistics_and_outliers(self):
		filename = self.make_file(
			"A,09:28:09 AM 04/20/2026,10\nA,09:28:09 AM 04/21/2026,20\n"
		)
		observations, _ = read_observations(filename)
		self.assertEqual(station_statistics(observations)["A"], (10.0, 20.0, 15.0))
		self.assertEqual(station_outliers(observations)["A"][1:], (20.0, 15.0))

	def test_writes_sorted_formatted_output(self):
		filename = self.make_file("")
		write_statistics(filename, {"Z": (1, 2, 1.5), "A": (-2, 3, 0.5)})
		self.assertEqual(
			filename.read_text(encoding="utf-8"),
			"A,-2.0,3.0,0.5\nZ,1.0,2.0,1.5\n",
		)

	def test_missing_file_raises_file_not_found(self):
		with self.assertRaises(FileNotFoundError):
			read_observations("missing-observations.txt")


if __name__ == "__main__":
	main()

