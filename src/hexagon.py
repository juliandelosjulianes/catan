import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def draw_hex(ax, center, radius):
    hexagon = Polygon([((np.cos(2 * np.pi / 6 * (i + 0.5)) * radius) + center[0], (np.sin(2 * np.pi / 6 * (i + 0.5)) * radius) + center[1]) for i in range(6)], closed=True)
    ax.add_patch(hexagon)

fig, ax = plt.subplots()
ax.set_aspect('equal')

# Tamaño del tablero de Catan
board_size = 2  # Radio del tablero en hexágonos

# Crear el tablero con hexágonos
for q in range(-board_size, board_size + 1):
    for r in range(-board_size, board_size + 1):
        s = -q-r
        if abs(s) <= board_size:
            x_offset = 0.5 if r % 2 == 0 else 0
            draw_hex(ax, (q + x_offset, r * np.sqrt(3) / 2), 0.5)

# Configurar límites
ax.set_xlim(-board_size-1, board_size+1)
ax.set_ylim(-board_size-1, board_size+1)

plt.axis('off')
plt.show()
