import sympy as sp

# Define symbolic variable
x = sp.symbols('x')

# define the function
f = (x)**2 + 6*(x) + 1

# derivative
f_derivative = sp.diff(f, x)

# define inital values
x_value = 0
alfa = 0.1


for i in range(1, 5):

    result = f_derivative.subs(x, x_value)

    # new x value
    x_value -= alfa * result
    print(f"Yeni x_{i} değeri: {x_value}\n")
