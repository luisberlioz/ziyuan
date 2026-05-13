import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(10, 2.5))
ax.set_xlim(-6, 6)
ax.set_ylim(-1, 1)

# Draw the number line
ax.axhline(y=0, color='black', linewidth=2)
ax.arrow(6, 0, 0.3, 0, head_width=0.15, head_length=0.2, fc='black', ec='black')
ax.arrow(-6, 0, -0.3, 0, head_width=0.15, head_length=0.2, fc='black', ec='black')

# Tick marks and labels
for i in range(-5, 6):
    ax.plot(i, 0, 'k|', markersize=12)
    ax.text(i, -0.15, str(i), ha='center', va='top', fontsize=11, fontweight='bold')

# Labels
ax.text(-4.5, -0.5, 'Números\nnegativos', ha='center', va='top', fontsize=10, color='blue', fontweight='bold')
ax.text(0, -0.5, 'Cero', ha='center', va='top', fontsize=10, color='green', fontweight='bold')
ax.text(4.5, -0.5, 'Números\npositivos', ha='center', va='top', fontsize=10, color='red', fontweight='bold')

ax.set_title('La Recta Real', fontsize=14, fontweight='bold', pad=15)
ax.axis('off')
plt.tight_layout()
plt.savefig('/data/MyTera/ziyuan/recta_real.png', dpi=150, bbox_inches='tight')
print("Done!")
