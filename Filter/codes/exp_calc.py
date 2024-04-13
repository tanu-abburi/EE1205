from sympy import symbols, simplify

# Define symbolic variable s
s_L = symbols('s_L')

# Given roots
s1 = -0.3913 - 0.4156j
s2 = -0.3913 + 0.4156j
s3 = -0.1621 + 1.0033j
s4 = -0.1621 - 1.0033j

# Define the given polynomial expression
polynomial_expr = 0.3125 / ((s_L - s1) * (s_L - s2) * (s_L - s3) * (s_L - s4))

# Simplify the expression
simplified_expr = simplify(polynomial_expr)

# Print the simplified expression
print("Simplified Polynomial in terms of s:")
print(simplified_expr)
