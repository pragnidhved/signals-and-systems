import numpy as np

# Given parameters
s1 = -0.3028 - 1.1781j
s2 = -0.7311 - 0.4880j
s3 = -0.7311 + 0.4880j
s4 = -0.3028 + 1.1781j
epsilon = 0.11
Omega_Lp = 1

# Generate the denominator polynomial
den = np.poly([s1, s2, s3, s4])
num = np.array([1])
s = 1j*1  # use Omega = 1
H = num / np.polyval(den, s)

req = 1 / np.sqrt(1 + epsilon**2)

Gain_LP = req / abs(H)
print(Gain_LP)
