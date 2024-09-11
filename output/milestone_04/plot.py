import pandas as pd
from matplotlib import pyplot as plt
import os

# Set the path to the CSV file
csv_file_path = 'energies_vs_time_step.csv'

# Check if the file exists
if not os.path.exists(csv_file_path):
    raise FileNotFoundError(f"The file {csv_file_path} does not exist.")

# Set plot parameters
plt.rcParams["figure.figsize"] = [8.00, 5.00]  # Balanced layout
plt.rcParams["figure.autolayout"] = True

# Columns to read
columns = ["time_step", "total_energy", "kinetic_energy", "potential_energy"]

# Read the CSV file
df = pd.read_csv(csv_file_path, usecols=columns)

# Plot total energy vs. time step with updated design
plt.plot(df.time_step, df.total_energy, label='Total Energy', linestyle='-', marker='o', color='#FF6F61', markersize=7, linewidth=2.5)

# Set labels and title with consistent font and color styling
plt.xlabel("Time Step", fontsize=12, fontweight='medium', color='#4B0082')
plt.ylabel("Total Energy", fontsize=12, fontweight='medium', color='#4B0082')
plt.title("Total Energy vs Time Step", fontsize=14, fontweight='bold', color='#4B0082')

# Customize the grid with light blue lines
plt.grid(True, which='both', linestyle='-', linewidth=0.5, alpha=0.4, color='#B0E0E6')

# Add a legend with updated style
plt.legend(loc="upper right", fontsize=10, facecolor='lightgray', edgecolor='black')

# Save the plot with a unique filename
plt.savefig("custom_total_energy_vs_time_step.png", dpi=300)

# Show the plot
plt.show()
