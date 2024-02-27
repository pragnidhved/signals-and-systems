import numpy as np
import matplotlib.pyplot as plt

# Define the range of t values for continuous plot
t_values = np.linspace(0, 5, 100)  # Adjust the range as per your requirement

# Calculate the corresponding values of e^-2t
y_values_continuous = np.exp(-2 * t_values)

# Plotting the continuous graph
plt.plot(t_values, y_values_continuous, label=r'$e^{-2t}$ (continuous)')

# Define parameters for the discrete plot
n_values = np.arange(0, 10)  # Define the range of n values
y_values_discrete = [1]  # Initial condition y(0) = 1

# Calculate the discrete values of y(n) iteratively
for n in range(1, len(n_values)):
    y_values_discrete.append(y_values_discrete[-1] / 2)

# Plotting the discrete graph
plt.stem(n_values, y_values_discrete, linefmt='C1-', markerfmt='C1o', basefmt='C1_', label=r'$y(n+1) = \frac{y(n)}{d}$ (discrete)')

# Adding labels and title
plt.xlabel('t / n')
plt.ylabel('y')
plt.title('Continuous and Discrete Graphs')

# Adding grid
plt.grid(True)

# Adding legend
plt.legend()

# Save the plot as an image file
plt.savefig('graph.png')

# Show plot
plt.show()

