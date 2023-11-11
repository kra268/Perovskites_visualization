import numpy as np
import matplotlib.pyplot as plt

def plot_dos(data, energy_range, labels, colors, title, filename):
    """
    Plot density of states (DOS) data and save the plot.

    Parameters
    ----------
    data : numpy.ndarray
        Array containing DOS data with two columns (energy and density).
    energy_range : tuple
        Tuple specifying the energy range for the plot.
    labels : list
        List of labels for each DOS curve.
    colors : list
        List of colors for each DOS curve.
    title : str
        Title for the plot.
    filename : str
        Filename to save the plot.

    Returns
    -------
    None
    """
    plt.plot(data[energy_range[0]:energy_range[1], 0], data[energy_range[0]:energy_range[1], 1], label=labels[0], c=colors[0])
    plt.plot(data[energy_range[2]:energy_range[3], 0], data[energy_range[2]:energy_range[3], 1], label=labels[1], c=colors[1])
    plt.plot(data[energy_range[4]:energy_range[5], 0], data[energy_range[4]:energy_range[5], 1], label=labels[2], c=colors[2])
    plt.plot(data[energy_range[6]:energy_range[7], 0], data[energy_range[6]:energy_range[7], 1], c=colors[3])
    plt.legend()
    plt.xlabel("Energy (eV)", fontstyle='normal', c='black', fontfamily='sans-serif', fontweight='bold')
    plt.ylabel("Density (states/eV)", fontstyle='normal', c='black', fontfamily='sans-serif', fontweight='bold')
    plt.title(title, fontweight="bold")
    plt.ylim(0)
    plt.xlim(energy_range[8], energy_range[9])  # Sets a limit
    plt.yticks([])  # Removes y-axis numbers
    plt.xticks(np.arange(energy_range[8], energy_range[9], 1))
    plt.savefig(filename, dpi=300)
    plt.show()

def main():
    """
    Main function to load DOS data and create plots for Anilinium and 2,3,4,5,6-FAn.

    Returns
    -------
    None
    """
    plt.figure(1)
    data_1 = np.loadtxt('BNH3.dat')
    plot_dos(data_1, (7930, 10000, 12925, 15000, 2940, 5000, 0, 5, -4, 5), ['Sn(p)', 'I(p)', 'Total DOS'], ['grey', 'violet', 'forestgreen'], 'Anilinium', 'Anilinium_Sn_I_states.png')

    plt.figure(2)
    data_2 = np.loadtxt('BF5NH3_C_N_F.dat')
    plot_dos(data_2, (7930, 10000, 12925, 15000, 17925, 20000, 2940, 5000, -4, 5), ['N(p)', 'C(p)', 'F(p)', 'Total DOS'], ['skyblue', 'peru', 'royalblue', 'forestgreen'], '2,3,4,5,6-FAn', 'BF5NH3_C_N_F_states.png')

if __name__ == "__main__":
    main()
