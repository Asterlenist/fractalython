import matplotlib.pyplot as plt
import numpy as np
def koch_snowflake(order, scale=10):
    angles = np.array([np.pi/2, np.pi/2 + 2*np.pi/3, np.pi/2 + 4*np.pi/3, np.pi/2])
    points = scale * np.exp(1j * angles)
    for _ in range(order):
        new_points = []
        for i in range(len(points) - 1):
            p1 = points[i]
            p2 = points[i+1]
            v = p2 - p1
            a = p1 + v / 3
            b = p1 + 2 * v / 3
            c = a + (b - a) * np.exp(-1j * np.pi / 3)
            new_points.extend([p1, a, c, b])
        new_points.append(points[-1])
        points = np.array(new_points)
    return points
order = 5
points = koch_snowflake(order)
plt.figure(figsize=(30, 30), dpi=100)
plt.plot(points.real, points.imag, color='white', linewidth=1.5)
plt.axis('equal')
plt.axis('off')
plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
plt.margins(0, 0)
plt.savefig('koch_snowflake_black.png', bbox_inches='tight', pad_inches=0, facecolor='black')
print("Done.")
