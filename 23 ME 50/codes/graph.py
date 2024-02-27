import numpy as np
import matplotlib.pyplot as plt

# Define the range of t values for continuous plot
t_values = np.linspace(0, 5, 100)  # Adjust the range as per your requirement

# Calculate the corresponding values of e^-2t
y_values_continuous = np.exp(-2 * t_values)

# Plotting the continuous graph
plt.plot(t_values, y_values_continuous, label=r'$e^{-2t}$ (continuous)')

data = np.loadtxt('values.dat', delimiter=' ', comments='Values')

# Extracting values for x_1(n) and x_2(n)
n_values_1 = data[:7, 0]
x_1_values = data[:7, 1]
# Plotting the discrete graph
plt.stem(n_values_1, x_1_values, linefmt='C1-', markerfmt='C1o', basefmt='C1_', label='discrete')

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

