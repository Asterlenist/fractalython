import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
def mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    C = x + y[:, None] * 1j
    Z = np.zeros_like(C)
    output = np.zeros(C.shape, dtype=float)
    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        Z[mask] = Z[mask] ** 2 + C[mask]
        output[mask] = i
    output[output == max_iter - 1] = np.nan
    return output
width, height = 3000, 3000
max_iter = 256
image = mandelbrot(-2.0, 1.0, -1.5, 1.5, width, height, max_iter)
plt.figure(figsize=(30, 30), dpi=100)
colors = [(0, 0, 0, 0), (1, 0, 1, 1)]
cmap = mcolors.LinearSegmentedColormap.from_list("custom", colors, N=256)
plt.imshow(image.T, extent=[-2.0, 1.0, -1.5, 1.5], cmap=cmap, origin='lower')
plt.axis('off')
plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
plt.margins(0, 0)
plt.savefig('mandelbrot_black.png', bbox_inches='tight', pad_inches=0, facecolor='black')
print("Done.")
