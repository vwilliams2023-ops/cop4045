"""Unit tests for filesystem entries and recursive search behavior."""

import unittest

from p6_Williams_Vincente import Entry, File, Folder, find_large_files


class EntryMethodsTest(unittest.TestCase):
    """Test absolute paths and recursive large-file searches."""

    def setUp(self) -> None:
        """Create a small nested folder tree for each test."""
        self.root = Folder("root")
        self.nested = Folder("nested", self.root)
        self.small_file = File("small.txt", self.root, 4)
        self.large_file = File("large.txt", self.nested, 10)
        self.equal_file = File("equal.txt", self.root, 8)
        self.root.add(self.small_file)
        self.root.add(self.nested)
        self.root.add(self.equal_file)
        self.nested.add(self.large_file)

    def test_absolute_path_root(self) -> None:
        """A root entry's absolute path contains only itself."""
        self.assertEqual(self.root.absolute_path(), [self.root])

    def test_absolute_path_nested_folder(self) -> None:
        """A nested folder's path starts at itself and ends at the root."""
        self.assertEqual(self.nested.absolute_path(), [self.nested, self.root])

    def test_absolute_path_file(self) -> None:
        """A file path includes the file and all ancestor folders."""
        self.assertEqual(
            self.large_file.absolute_path(),
            [self.large_file, self.nested, self.root],
        )

    def test_find_large_files_on_file_at_threshold(self) -> None:
        """A file meeting the threshold is returned when searched directly."""
        self.assertEqual(find_large_files(self.equal_file, 8), [self.equal_file])

    def test_find_large_files_on_file_below_threshold(self) -> None:
        """A file below the threshold is excluded when searched directly."""
        self.assertEqual(find_large_files(self.small_file, 5), [])

    def test_find_large_files_recurses_through_nested_folders(self) -> None:
        """A folder search returns matching files in child traversal order."""
        self.assertEqual(
            find_large_files(self.root, 8),
            [self.large_file, self.equal_file],
        )

    def test_find_large_files_with_no_matches(self) -> None:
        """A folder search returns an empty list when nothing matches."""
        self.assertEqual(find_large_files(self.root, 11), [])

    def test_find_large_files_on_empty_folder(self) -> None:
        """Searching an empty folder returns an empty list."""
        empty_folder = Folder("empty")
        self.assertEqual(find_large_files(empty_folder, 0), [])

    def test_find_large_files_rejects_plain_entry(self) -> None:
        """Searching an entry without file or folder behavior raises."""
        with self.assertRaises(TypeError):
            find_large_files(Entry("plain"), 0)

    def test_three_level_folder_size_and_search_thresholds(self) -> None:
        """One outer-folder size call includes nested files and folders."""
        outer = Folder("outer")
        middle = Folder("middle", outer)
        inner = Folder("inner", middle)
        small_file = File("small.txt", outer, 5)
        middle_file = File("middle.txt", middle, 15)
        large_file = File("large.txt", inner, 25)
        outer.add(small_file)
        outer.add(middle)
        middle.add(middle_file)
        middle.add(inner)
        inner.add(large_file)

        self.assertEqual(outer.size(), 45)
        self.assertEqual(inner.absolute_path(), [inner, middle, outer])
        self.assertEqual(
            large_file.absolute_path(), [large_file, inner, middle, outer]
        )
        self.assertEqual(
            find_large_files(outer, 15), [middle_file, large_file]
        )
        self.assertEqual(find_large_files(outer, 20), [large_file])


if __name__ == "__main__":
    unittest.main()
