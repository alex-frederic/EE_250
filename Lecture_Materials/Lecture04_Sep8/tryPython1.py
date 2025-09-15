# Example Python Script for Teaching Key Concepts

# 1. Shallow Copy vs. Deep Copy
print("=== Shallow Copy vs. Deep Copy ===")
import copy

# Original list with nested lists
original_list = [[1, 2], [3, 4]]
print("Original List:", original_list)

# Shallow copy
#shallow_copy = copy.copy(original_list)
shallow_copy = original_list
print("Shallow Copy:", shallow_copy)

# Deep copy
deep_copy = copy.deepcopy(original_list)
print("Deep Copy:", deep_copy)

# Modify the original list
original_list[0][0] = 99
print("After Modifying Original List:")
print("Original List:", original_list)
print("Shallow Copy:", shallow_copy)  # Changes reflect here
print("Deep Copy:", deep_copy)        # No changes here

print("\n")

print("Press Enter to continue...")
input()  # Waits for user input

# 2. Lists vs. Tuples
print("=== Lists vs. Tuples ===")
# A list
my_list = [1, 2, 3]
print("List:", my_list)
my_list[0] = 99  # Mutable
print("Modified List:", my_list)

# A tuple
my_tuple = (1, 2, 3)
print("Tuple:", my_tuple)
try:
    my_tuple[0] = 99  # Uncommenting this line will raise a TypeError (tuples are immutable)
except TypeError as e:
    print("Error:", e)
#my_tuple[0] = 99  # Uncommenting this line will raise a TypeError (tuples are immutable)  

print("\n")

print("functionality with list:")
print(dir(my_list))
print("functionality with tuple:")
print(dir(my_tuple))

print("\n using in-built functions for list: reverse, insert, count")
my_list.reverse()
print(my_list)
my_list.insert(2,3)
print(my_list)
print(my_list.count(3))

print("\n using in-built functions for tuple: count")
print(my_tuple.count(3))

print("\n")

print("Press Enter to continue...")
input()  # Waits for user input

# 3. Dictionary
print("=== Dictionary ===")
# Creating a dictionary
student = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Science"]
}
print("Dictionary:", student)

# Accessing dictionary elements
print("Name:", student["name"])
print("Courses:", student["courses"])

# Adding a new key-value pair
student["graduation_year"] = 2025
print("Updated Dictionary:", student)

# Removing a key-value pair
del student["age"]
print("Dictionary after deletion:", student)

print("\n")

print("Press Enter to continue...")
input()  # Waits for user input

# 4. Iterators
print("=== Iterators ===")
# Create an iterable
numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)  # Create an iterator from the list
print("Iterator Example:")
print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
# Use a loop to go through remaining elements
for number in iterator:
    print(number)

print("\n")

print("=== Dictionary Iteration ===")
print("Dictionary Iteration Example:")
for (k,v) in student.items():
    print(f"{k}: {v}")
print("\n")

print("Press Enter to continue...")
input()  # Waits for user input


# 5. String Built-in Functions
print("=== String Built-in Functions ===")
text = " Hello, World! "
print("Original Text:", f"'{text}'")

# Strip whitespace
stripped = text.strip()
print("Stripped Text:", f"'{stripped}'")

# Convert to uppercase
upper_case = text.upper()
print("Uppercase Text:", upper_case)

# Replace a substring
replaced = text.replace("World", "Python")
print("Replaced Text:", replaced)

# Split into a list of words
words = text.split()
print("Split Text:", words)

# Join words with a hyphen
joined = "-".join(words)
print("Joined Text:", joined)

# Check if the text starts with a specific substring
print("Starts with 'Hello':", text.startswith(" Hello"))

# Check if the text ends with a specific substring
print("Ends with '!':", text.endswith("!"))

print("\n")

