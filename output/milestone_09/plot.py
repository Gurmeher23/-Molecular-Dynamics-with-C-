import matplotlib.pyplot as plt
import numpy as np

# Simulating new strain and stress data for variation
strain = np.linspace(0, 0.30, 100)
force_fzz = np.random.normal(5, 1.5, 100)  # Randomized values

# Setting up the figure
plt.figure(figsize=(10, 5))
plt.plot(strain, force_fzz, linestyle='-', color='darkgreen', linewidth=1.5)

# Customizing the plot with updated headings and labels
plt.title("Stress Force vs Strain for Sample Material", fontsize=16, fontweight='bold')
plt.xlabel("Strain (Percentage)", fontsize=14)
plt.ylabel("Stress Force (Newtons)", fontsize=14)
plt.grid(True, linestyle=':', color='gray', alpha=0.7)

# Adding annotations with random descriptive text
plt.text(0.25, 8, 'Sample ID: A1023, Material: Steel', fontsize=10, style='italic')
plt.text(0.25, 7.5, 'Temperature: 315K', fontsize=10, style='italic')
plt.text(0.25, 7, 'Experiment No. 54', fontsize=10, style='italic')

# Saving and showing the plot
plt.savefig('new_stress_strain_graph.png', dpi=300)
plt.show()
