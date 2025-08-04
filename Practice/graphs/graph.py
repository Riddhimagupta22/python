import matplotlib.pyplot as plt
import numpy as np

try:
    start = float(input("Enter the starting of range (example :- -1) :- "))
    points = int(input("Enter number of points (example :- 10) :- "))
    end = float(input("Enter the ending of range (example :- 1) :- "))
except ValueError:
    print("Invalid input!")
    exit()

x = np.linspace(start, end, points)

square = input("Plot x^2? (yes/no):- ").lower()
cube = input("Plot x^3? (yes/no):- ").lower()

if square in ("yes", "y"):
    y = x**2
    plt.plot(x, y, '*-', label='x^2', color='blue')

if cube in ("yes", "y"):
    z = x**3
    plt.plot(x, z, 'o-', label='x^3', color='red')

plt.xlabel('X Values', fontsize=15)
plt.ylabel('Y Values', fontsize=15)
plt.title('User-driven plot of x^2 and/or x^3', fontsize=18, fontweight='bold')

if square in ("yes", "y") or cube in ("yes", "y"):
    plt.legend()

plt.grid(True,linestyle = '--', alpha = 0.7)
plt.show()
