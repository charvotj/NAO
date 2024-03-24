import pandas as pd
from matplotlib import rc
import matplotlib.pyplot as plt
# Set LaTeX font for labels
rc('text', usetex=True)
# lmodern font
rc('font', **{'family': 'serif', 'serif': ['lmodern']})

# foto tranzistor E=0 lux,,E=727 lux,,E=1590 lux,
#               U[V],I[mA],U[V],I[mA],U[V],I[mA]
def main():
    plot_possitive()
    plot_negative()
    #All_in_one()

def plot_possitive():
    path_trans = '5-fototranzistor.csv'
    path_res = '3-fotoodpor.csv'
    path_diode = '2-dioda.csv'
    path_resistance = '3-odpor-odporu.csv'
    
    data_trans = pd.read_csv(path_trans, sep=',', header=None)
    data_res = pd.read_csv(path_res, sep=',', header=None)
    data_diode = pd.read_csv(path_diode, sep=',', header=None)
    data_resistance = pd.read_csv(path_resistance, sep=',', header=None)
    
    fig, axs = plt.subplots(2, 2, figsize=(11.69, 8.24))  # A4 size on its side
    
    axs[0, 0].plot(data_trans[0][data_trans[0]>0], data_trans[1][data_trans[0]>0], label=r'$E=0$ lux', marker='x')
    axs[0, 0].plot(data_trans[2][data_trans[2]>0], data_trans[3][data_trans[2]>0], label=r'$E=727$ lux', marker='x')
    axs[0, 0].plot(data_trans[4][data_trans[4]>0], data_trans[5][data_trans[4]>0] , label=r'$E=1590$ lux', marker='x')
    axs[0, 0].set_xlabel(r'$U$ [V]')
    axs[0, 0].set_ylabel(r'$I$ [mA]')
    axs[0, 0].legend(loc="best")
    axs[0, 0].set_title(r'Graf 1: A-V charakteristika fototranzistoru v propustném směru')
    axs[0, 0].grid(True)  # Add grid
    
    axs[0, 1].plot(data_res[0][data_res[0]>0], data_res[1][data_res[0]>0], label=r'$E=0$ lux', marker='x')
    axs[0, 1].plot(data_res[2][data_res[2]>0], data_res[3][data_res[2]>0], label=r'$E=729$ lux', marker='x')
    axs[0, 1].plot(data_res[4][data_res[4]>0], data_res[5][data_res[4]>0], label=r'$E=1583$ lux', marker='x')
    axs[0, 1].set_xlabel(r'$U$ [V]')
    axs[0, 1].set_ylabel(r'$I$ [mA]')
    axs[0, 1].legend(loc="best")
    axs[0, 1].set_title(r'Graf 2: A-V charakteristika fotoodporu v propustném směru')   
    axs[0, 1].grid(True)  # Add grid
    
    axs[1, 0].plot(-data_diode[0][-data_diode[0]>0], -data_diode[1][-data_diode[0]>0], label=r'$E=0$ lux', marker='x')
    axs[1, 0].plot(-data_diode[2][-data_diode[2]>0], -data_diode[3][-data_diode[2]>0], label=r'$E=731$ lux', marker='x')
    axs[1, 0].plot(-data_diode[4][-data_diode[4]>0], -data_diode[5][-data_diode[4]>0], label=r'$E=1575$ lux', marker='x')
    axs[1, 0].set_xlabel(r'$U$ [V]')
    axs[1, 0].set_ylabel(r'$I$ [mA]')
    axs[1, 0].legend(loc="best")
    axs[1, 0].set_title(r'Graf 3: A-V charakteristika fotodiody v propustném směru')
    axs[1, 0].grid(True)  # Add grid
    
    axs[1, 1].plot(data_resistance[0], data_resistance[1], marker='x')
    axs[1, 1].set_xlabel(r'$E$ [lux]')
    axs[1, 1].set_ylabel(r'$R$ [$k\Omega$]')
    axs[1, 1].set_ylim(0, 2e5)
    axs[1, 1].set_xscale('log')
    axs[1, 1].set_title(r'Graf 4: Závislost odporu na osvětlení')
    axs[1, 1].grid(True)  # Add grid
    
    # Move the title below the graph
    axs[0, 0].title.set_position([0.5, -0.2])
    axs[0, 1].title.set_position([0.5, -0.2])
    axs[1, 0].title.set_position([0.5, -0.2])
    axs[1, 1].title.set_position([0.5, -0.2])    
    plt.tight_layout()
    plt.savefig('possitive.png', dpi=300)
    #plt.show()

