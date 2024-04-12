import sympy as sp

# Define symbols
s, z = sp.symbols('s z')

# Given transfer function
Ha_BP_s =302.85 * s**4 / (16449.66*s**8 + 3003.4*s**7 + 8412.19*s**6 + 1126.65*s**5 + 1561.67*s**4 + 137.14*s**3 + 124.65*s**2 + 5.41*s + 3.61)
# Perform substitution
substitution = ((1 - z**-1) / (1 + z**-1))
substituted_expression = Ha_BP_s.subs(s, substitution)

# Simplify the expression
simplified_expression = sp.simplify(substituted_expression)

# Print the result
print("Expression in z:")
print(simplified_expression)


