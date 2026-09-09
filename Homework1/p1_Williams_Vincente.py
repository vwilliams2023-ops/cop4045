import math
import matplotlib.pyplot as plt
import numpy as np

while True:
    a_input = input("Enter coefficient a (or press ENTER to exit): ")
    if a_input == "":
        break
    
    a = float(a_input)
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    
    d = b**2 - 4*a*c
    
    if d < 0:
        print("no real solutions")
        x_center = -b / (2*a)
        x = np.linspace(x_center - 5, x_center + 5, 150)
        roots = []
    elif d == 0:
        x1 = -b / (2*a)
        print(f"one solution: {x1:.4f}")
        x = np.linspace(x1 - 3, x1 + 3, 150)
        roots = [x1]
    else:
        sqrt_d = math.sqrt(d)
        x1 = (-b + sqrt_d) / (2*a)
        x2 = (-b - sqrt_d) / (2*a)
        print(f"two solutions: {x1:.4f} and {x2:.4f}")
        x = np.linspace(min(x1, x2) - 2, max(x1, x2) + 2, 150)
        roots = [x1, x2]
    
    y = a * x**2 + b * x + c
    
    # --- CREATE PLOT IN NEW WINDOW ---
    plt.figure()  
    
    plt.plot(x, y, 'b-', linewidth=2)
    plt.axhline(0, color='k')
    plt.axvline(0, color='k')
    
    for r in roots:
        plt.plot(r, 0, 'ro', markersize=8)
    
    plt.grid(True, alpha=0.3)
    plt.title(f'y = {a}x² + {b}x + {c}')
    plt.xlabel('x')
    plt.ylabel('y')
    
    plt.show()