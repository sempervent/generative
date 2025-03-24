import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt
import numpy as np
import colorsys


def get_circle_color(mode='gray', index=0, total=1, center=(0, 0)):
    if mode == 'gray':
        # Evenly spaced grayscale from dark to light
        gray = 0.2 + 0.6 * (index / max(total - 1, 1))  # Avoid div/0
        return (gray, gray, gray)

    elif mode == 'color':
        # Hue based on index (rainbow cycle)
        hue = index / total
        r, g, b = colorsys.hsv_to_rgb(hue, 0.8, 0.9)
        return (r, g, b)

    elif callable(mode):
        return mode(index=index, total=total, center=center)

    return 'black'  # Fallback default


def draw_circle(ax, center, radius, color):
    circle = plt.Circle(center, radius, fill=False, linewidth=2, edgecolor=color)
    ax.add_artist(circle)


def generate_hexagon_circle_centers(center, radius):
    cx, cy = center
    angles_deg = np.arange(0, 360, 60)
    centers = []

    for angle in angles_deg:
        rad = np.radians(angle)
        x = cx + radius * np.cos(rad)
        y = cy + radius * np.sin(rad)
        centers.append((x, y))

    return centers


def draw_seed_of_life(radius=1.0, color_mode='gray', background_color='black'):
    fig, ax = plt.subplots()
    fig.patch.set_facecolor(background_color)  # Set figure background
    ax.set_facecolor(background_color)
    ax.set_aspect('equal')
    ax.axis('off'

            )

    center = (0, 0)
    all_centers = [center] + generate_hexagon_circle_centers(center, radius)

    for idx, c in enumerate(all_centers):
        color = get_circle_color(mode=color_mode, index=idx, total=len(all_centers), center=c)
        draw_circle(ax, c, radius, color)

    ax.set_xlim(-3 * radius, 3 * radius)
    ax.set_ylim(-3 * radius, 3 * radius)
    plt.title("Seed of Life", fontsize=14, color='white' if background_color == 'black' else 'black')
    plt.show()


if __name__ == "__main__":
    draw_seed_of_life(radius=1.0, color_mode='gray')  # Grayscale
    # draw_seed_of_life(radius=1.0, color_mode='color')  # Colorful rainbow