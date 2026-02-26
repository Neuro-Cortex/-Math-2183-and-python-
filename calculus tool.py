# calculus_tool.py
# Simple Calculus Analyzer
# Author: Pollob Das

import sympy as sp

x = sp.symbols('x')

def analyze(expr):
    f = sp.sympify(expr)
    f1 = sp.diff(f, x)
    f2 = sp.diff(f1, x)

    critical = sp.solve(f1, x)
    inflection = sp.solve(f2, x)

    print("\nFunction:", f)
    print("First Derivative:", f1)
    print("Second Derivative:", f2)
    print("Critical Points:", critical)
    print("Inflection Points:", inflection)

if __name__ == "__main__":
    expr = input("Enter function in x: ")
    analyze(expr)

#x**3 - 6*x**2 + 9*x ans
