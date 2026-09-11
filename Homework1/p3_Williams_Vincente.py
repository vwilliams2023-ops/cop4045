def find_dup_str(s, n):
  
    if n <= 0 or n > len(s):
        return ""
    
    seen = set()
    
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring in seen:
            return substring
        seen.add(substring)
    
    return ""


def find_max_dup(s):
    
    if len(s) < 2:
        return ""
    
    max_dup = ""
    
    for n in range(len(s) - 1, 0, -1):
        result = find_dup_str(s, n)
        if result != "":
            return result
    
    return ""


# Testing code for part a)
print("Testing find_dup_str")
s = input("Enter a string: ")
n = int(input("Enter substring length: "))
result = find_dup_str(s, n)
print(f"Result: '{result}'")

# Testing code for part b)
print("\nTesting find_max_dup")
s = input("Enter a string: ")
result = find_max_dup(s)
print(f"Longest duplicated substring: '{result}'")