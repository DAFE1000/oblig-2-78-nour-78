import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# Likningen vi løser (for x)
def likning(x):
    return np.arctan(x) - 4/(x**2 +1)

#funksjon
def f(x):
    return np.exp(-x/4) * np.arctan(x)

# startverdi
x0 = 0.2

# Løs likning
løsning = fsolve(likning, x0)
x = løsning[0]

# Finn y-verdi
y = f(x)

# fire demsimaler
print(f"x = {x:.4f}")
print(f"y = {y:.4f}")

# Lage graf
x_vals = np.linspace(0, 5, 100)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals)
plt.scatter(x, y)  # toppunkt

plt.title("Graf av f(x)")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.savefig("plot.png")
plt.show()

