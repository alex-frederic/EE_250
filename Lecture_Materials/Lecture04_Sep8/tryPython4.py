# Step 1: Importing Matplotlib and NumPy
import matplotlib.pyplot as plt
import numpy as np

print("Welcome to the Matplotlib tutorial!")

# Step 2: Scatter Plot
print("\n--- Scatter Plot ---")
# Generate data
x = np.random.rand(20) * 10  # 20 random x-values between 0 and 10
y = np.random.rand(20) * 10  # 20 random y-values between 0 and 10
sizes = np.random.rand(20) * 100  # Random sizes for scatter points
colors = np.random.rand(20)  # Random colors for scatter points

# Create scatter plot
plt.figure(figsize=(6, 4))  # Set figure size
plt.scatter(x, y, s=sizes, c=colors, cmap="viridis", alpha=0.7, edgecolors="black")
plt.colorbar(label="Color Intensity")  # Add a color bar
plt.title("Scatter Plot Example")
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.show()  # Display the plot

#plot y = x^2
# Generate data
x = range(-10, 11)  # x values from -10 to 10
y = [i**2 for i in x]  # y = x^2

# Plot the curve
plt.plot(x, y, label="y = x^2", color="blue")

# Add labels and title
plt.title("Plot of y = x^2")
plt.xlabel("x")
plt.ylabel("y")

# Show legend
plt.legend()

# Display the plot
plt.show()



# Step 3: Bar Graph
print("\n--- Bar Graph ---")
# Generate data
categories = ['A', 'B', 'C', 'D', 'E']  # Categories
values = [10, 20, 15, 25, 30]  # Corresponding values

# Create bar graph
plt.figure(figsize=(6, 4))
plt.bar(categories, values, color="skyblue", edgecolor="black")
plt.title("Bar Graph Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# Step 4: Histogram
print("\n--- Histogram ---")
# Generate data
data = np.random.randn(1000)  # 1000 random numbers from a normal distribution

# Create histogram
plt.figure(figsize=(6, 4))
plt.hist(data, bins=20, color="purple", edgecolor="black", alpha=0.7)
plt.title("Histogram Example")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.show()

# Step 5: Pie Plot
print("\n--- Pie Plot ---")
# Generate data
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [40, 30, 20, 10]  # Proportions for each category
explode = (0.1, 0, 0, 0)  # "Explode" the first slice slightly

# Create pie plot
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=explode, startangle=90, colors=["gold", "lightblue", "pink", "lightgreen"])
plt.title("Pie Plot Example")
plt.show()

print("\nThank you for following this Matplotlib tutorial!")
