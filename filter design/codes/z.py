import sympy as sp

# Define symbols
s, z = sp.symbols('s z')

# Given transfer function
Ha_BP_s =768.07 * s**4 / (16449.66*s**8 + 1965.82*s**7 + 8255.46*s**6 + 731.92*s**5 + 1522.84*s**4 + 89.09*s**3 + 122.33*s**2 + 3.54*s + 3.61)
# Perform substitution
substitution = ((1 - z**-1) / (1 + z**-1))
substituted_expression = Ha_BP_s.subs(s, substitution)

# Simplify the expression
simplified_expression = sp.simplify(substituted_expression)

# Print the result
print("Expression in z:")
print(simplified_expression)


