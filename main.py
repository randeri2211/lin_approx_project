import sympy as sp

# Define the symbol
x = sp.symbols('x')

# Define the expression
expr = sp.sin(x**2)
derivative = sp.diff(expr, x)

# Convert the expression into a function
f = sp.lambdify(x, expr)
f_d = sp.lambdify(x, derivative)

def upwind_difference(func, val, h):
    return (func(val + h) - func(val)) / h

def backwind_difference(func, val, h):
    return (func(val) - func(val - h)) / h

def central_difference(func, val, h):
    return (func(val + h) - func(val - h)) / (2 * h)

val = 2
step_size = 0.05
actual_d = f_d(val)
up = upwind_difference(f, val, step_size)
down = backwind_difference(f, val, step_size)
center = central_difference(f, val, step_size)

decimals = 4
format_str = f'.{decimals}f'

print(f'Function: {expr}')
print(f'Val: {val:{format_str}}')
print(f'Step Size: {step_size:{format_str}}')
print(f'Actual derivative: {actual_d:{format_str}}\n')
print(f'Upwind difference: {up:{format_str}}\nError: {actual_d - up:{format_str}}\n')
print(f'Backwind difference: {down:{format_str}}\nError: {actual_d - down:{format_str}}\n')
print(f'Central difference: {center:{format_str}}\nError: {actual_d - center:{format_str}}\n')

