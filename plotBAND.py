import numpy as np
import matplotlib.pyplot as plt

def plot_band(data, xlim, ylim, title, filename):
    """
    Plot band data and save the plot.

    Parameters
    ----------
    data : numpy.ndarray
        Array containing band data with two columns (wave vector and energy).
    xlim : tuple
        Tuple specifying the x-axis limits.
    ylim : tuple
        Tuple specifying the y-axis limits.
    title : str
        Title for the plot.
    filename : str
        Filename to save the plot.

    Returns
    -------
    None
    """
    plt.plot(data[:, 0], data[:, 1], c='royalblue')
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel('Wave Vector', fontstyle='normal', c='black', fontfamily='sans-serif', fontweight='bold')
    plt.ylabel('Energy (eV)', fontstyle='normal', c='black', fontfamily='sans-serif', fontweight='bold')
    plt.title(title, fontweight='bold')
    plt.savefig(filename, dpi=300)
    plt.show()

def main():
    """
    Main function to load band data and create plots for orthorhombic and cubic structures.

    Returns
    -------
    None
    """
    data_1 = np.loadtxt('orthoBAND.dat')
    plot_band(data_1, (0, 3), (-5, 5), 'Orthorhombic', 'orthoBAND.png')

    data_2 = np.loadtxt('cubicBAND.dat')
    plot_band(data_2, (0, 2.5), (-5, 5), 'Cubic', 'cubicBAND.png')

if __name__ == "__main__":
    main()
