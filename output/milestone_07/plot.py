import pandas as pd
from matplotlib import pyplot as plt
import os
import glob
import re

# Set plot parameters for better visualization
plt.rcParams["figure.figsize"] = [8.00, 5.00]  # Increased plot size for clarity
plt.rcParams["figure.autolayout"] = True

# Define the columns to read from each file
columns = ["iteration", "total_energy", "average_temp", "potential_energy"]
directory = './'
extension = 'csv'

# Helper function to sort files based on numbers in filenames
def num_sort(test_string):
    numbers = re.findall(r'\d+', test_string)
    return int(numbers[0]) if numbers else float('inf')

# Helper function to check if a file contains required columns
def has_required_columns(file, required_columns):
    df = pd.read_csv(file, nrows=1)
    return all(column in df.columns for column in required_columns)

# Change directory and get the list of files with the specified extension
os.chdir(directory)
energy_files = glob.glob('**/*.{}'.format(extension), recursive=True)
energy_files.sort(key=num_sort)
legend = []

heat_capacity = []
start_energies = []

# Process each energy file
for file in energy_files:
    if 'melting_points_vs_cluster_size' in file:
        continue
    if not has_required_columns(file, columns):
        print(f"Skipping {file} as it does not contain the required columns.")
        continue

    # Read the data from the CSV file
    energy_file = pd.read_csv(file, usecols=columns)

    # Plot total energy vs average temperature without markers (no circle)
    plt.plot(energy_file['average_temp'], energy_file['total_energy'],
             linestyle='-', linewidth=2)  # Removed 'marker' parameter

    legend.append(file.split("/")[0])

    # Calculate heat capacity
    delta_energy = energy_file['total_energy'].iloc[-1] - energy_file['total_energy'].iloc[0]
    delta_temp = energy_file['average_temp'].iloc[-1] - energy_file['average_temp'].iloc[0]
    heat_capacity.append(delta_energy / delta_temp)
    start_energies.append(energy_file['total_energy'].iloc[0])

# Customize labels, title, and grid
plt.xlabel("Average Temperature (K)", fontsize=12, fontweight='medium', color='darkblue')
plt.ylabel("Total Energy (J)", fontsize=12, fontweight='medium', color='darkblue')
plt.title("Total Energy vs Average Temp", fontsize=14, fontweight='bold', color='purple')

# Customize the grid
plt.grid(True, which='major', linestyle='--', linewidth=0.6, color='lightgray')

# Move the legend to the upper right
plt.legend(legend, loc='upper right', fontsize=10)

# Save the plot with a unique name
plt.savefig("custom_total_energy_vs_average_temp_no_markers.png", dpi=300)
plt.show()

# Clear the figure for the next plot
plt.clf()

# Plot melting points vs cluster size with distinct styles
columns2 = ["cluster_size", "melting_point", "number_of_iterations_till_melting", "added_energy", "atoms_number", "latent_energy"]
melting_file = pd.read_csv("melting_points_vs_cluster_size.csv", usecols=columns2)

plt.plot(melting_file['cluster_size'], melting_file['melting_point'],
         linestyle='-', marker='D', color='orange', markersize=6, linewidth=2)
plt.xlabel("Cluster Size", fontsize=12, fontweight='medium', color='darkgreen')
plt.ylabel("Melting Point (K)", fontsize=12, fontweight='medium', color='darkgreen')
plt.title("Melting Point vs Cluster Size", fontsize=14, fontweight='bold', color='green')

# Customize the grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='lightblue')

# Save the plot
plt.savefig("custom_melting_point_vs_cluster_size.png", dpi=300)
plt.show()

# Clear the figure for the next plot
plt.clf()

# Plot heat capacity vs cluster size with a distinct style
plt.plot(melting_file['cluster_size'], heat_capacity, linestyle='--', marker='o', color='red', markersize=6, linewidth=2)
plt.xlabel("Cluster Size", fontsize=12, fontweight='medium', color='maroon')
plt.ylabel("Heat Capacity (J/K)", fontsize=12, fontweight='medium', color='maroon')
plt.title("Heat Capacity vs Cluster Size", fontsize=14, fontweight='bold', color='brown')

# Customize the grid
plt.grid(True, linestyle='-.', linewidth=0.6, color='lightgray')

# Save the plot
plt.savefig("custom_heat_capacity_vs_cluster_size.png", dpi=300)
plt.show()

# Clear the figure for the next plot
plt.clf()

# Plot latent heat vs cluster size with a distinct style
plt.plot(melting_file['cluster_size'], melting_file['latent_energy'],
         linestyle='-', marker='^', color='purple', markersize=7, linewidth=1.8)
plt.xlabel("Cluster Size", fontsize=12, fontweight='medium', color='darkviolet')
plt.ylabel("Latent Heat (J)", fontsize=12, fontweight='medium', color='darkviolet')
plt.title("Latent Heat vs Cluster Size", fontsize=14, fontweight='bold', color='darkviolet')

# Customize the grid
plt.grid(True, linestyle='-', linewidth=0.5, color='lavender')

# Save the plot
plt.savefig("custom_latent_heat_vs_cluster_size.png", dpi=300)
plt.show()

# Clear the figure
plt.clf()
