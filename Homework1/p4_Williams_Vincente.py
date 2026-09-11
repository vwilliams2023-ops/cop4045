import math
import matplotlib.pyplot as plt


def plot_function(fun_str, domain, ns):
    
    xmin, xmax = domain
    
    xs = []
    step = (xmax - xmin) / (ns - 1)
    for i in range(ns):
        xs.append(xmin + i * step)
    
    ys = []
    for x in xs:
        y = eval(fun_str)
        ys.append(y)
    
    print()
    print("{:>12s} | {:>12s}".format("x", "y"))
    print("-" * 27)
    for x, y in zip(xs, ys):
        print("{:12.4f} | {:12.4f}".format(x, y))
    print()
    
    plt.plot(xs, ys)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("y = " + fun_str)
    plt.grid(True)
    plt.show()


fun_str = input("Enter function with variable x: ")
xmin = float(input("Enter xmin: "))
xmax = float(input("Enter xmax: "))
ns = int(input("Enter number of samples: "))

plot_function(fun_str, (xmin, xmax), ns)