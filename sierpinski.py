import matplotlib.pyplot as plt
import matplotlib.patches as patches
def draw_sierpinski(ax, p1, p2, p3, level):
    if level == 0:
        triangle = patches.Polygon([p1, p2, p3], closed=True, facecolor='white', edgecolor='none')
        ax.add_patch(triangle)
    else:
        mid1 = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
        mid2 = ((p2[0] + p3[0]) / 2, (p2[1] + p3[1]) / 2)
        mid3 = ((p3[0] + p1[0]) / 2, (p3[1] + p1[1]) / 2)
        draw_sierpinski(ax, p1, mid1, mid3, level - 1)
        draw_sierpinski(ax, mid1, p2, mid2, level - 1)
        draw_sierpinski(ax, mid3, mid2, p3, level - 1)
level = 8
fig, ax = plt.subplots(figsize=(30, 30), dpi=100)
h = (3**0.5) / 2
p1 = (0, h)
p2 = (-0.5, 0)
p3 = (0.5, 0)
draw_sierpinski(ax, p1, p2, p3, level)
ax.set_xlim(-0.6, 0.6)
ax.set_ylim(-0.1, h + 0.1)
ax.axis('equal')
ax.axis('off')
plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
plt.savefig('sierpinski_black.png', bbox_inches='tight', pad_inches=0, facecolor='black')
print("Done.")
