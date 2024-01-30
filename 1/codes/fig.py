import matplotlib.pyplot as plt
import numpy as np
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
y = np.array([6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66])
fig, ax = plt.subplots()
plt.stem(x, y)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('AP')
fig.set_size_inches(4, 3)
plt.savefig('plot.png')
plt.show()
