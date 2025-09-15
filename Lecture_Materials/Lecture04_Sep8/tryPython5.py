# Python Tutorial: Advanced Concepts

# --- Zip Function ---
print("--- Zip Function: Basic Example ---")

# Two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Combine the two lists using zip()
zipped = zip(names, ages)

# Convert to a list and display
zipped_list = list(zipped)
print(f"Zipped list: {zipped_list}")

print("--- Zip Function: Iterating Example ---")

# Two lists
subjects = ["Math", "Science", "History"]
marks = [85, 90, 78]

# Iterate over the zipped object
for subject, mark in zip(subjects, marks):
    print(f"{subject}: {mark}")

# --- List Comprehension ---
print("--- List Comprehension: Basic Example ---")

# Create a list of squares of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]
print(f"Squares of numbers from 1 to 10: {squares}")

print("--- List Comprehension: With Condition ---")

# Create a list of even numbers from 1 to 20
evens = [x for x in range(1, 21) if x % 2 == 0]
print(f"Even numbers from 1 to 20: {evens}")

print("--- List Comprehension: Nested Example ---")

# Generate a multiplication table (1 to 3)
table = [[x * y for y in range(1, 4)] for x in range(1, 4)]
print("Multiplication table (1 to 3):")
print(table)

# --- Lambda Functions ---
print("--- Lambda Function: Basic Example ---")

# Lambda to calculate the square of a number
square = lambda x: x**2
print(f"The square of 5 is: {square(5)}")

print("--- Lambda Function: Sorting Example ---")

# List of tuples
data = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]

# Sort by the second element (age)
sorted_data = sorted(data, key=lambda x: x[1])
print(f"Data sorted by age: {sorted_data}")

# --- Map Function ---
print("--- Map Function: Basic Example ---")

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Use map to calculate squares
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Original numbers: {numbers}")
print(f"Squared numbers: {squared_numbers}")

print("--- Map Function: Using Built-in Function ---")

# List of strings
words = ["hello", "world", "python"]

# Use map to convert strings to uppercase
uppercase_words = list(map(str.upper, words))
print(f"Original words: {words}")
print(f"Uppercase words: {uppercase_words}")

# --- Filter Function ---
print("--- Filter Function: Basic Example ---")

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Use filter to select even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Original numbers: {numbers}")
print(f"Even numbers: {even_numbers}")

print("--- Filter Function: With Strings ---")

# List of words
words = ["apple", "banana", "cherry", "date"]

# Filter words that start with 'a'
a_words = list(filter(lambda word: word.startswith('a'), words))
print(f"Original words: {words}")
print(f"Words starting with 'a': {a_words}")

# --- Combined Example ---
print("--- Combined Example ---")

# Data: Names and ages
names = ["Alice", "Bob", "Charlie", "David"]
ages = [25, 30, 35, 40]

# Use zip() to combine names and ages
zipped_data = list(zip(names, ages))
print(f"Zipped data: {zipped_data}")

# Use filter() to find people aged 30 or older
adults = list(filter(lambda person: person[1] >= 30, zipped_data))
print(f"Adults (30 or older): {adults}")

# Use map() to extract names of adults
adult_names = list(map(lambda person: person[0], adults))
print(f"Names of adults: {adult_names}")

# Use list comprehension to create a message
messages = [f"{name} is {age} years old." for name, age in adults]
print("Messages:")
for message in messages:
    print(message)