def plot_negative():
    path_trans = '5-fototranzistor.csv'
    path_res = '3-fotoodpor.csv'
    path_diode = '2-dioda.csv'
    path_resistance = '3-odpor-odporu.csv'
    
    data_trans = pd.read_csv(path_trans, sep=',', header=None)
    data_res = pd.read_csv(path_res, sep=',', header=None)
    data_diode = pd.read_csv(path_diode, sep=',', header=None)
    data_resistance = pd.read_csv(path_resistance, sep=',', header=None)
    
    fig, axs = plt.subplots(2, 2, figsize=(11.69, 8.27))  # A4 size on its side
    
    axs[0, 0].plot(data_trans[0][data_trans[0]<0], data_trans[1][data_trans[0]<0], label=r'$E=0$ lux', marker='x')
    axs[0, 0].plot(data_trans[2][data_trans[2]<0], data_trans[3][data_trans[2]<0], label=r'$E=727$ lux', marker='x')
    axs[0, 0].plot(data_trans[4][data_trans[4]<0], data_trans[5][data_trans[4]<0] , label=r'$E=1590$ lux', marker='x')
    axs[0, 0].set_xlabel(r'$U$ [V]')
    axs[0, 0].set_ylabel(r'$I$ [mA]')
    axs[0, 0].legend(loc="best")
    axs[0, 0].set_title(r'Graf 5: A-V charakteristika tranzistoru v závěrném směru')
    axs[0, 0].grid(True)  # Add grid
    
    axs[0, 1].plot(data_res[0][data_res[0]<0], data_res[1][data_res[0]<0], label=r'$E=0$ lux', marker='x')
    axs[0, 1].plot(data_res[2][data_res[2]<0], data_res[3][data_res[2]<0], label=r'$E=729$ lux', marker='x')
    axs[0, 1].plot(data_res[4][data_res[4]<0], data_res[5][data_res[4]<0], label=r'$E=1583$ lux', marker='x')
    axs[0, 1].set_xlabel(r'$U$ [V]')
    axs[0, 1].set_ylabel(r'$I$ [mA]')
    axs[0, 1].legend(loc="best")
    axs[0, 1].set_title(r'Graf 6: A-V charakteristika fotoodporu v závěrném směru')
    axs[0, 1].grid(True)  # Add grid
    
    axs[1, 0].plot(-data_diode[0][-data_diode[0]<0], -data_diode[1][-data_diode[0]<0], label=r'$E=0$ lux', marker='x')
    axs[1, 0].plot(-data_diode[2][-data_diode[2]<0], -data_diode[3][-data_diode[2]<0], label=r'$E=731$ lux', marker='x')
    axs[1, 0].plot(-data_diode[4][-data_diode[4]<0], -data_diode[5][-data_diode[4]<0], label=r'$E=1575$ lux', marker='x')
    axs[1, 0].set_xlabel(r'$U$ [V]')
    axs[1, 0].set_ylabel(r'$I$ [mA]')
    axs[1, 0].legend(loc="best")
    axs[1, 0].set_title(r'Graf 7: A-V charakteristika fotodiody v závěrném směru')
    axs[1, 0].grid(True)  # Add grid
    
    # Remove the empty subplot
    fig.delaxes(axs[1, 1])
    
    # Move the title below the graph
    axs[0, 0].title.set_position([0.5, -0.2])
    axs[0, 1].title.set_position([0.5, -0.2])
    axs[1, 0].title.set_position([0.5, -0.2])
 
    plt.tight_layout()
    #plt.show()
    plt.savefig('negative.png', dpi=300)

