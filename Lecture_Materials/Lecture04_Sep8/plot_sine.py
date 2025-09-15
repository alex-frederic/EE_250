import matplotlib.pyplot as plt
import numpy as np
import math

start = 0
stop = 2 * math.pi
step = 0.5

x_values = np.arange(0, 2*math.pi, 0.01)
y_values = [ math.sin(i) for i in x_values ]

plt.figure(figsize=(6,4))
plt.plot(x_values, y_values, label="y = sin(x)", color="red")

plt.title("Graph of y = sin(x)")
plt.xlabel("x")
plt.ylabel("y")

plt.legend()
plt.show()