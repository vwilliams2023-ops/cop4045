import math
import matplotlib.pyplot as plt
import numpy as np

while True:

    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        # Two real roots
        sqrt_disc = math.sqrt(discriminant)
        x1 = (-b + sqrt_disc) / (2*a)
        x2 = (-b - sqrt_disc) / (2*a)
        print(f"\nTwo real roots:")
        print(f"x1 = {x1:.4f}")
        print(f"x2 = {x2:.4f}")
        roots = [x1, x2]
        
    elif discriminant == 0:
        # One real root 
        x1 = -b / (2*a)
        print(f"\nOne real root:")
        print(f"x1 = x2 = {x1:.4f}")
        roots = [x1]
        
    else:
        # Complex roots
        real_part = -b / (2*a)
        imag_part = math.sqrt(abs(discriminant)) / (2*a)
        print(f"\nComplex roots:")
        print(f"x1 = {real_part:.4f} + {imag_part:.4f}i")
        print(f"x2 = {real_part:.4f} - {imag_part:.4f}i")
        roots = []



    
x = np.linspace(x_min, x_max, 150)
    
   
y = a * x**2 + b * x + c
    
plt.plot(x, y, 'b-', linewidth=2)
plt.axhline(y=0, color='black')  # x-axis
plt.axvline(x=0, color='black')  # y-axis
plt.grid(True, alpha=0.3)
plt.title(f'y = {a}x² + {b}x + {c}')
plt.xlabel('x')
plt.ylabel('y')
plt.show(block=False)
plt.pause(0.1)

plt.show()

print("\n" + "-"*60)