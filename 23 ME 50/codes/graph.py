import numpy as np
import matplotlib.pyplot as plt

# Define the range of t values for continuous plot
data = np.loadtxt('values.dat', delimiter=' ', comments='Values')

# Extracting values for x_1(n) and x_2(n)
n_values_2 = data[:7, 0]
x_2_values = data[:7, 1]
# Plotting the discrete graph
plt.stem(n_values_2, x_2_values, linefmt='C1-', markerfmt='C1o', basefmt='C1_', label='numerical')



# Extracting values for x_1(n) and x_2(n)
n_values_1 = data[:7, 0]
x_1_values = data[:7, 1]
# Plotting the discrete graph
plt.stem(n_values_1, x_1_values, linefmt='C1-', markerfmt='C2o', basefmt='C1_', label='theoritical')

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

