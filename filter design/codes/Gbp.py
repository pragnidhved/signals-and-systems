import numpy as np

# Given parameters
s1 = -0.1982 - 1.0404j
s2 = -0.4785 - 0.4310j
s3 = -0.4785 + 0.4310j
s4 = -0.1982 + 1.0404j
epsilon = 0.279
Omega_Lp = 1

# Define denominator polynomial
den = np.poly([s1, s2, s3, s4])

# Define frequency range
w = np.arange(-2, 2.01, 0.01)

num = 0.4480

# Define parameters for transformation
B = 0.0883
Omega0 = 0.3489
# Perform transformation to get s_L
s_L = (1j * 0.5913)**2 + Omega0**2
s_L /= B * (1j * 0.5913)

H = num / np.polyval(den, s_L)
print(1 / abs(H))
