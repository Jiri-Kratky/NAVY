import numpy as np
import random

# Velikost pole
rows = 15
cols = 15

# Vytvoření pole
R = np.zeros((rows, cols), dtype=int)

# Náhodné umístění zdí
for i in range(rows):
    for j in range(cols):
        # 30% šance na umístění zdi
        if random.random() < 0.2:
            R[i, j] = -50  # Zdi

# Náhodné umístění cíle
goal_row = random.randint(0, rows - 1)
goal_col = random.randint(0, cols - 1)
R[goal_row, goal_col] = 50  # Cíl

R[R==0] = -1
