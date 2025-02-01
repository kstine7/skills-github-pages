import math

def approximation_algorithm(x0, tol=1e-6):
    """Approximation algorithm to find square root of 2."""
    iter_count = 0
    x = x0
    diff = x0

    print(f"{iter_count} : {x:.15f}")

    while diff >= tol:
        iter_count += 1
        y = x
        x = (x / 2) + (1 / x)
        diff = abs(x - y)

        print(f"{iter_count} : {x:.15f}")

    print(f"\nConvergence after {iter_count} iterations")
    return x

def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    """Bisection method to find the root of a function."""
    if func(a) * func(b) >= 0:
        raise ValueError("Function must have opposite signs at a and b.")

    iter_count = 0
    while abs(b - a) > tol and iter_count < max_iter:
        iter_count += 1
        p = (a + b) / 2
        if func(a) * func(p) < 0:
            b = p
        else:
            a = p

    print(f"Bisection method converged after {iter_count} iterations.")
    return (a + b) / 2

def fixed_point_iteration(g, p0, tol=1e-6, max_iter=100):
    """Fixed-point iteration method to find root of a function."""
    iter_count = 0

    while iter_count < max_iter:
        iter_count += 1
        p = g(p0)
        if abs(p - p0) < tol:
            print(f"Fixed-point iteration converged after {iter_count} iterations.")
            return p
        p0 = p

    print("Fixed-point iteration failed to converge.")
    return None

def newton_raphson(func, dfunc, p0, tol=1e-6, max_iter=100):
    """Newton-Raphson method to find root of a function."""
    iter_count = 0

    while iter_count < max_iter:
        iter_count += 1
        f_p0 = func(p0)
        df_p0 = dfunc(p0)

        if abs(df_p0) < tol:
            print("Derivative is too small. Newton-Raphson method failed.")
            return None

        p = p0 - f_p0 / df_p0
        if abs(p - p0) < tol:
            print(f"Newton-Raphson method converged after {iter_count} iterations.")
            return p
        p0 = p

    print("Newton-Raphson method failed to converge.")
    return None

# Example usage
def example_func(x):
    return x**3 - 2*x - 5

def example_dfunc(x):
    return 3*x**2 - 2

def g_func(x):
    return math.sqrt(2)

if __name__ == "__main__":
    # Approximation Algorithm
    print("Approximation Algorithm:")
    approximation_algorithm(1.5)

    # Bisection Method
    print("\nBisection Method:")
    root_bisection = bisection_method(example_func, 1, 3)
    print(f"Root (Bisection): {root_bisection:.6f}")

    # Fixed-Point Iteration
    print("\nFixed-Point Iteration:")
    root_fixed_point = fixed_point_iteration(g_func, 1.5)
    print(f"Root (Fixed-Point): {root_fixed_point:.6f}")

    # Newton-Raphson Method
    print("\nNewton-Raphson Method:")
    root_newton = newton_raphson(example_func, example_dfunc, 2)
    print(f"Root (Newton-Raphson): {root_newton:.6f}")