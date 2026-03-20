import numpy as np
from scipy.optimize import fsolve


#Definere funksjonen:
def f(x):
    return np.arctan(x)- 4/(1+ x**2)

#Startverdien
x0= 1

#Løser likning 
løsning =fsolve(f, x0)

x= løsning[0]

#Printer ut svaret med 4 desimaler
print(f"x= {x:.4f}")

