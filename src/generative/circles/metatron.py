import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt
import numpy as np


def draw_circle(ax, center, radius):
    circle = plt.Circle(center, radius, fill=False, linewidth=1)
    ax.add_artist(circle)


def generate_flower_of_life_centers(radius, levels=2):
    centers = [(0, 0)]
    angles = np.arange(0, 360, 60)

    # First ring
    for angle in angles:
        rad = np.radians(angle)
        x = radius * np.cos(rad)
        y = radius * np.sin(rad)
        centers.append((x, y))

    # Second ring (hex around each first ring circle)
    if levels > 1:
        for (cx, cy) in centers[1:]:
            for angle in angles:
                rad = np.radians(angle)
                x = cx + radius * np.cos(rad)
                y = cy + radius * np.sin(rad)
                new_center = (x, y)
                if not any(np.allclose(new_center, existing, atol=1e-3) for existing in centers):
                    centers.append(new_center)

    return centers


def draw_metatrons_cube(radius=1.0):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')

    # Step 1: Get circle centers
    centers = generate_flower_of_life_centers(radius, levels=1)

    # Step 2: Draw 13 circles
    for center in centers:
        draw_circle(ax, center, radius)

    # Step 3: Connect all circle centers with lines
    for i, p1 in enumerate(centers):
        for j, p2 in enumerate(centers):
            if j > i:
                ax.plot([p1[0], p2[0]], [p1[1], p2[1]], linewidth=0.5, color='black')

    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    plt.title("Metatron's Cube", fontsize=14)
    plt.show()


if __name__ == '__main__':
    draw_metatrons_cube()