def All_in_one():
    path_trans = '5-fototranzistor.csv'
    path_res = '3-fotoodpor.csv'
    path_diode = '2-dioda.csv'
    path_resistance = '3-odpor-odporu.csv'
    
    data_trans = pd.read_csv(path_trans, sep=',', header=None)
    data_res = pd.read_csv(path_res, sep=',', header=None)
    data_diode = pd.read_csv(path_diode, sep=',', header=None)
    data_resistance = pd.read_csv(path_resistance, sep=',', header=None)
    
    fig, axs = plt.subplots(2, 3, figsize=(8.69, 11.27))  # A4 size on its side
    
    axs[0, 0].plot(data_trans[0], data_trans[1], label=r'$E=0$ lux', marker='x')
    axs[0, 0].plot(data_trans[2], data_trans[3], label=r'$E=727$ lux', marker='x')
    axs[0, 0].plot(data_trans[4], data_trans[5], label=r'$E=1590$ lux', marker='x')
    axs[0, 0].set_xlabel(r'$U$ [V]')
    axs[0, 0].set_ylabel(r'$I$ [mA]')
    axs[0, 0].legend()
    axs[0, 0].set_title(r'Graf 1: Závislost tranzistoru na osvětlení')
    axs[0, 0].grid(True)  # Add grid

    axs[1, 0].plot(data_trans[0][data_trans[0]<0], data_trans[1][data_trans[0]<0], label=r'$E=0$ lux', marker='x')
    axs[1, 0].plot(data_trans[2][data_trans[2]<0], data_trans[3][data_trans[2]<0], label=r'$E=727$ lux', marker='x')
    axs[1, 0].plot(data_trans[4][data_trans[4]<0], data_trans[5][data_trans[4]<0] , label=r'$E=1590$ lux', marker='x')
    axs[1, 0].set_xlabel(r'$U$ [V]')
    axs[1, 0].set_ylabel(r'$I$ [mA]')
    axs[1, 0].legend()
    axs[1, 0].set_title(r'Graf 1: Závislost tranzistoru na osvětlení')
    axs[1, 0].grid(True)  # Add grid
    
    axs[0, 1].plot(data_res[0], data_res[1], label=r'$E=0$ lux', marker='x')
    axs[0, 1].plot(data_res[2], data_res[3], label=r'$E=729$ lux', marker='x')
    axs[0, 1].plot(data_res[4], data_res[5], label=r'$E=1583$ lux', marker='x')
    axs[0, 1].set_xlabel(r'$U$ [V]')
    axs[0, 1].set_ylabel(r'$I$ [mA]')
    axs[0, 1].legend()
    axs[0, 1].set_title(r'Graf 2: Závislost fotoodporu na osvětlení')
    axs[0, 1].grid(True)  # Add grid

    axs[1, 1].plot(-data_diode[0][-data_diode[0]<0], -data_diode[1][-data_diode[0]<0], label=r'$E=0$ lux', marker='x')
    axs[1, 1].plot(-data_diode[2][-data_diode[2]<0], -data_diode[3][-data_diode[2]<0], label=r'$E=731$ lux', marker='x')
    axs[1, 1].plot(-data_diode[4][-data_diode[4]<0], -data_diode[5][-data_diode[4]<0], label=r'$E=1575$ lux', marker='x')
    axs[1, 1].set_xlabel(r'$U$ [V]')
    axs[1, 1].set_ylabel(r'$I$ [mA]')
    axs[1, 1].legend()
    axs[1, 1].set_title(r'Graf 3: Závislost diody na osvětlení')
    axs[1, 1].grid(True)  # Add grid

    axs[0, 2].plot(data_res[0][data_res[0]<0], data_res[1][data_res[0]<0], label=r'$E=0$ lux', marker='x')
    axs[0, 2].plot(data_res[2][data_res[2]<0], data_res[3][data_res[2]<0], label=r'$E=729$ lux', marker='x')
    axs[0, 2].plot(data_res[4][data_res[4]<0], data_res[5][data_res[4]<0], label=r'$E=1583$ lux', marker='x')
    axs[0, 2].set_xlabel(r'$U$ [V]')
    axs[0, 2].set_ylabel(r'$I$ [mA]')
    axs[0, 2].legend()
    axs[0, 2].set_title(r'Graf 2: Závislost fotoodporu na osvětlení')
    axs[0, 2].grid(True)  # Add grid
    
    axs[1, 2].plot(-data_diode[0], -data_diode[1], label=r'$E=0$ lux', marker='x')
    axs[1, 2].plot(-data_diode[2], -data_diode[3], label=r'$E=731$ lux', marker='x')
    axs[1, 2].plot(-data_diode[4], -data_diode[5], label=r'$E=1575$ lux', marker='x')
    axs[1, 2].set_xlabel(r'$U$ [V]')
    axs[1, 2].set_ylabel(r'$I$ [mA]')
    axs[1, 2].legend()
    axs[1, 2].set_title(r'Graf 3: Závislost diody na osvětlení')
    axs[1, 2].grid(True)  # Add grid

    #axs[1, 3].plot(data_resistance[0], data_resistance[1], marker='x')
    #axs[1, 3].set_xlabel(r'$E$ [lux]')
    #axs[1, 3].set_ylabel(r'$R$ [$k\Omega$]')
    #axs[1, 3].set_ylim(0, 2e5)
    #axs[1, 3].set_xscale('log')
    #axs[1, 3].set_title(r'Graf 4: Závislost odporu na osvětlení')
    #axs[1, 3].grid(True)  # Add grid
    #
    ## Move the title below the graph
    #axs[0, 0].title.set_position([0.5, -0.2])
    #axs[0, 1].title.set_position([0.5, -0.2])
    #axs[1, 0].title.set_position([0.5, -0.2])
    #axs[1, 1].title.set_position([0.5, -0.2])    
    plt.tight_layout()
    plt.show()
   
    
if __name__ == '__main__':
    main()