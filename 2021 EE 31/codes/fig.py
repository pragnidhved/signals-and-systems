import matplotlib.pyplot as plt
import numpy as np

# Read data from the .dat file with space as the delimiter, skip lines starting with 'Values'
data = np.loadtxt('values.dat', delimiter=' ', comments='Values')

# Extracting values for x_1(n) and x_2(n)
n_values_1 = data[:7, 0]
x_1_values = data[:7, 1]

n_values_2 = data[7:, 0]
x_2_values = data[7:, 1]


# Create the first stem plot for x_1(n)
plt.subplot(2, 1, 1)
plt.stem(n_values_1, x_1_values, linefmt='b-', markerfmt='bo', basefmt='r-')


# Add labels and title for the first plot
plt.xlabel('$n$')
plt.ylabel('$x(n)$')
plt.grid(True)

# Create the second stem plot for x_2(n)
plt.subplot(2, 1, 2)
plt.stem(n_values_2, x_2_values, linefmt='b-', markerfmt='bo', basefmt=' ')


# Add labels and title for the second plot
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()
plt.savefig('plot.png')
# Show the combined plot
plt.show()
