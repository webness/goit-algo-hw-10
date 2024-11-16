import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


def f(x):
    return x ** 2


a = 0  # Lower limit
b = 2  # Upper limit


def monte_carlo_integration(func, a, b, num_samples=10000):
    x_random = np.random.uniform(a, b, num_samples)  # Random points in [a, b]
    y_random = func(x_random)  # Function values at these points
    area = (b - a) * np.mean(y_random)  # Monte Carlo estimate
    return area


def validate_integration(func, a, b, monte_carlo_result, num_samples=10000):
    analytical_result = (b ** 3 / 3) - (a ** 3 / 3)

    quad_result, _ = quad(func, a, b)

    print(f"Monte Carlo Result ({num_samples} samples): {monte_carlo_result}")
    print(f"Analytical Result: {analytical_result}")
    print(f"Quad Function Result: {quad_result}")

    return monte_carlo_result, analytical_result, quad_result


num_samples = 10000
monte_carlo_result = monte_carlo_integration(f, a, b, num_samples)

validate_integration(f, a, b, monte_carlo_result, num_samples)

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Integration of f(x) = x^2 from ' + str(a) + ' to ' + str(b))
plt.grid()
plt.show()
