from sympy import symbols, simplify

# Define symbolic variable s
s = symbols('s')

# Constants
omega0_val = 0.3489
B_val =0.0883




# Given roots
s1 = -0.3028 - 1.1781j
s2 = -0.7311 - 0.4880j
s3 = -0.7311 + 0.4880j
s4 = -0.3028 + 1.1781j
# Define the given polynomial expression
polynomial_expr = 1.1362/ ((s - s1) * (s - s2) * (s - s3) * (s - s4))

# Simplify the expression
simplified_expr = simplify(polynomial_expr)

# Print the simplified expression
print("Simplified Polynomial in terms of s:")
print(simplified_expr)
