import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

fonts_setting = {
        # Use LaTeX to write all text
        "text.usetex": True,
        "font.family": "serif",
        # Use 10pt font in plots, to match 10pt font in document
        "axes.labelsize": 12,
        "font.size": 12,
        # Make the legend/label fonts a little smaller
        "legend.fontsize": 12,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10
    }
plt.rcParams.update(fonts_setting)

def main():
    # Initial conditions
    C_initial = 100  # initial concentration in mM (milimolar)
    V_solvent = 10e-3  # volume of the solvent in liters (10 mL)
    V_added_per_step = 100e-6  # volume added per step in liters (100 µL)

    data_peak = []
    for i in range(0, 11):
        V_added_total = V_added_per_step * i  # total added volume in liters
        V_total = V_solvent + V_added_total  # total volume in liters
        C_final = (C_initial * V_added_total) / V_total  # final concentration in mM
        data = load_data(f"{i}x.csv", separate=",")
        data_max = data.max()
        print(data_max["i"], i*100)
        data_peak.append([data_max["i"], C_final])
    # Create a DataFrame from data_peak
    df = pd.DataFrame(data_peak, columns=["v", "i"])

    # Create subplots
    fig, axs = plt.subplots(3, 1, figsize=(8.27, 11.69), dpi=100)

    # Plotting the data
    axs[1].plot(df['i'], df['v'], marker='x', color=cm.get_cmap('viridis')(0.5))
    axs[1].set_title('Kalibrační křivka')
    axs[1].set_ylabel(r'$|I|$ $[mA]$')
    axs[1].set_xlabel(r'$C_{CdCl_2} [mMol/l]$')
    axs[1].set_xlim(0, 9.1)
    axs[1].grid(True)

    for i in range(0, 11):
        data = load_data(f"{i}x.csv", separate=",")
        color = cm.get_cmap('viridis')(i/10)  # Get color from Veridis colormap
        axs[0].plot(data["v"], data["i"], label=f"{i*100}", color=color)
    axs[0].legend(title=r'$CdCl_2$ roztok $[uL]$', loc="center left", bbox_to_anchor=(1.05, 0.5))
    axs[0].set_ylabel(r'$I$ $[mA]$')
    axs[0].set_xlim(-1.4, -0.4)
    axs[0].set_xlabel(r'$U [V]$')
    axs[0].grid(True)

    string_list = ["kya10.csv", "kya20.csv","kya50.csv" ,"kya100.csv" , "kya200.csv"]
    for i,string in enumerate(string_list):
        data = load_data(string)
        color = cm.get_cmap('viridis')((i+1)/5)  # Get color from Veridis colormap
        axs[2].plot(data["v"], 1000*data["i"], color=color, label=f"{string.split('a')[1].split('.')[0]}")
    axs[2].legend(title="Náběhové napětí [mV/s]", loc="center left", bbox_to_anchor=(1, 0.5))
    axs[2].set_xlabel("U [V]")
    axs[2].set_ylabel("I [mA]")
    axs[2].set_xlim(-1, 1)
    axs[2].set_ylim(-2, 1.2)
    axs[2].grid(True)

    # Adjust spacing between subplots
    plt.tight_layout()

    # Save the figure
    plt.savefig("all_plots.pdf")

    # Show the figure
    plt.show()

    data = load_data(f"xx.csv", separate=",")
    data_max = data.max()
    print(data_max)


def load_data(file,separate = "\t"):
    data = pd.read_csv(file, sep=separate)
    return data







if __name__ == "__main__":
    main()