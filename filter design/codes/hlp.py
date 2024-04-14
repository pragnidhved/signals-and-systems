from sympy import symbols, simplify

# Define symbolic variable s
s = symbols('s')

# Constants
omega0_val = 0.3489
B_val =0.0883




# Given roots
s1 = -0.1982 - 1.0404j
s2 = -0.4785 - 0.4310j
s3 = -0.4785 + 0.4310j
s4 = -0.1982 + 1.0404j
# Define the given polynomial expression
polynomial_expr = 0.4480/ ((s - s1) * (s - s2) * (s - s3) * (s - s4))

# Simplify the expression
simplified_expr = simplify(polynomial_expr)

# Print the simplified expression
print("Simplified Polynomial in terms of s:")
print(simplified_expr)
