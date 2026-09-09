def pyth(n):

    threes = []

    for a in range(1, n + 1):
        for b in range(a, n + 1):
            for c in range(b, n + 1):
                if a**2 + b**2 == c**2:
                    threes.append((a, b, c))
    return threes


def pythcalc():
    # Read positive integer from terminal
    while True:
        try:
            n = int(input("Enter a positive number: "))
            if n > 0:
                break
            else:
                print("Please enter a positive integer greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    threes = pyth(n)
    
    # Display results
    if threes:
        print(f"\nPythagorean triples with 0 < a, b, c <= {n}:")
        for triple in threes:
            print(f"({threes[0]}, {threes[1]}, {threes[2]})")
        print(f"\nTotal number of triples found: {len(threes)}")
    else:
        print(f"\nNo Pythagorean triples found = {n}.")

if __name__ == "__main__":
    pythcalc()