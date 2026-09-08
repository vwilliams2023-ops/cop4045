array = [1,2,3,4,5,6];

count = 0

for num in array:
    count += 1
print(f"count: {count}");

# Method 1: Using a for loop
numbers = [10, 25, 33, 47, 52, 68]
count = 0
for num in numbers:
    count += 1
print(f"Total count: {count}")  # Output: 6

# Method 2: Using len() - SIMPLEST
print(len(numbers))  # Output: 6

# Method 3: Count with condition (e.g., count numbers > 30)
count_greater_than_30 = sum(1 for num in numbers if num > 30)
print(count_greater_than_30)  # Output: 3