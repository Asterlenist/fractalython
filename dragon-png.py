import matplotlib.pyplot as plt
import numpy as np
def dragon_curve(iterations):
    points = np.array([0 + 0j, 1 + 0j])
    rotate = 1j
    for _ in range(iterations):
        last_point = points[-1]
        new_points = last_point + (points[-2::-1] - last_point) * rotate
        points = np.concatenate((points, new_points))
    return points
iterations = 16
points = dragon_curve(iterations)
plt.figure(figsize=(30, 30), dpi=100)
plt.plot(points.real, points.imag, color='white', linewidth=0.8)
plt.axis('equal')
plt.axis('off')
plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
plt.margins(0, 0)
plt.savefig('dragon_curve_transparent.png', bbox_inches='tight', pad_inches=0, transparent=True)
print("Done.")
