import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt
import numpy as np

def draw_circle(ax, center, radius):
    circle = plt.Circle(center, radius, fill=False, linewidth=2)
    ax.add_artist(circle)

def generate_hexagon_circle_centers(center, radius):
    cx, cy = center
    angles_deg = np.arange(0, 360, 60)  # 6 directions
    centers = []

    for angle in angles_deg:
        rad = np.radians(angle)
        x = cx + radius * np.cos(rad)
        y = cy + radius * np.sin(rad)
        centers.append((x, y))

    return centers

def draw_seed_of_life(radius=1.0):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')

    center = (0, 0)
    draw_circle(ax, center, radius)  # Center circle

    outer_centers = generate_hexagon_circle_centers(center, radius)
    for oc in outer_centers:
        draw_circle(ax, oc, radius)

    ax.set_xlim(-3*radius, 3*radius)
    ax.set_ylim(-3*radius, 3*radius)
    plt.title("Seed of Life", fontsize=14)
    plt.show()

if __name__ == "__main__":
    draw_seed_of_life()