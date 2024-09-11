import pandas as pd
from matplotlib import pyplot as plt

atoms_number = 923

# Set plot parameters for better visualization
plt.rcParams["figure.figsize"] = [8.00, 5.00]  # Slightly larger plot size
plt.rcParams["figure.autolayout"] = True

# Plot 1: Time to demonstrate energy conservation vs Cores number
columns = ["cores", "real", "user", "sys"]
df = pd.read_csv(f"{atoms_number}/equilibrium_on_923_atoms.csv", usecols=columns)

# Plot user time vs cores with a new color palette and line style
plt.plot(df.cores, df.user, linestyle='-', color='teal', linewidth=2)
plt.xlabel("Cores number", fontsize=12, fontweight='medium', color='teal')
plt.ylabel("Time to demonstrate energy conservation (fs)", fontsize=12, fontweight='medium', color='teal')
plt.title("Time to demonstrate energy conservation vs Cores number", fontsize=14, fontweight='bold', color='purple')

# Customize the grid with lighter lines
plt.grid(True, linestyle='--', linewidth=0.6, color='lightgrey')

# Save and show the plot
plt.savefig(f"{atoms_number}/time_to_demonstrate_energy_conservation_vs_cores_number.png", dpi=300)
plt.show()

# Clear the figure for the next plot
plt.clf()

# Plot 2: Total energy vs Time steps for different core counts
columns = ["iteration", "total_energy", "potential_energy"]
cores8 = pd.read_csv(f"{atoms_number}/8_energies.csv", usecols=columns)
cores4 = pd.read_csv(f"{atoms_number}/4_energies.csv", usecols=columns)
cores2 = pd.read_csv(f"{atoms_number}/2_energies.csv", usecols=columns)
cores1 = pd.read_csv(f"{atoms_number}/1_energies.csv", usecols=columns)

# Plot total energy for different cores with thinner lines and no markers
plt.plot(cores8.iteration, cores8.total_energy, linestyle='-', color='steelblue', linewidth=1.5)
plt.plot(cores4.iteration, cores4.total_energy, linestyle='--', color='darkorange', linewidth=1.5)
plt.plot(cores2.iteration, cores2.total_energy, linestyle='-.', color='green', linewidth=1.5)
plt.plot(cores1.iteration, cores1.total_energy, linestyle=':', color='crimson', linewidth=1.5)

# Customize labels, title, and legend
plt.legend(["8 cores", "4 cores", "2 cores", "1 core"], loc='best', fontsize=10)
plt.xlabel("Time steps (fs)", fontsize=12, fontweight='medium', color='navy')
plt.ylabel("Total energy (eV)", fontsize=12, fontweight='medium', color='navy')
plt.title("Total energy vs Time steps", fontsize=14, fontweight='bold', color='darkblue')

# Customize the grid
plt.grid(True, linestyle='--', linewidth=0.6, color='lightgrey')

# Save and show the plot
plt.savefig(f"{atoms_number}/total_energy_vs_time_steps.png", dpi=300)
plt.show()

# Clear the figure
plt.clf()
