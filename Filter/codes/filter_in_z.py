import sympy as sp

# Define symbols
s, z = sp.symbols('s z')

# Given transfer function
Ha_BP_s = 1.908e-5 * s**4 / (s**8 + 0.0978*s**7 + 0.508*s**6 + 0.037*s**5 + 0.0952*s**4 + 0.00458*s**3 + 0.0078*s**2 + 0.000186*s + 0.00024)

# Perform substitution
substitution = ((1 - z**-1) / (1 + z**-1))
substituted_expression = Ha_BP_s.subs(s, substitution)

# Simplify the expression
simplified_expression = sp.simplify(substituted_expression)

# Print the result
print("Expression in z:")
print(simplified_expression)


