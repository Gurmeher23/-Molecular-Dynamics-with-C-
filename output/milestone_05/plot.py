import pandas as pd
from matplotlib import pyplot as plt

# Customize plot size and layout
plt.rcParams["figure.figsize"] = [8.00, 5.00]  # Balanced layout
plt.rcParams["figure.autolayout"] = True

# Read the CSV data
columns = ["atoms_number", "simulation_time"]
df = pd.read_csv("simulation_time_vs_atoms_number.csv", usecols=columns)

# Plot with a new color scheme and design
plt.plot(df.atoms_number, df.simulation_time, linestyle='-', marker='D', color='#FF6F61', markersize=7, linewidth=2.5, label="Simulation Time")

# Set labels and title with the updated color and font
plt.xlabel("Number of Atoms", fontsize=12, fontweight='medium', color='#4B0082')  # Dark purple
plt.ylabel("Simulation Time (seconds)", fontsize=12, fontweight='medium', color='#4B0082')  # Dark purple
plt.title("Simulation Time vs Atom Count", fontsize=14, fontweight='bold', color='#4B0082')

# Customize the grid with light blue lines
plt.grid(True, which='both', linestyle='-', linewidth=0.5, alpha=0.4, color='#B0E0E6')  # Pale blue

# Add a legend
plt.legend(loc="upper left", fontsize=10, facecolor='lightgray', edgecolor='black')

# Save the plot with a unique filename
plt.savefig("simulation_time_vs_atoms_number.png", dpi=300)

# Show the plot
plt.show()
