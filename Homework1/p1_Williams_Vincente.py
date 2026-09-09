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

    #Visualization Part

    print("\nGenerating visualization...")
    
    if roots:
        x_min = min(roots) - 3
        x_max = max(roots) + 3
    else:
        vertex_x = -b / (2*a)
        x_min = vertex_x - 5
        x_max = vertex_x + 5
    
    x_values = np.linspace(x_min, x_max, 400)
    
    y_values = a * x_values**2 + b * x_values + c
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(x_values, y_values, 'b-', linewidth=2, label=f'{a}x² + {b}x + {c}')
    
    plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
    
    plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
    
    if roots:
        for root in roots:
            plt.plot(root, 0, 'ro', markersize=10, label=f'Root: {root:.2f}')
    
    
    vertex_x = -b / (2*a)
    vertex_y = a * vertex_x**2 + b * vertex_x + c
    plt.plot(vertex_x, vertex_y, 'go', markersize=10, label=f'Vertex: ({vertex_x:.2f}, {vertex_y:.2f})')
    
    plt.grid(True, alpha=0.3)
    
    # Add labels and title
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title(f'Quadratic Function: y = {a}x² + {b}x + {c}', fontsize=14)
    
    plt.legend()
   
    y_min = min(y_values) - 1
    y_max = max(y_values) + 1
    plt.ylim(y_min, y_max)
    
    plt.show(block=False)  
    plt.pause(0.1)  
