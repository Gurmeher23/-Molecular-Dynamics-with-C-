import pandas as pd
from matplotlib import pyplot as plt

# Customize plot size and layout
plt.rcParams["figure.figsize"] = [8.00, 5.00]  # Balanced layout
plt.rcParams["figure.autolayout"] = True

# Data for the plot
data = {
    "atoms_number": [9, 27, 64, 100, 125, 150, 200, 216, 294],
    "simulation_time": [0.068, 0.191, 0.422, 0.564, 0.659, 0.747, 1.058, 1.213, 1.861]
}

# Create DataFrame
df = pd.DataFrame(data)

# Line plot with a different color scheme
plt.plot(df.atoms_number, df.simulation_time, linestyle='-', marker='D', color='#FF6F61', markersize=7, linewidth=2.5, label="Simulation Time")

# Set labels and title with clean fonts
plt.xlabel("Number of Atoms", fontsize=12, fontweight='medium', color='#4B0082')  # Dark purple color
plt.ylabel("Simulation Time (seconds)", fontsize=12, fontweight='medium', color='#4B0082')  # Dark purple color
plt.title("Simulation Time vs Atom Count", fontsize=14, fontweight='bold', color='#4B0082')

# Customize the grid with a light color
plt.grid(True, which='both', linestyle='-', linewidth=0.5, alpha=0.4, color='#B0E0E6')  # Pale blue

# Add a legend with new color settings
plt.legend(loc="upper left", fontsize=10, facecolor='lightgray', edgecolor='black')

# Save the plot with a unique filename
plt.savefig("custom_color_simulation_time_vs_atoms_number.png", dpi=300)

# Show the plot
plt.show()
