import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

def make_first_plot(filename:str):
    # Read the CSV file, skipping the first two rows
    # and considering the third row as the header
    data = pd.read_csv(filename, delimiter='	')
    data['Id(Mp1)'] *= 1e6
    data['Id(Mp2)'] *= 1e6
    data['Id(Mp3)'] *= 1e6

    # Display the data
    # print(data)
    
    x_data = data['vcc']
    y1_data = data['Id(Mp1)']
    y2_data = data['Id(Mp2)']
    y3_data = data['Id(Mp3)']
    # Plot the data
    plt.plot(x_data, y1_data, label='Id(Mp1)')
    plt.plot(x_data, y2_data, label='Id(Mp2)')
    plt.plot(x_data, y3_data, label='Id(Mp3)')

   
 # First difference
    x_values = [0.9*1.8, 1.1*1.8]
    y_values = [y3_data[(x_data >= x_values[0]).idxmax()], y3_data[(x_data >= x_values[1]).idxmax()]]
    calc_value=abs(y_values[1]-y_values[0])
    plt.plot(x_values, [y_values[1],y_values[1]], color='b', linestyle=':')
    plt.plot([x_values[0],x_values[0]], y_values, color='b', linestyle=':')
    plt.annotate(r'$\Delta I='+f'{calc_value:.2f} \mu A'+r'(U_{CC}\pm 10\%)$', 
                xy=(x_values[0],y_values[1]), 
                xytext=(x_values[0]-0.2,y_values[1]-5), 
                arrowprops=dict(facecolor='black', arrowstyle='->'), 
                fontsize=10)

    plt.xlabel(r'$U_{CC} [V]$')
    plt.ylabel(r'$I [\mu A]$')
    plt.legend()
    plt.xlim(1,2)
    plt.ylim(bottom=0)
    plt.grid(True)  # Add gridlines
    plt.savefig("3/tex/img/3-1-4.pdf")
    plt.show()

def make_second_plot(filename:str):
    # Read the CSV file, skipping the first two rows
    # and considering the third row as the header
    data = pd.read_csv(filename, delimiter='	')
    data['Id(Mp1)'] *= 1e6
    data['Id(Mp2)'] *= 1e6
    data['Id(Mp3)'] *= 1e6
    data['time'] *= 1e3
    
    x_data = data['time']
    y1_data = data['Id(Mp1)']
    y2_data = data['Id(Mp2)']
    y3_data = data['Id(Mp3)']
    # Plot the data
    plt.plot(x_data, y1_data, label='Id(M1)')
    plt.plot(x_data, y2_data, label='Id(M2)')
    plt.plot(x_data, y3_data, label='Id(Mp3)')


    plt.xlabel(r'$t [ms]$')
    plt.ylabel(r'$I [\mu A]$')
    plt.legend()
    plt.xlim(0,1)
    plt.ylim(bottom=0)
    plt.grid(True)  # Add gridlines
    plt.savefig("3/tex/img/3-1-5.pdf")
    plt.show()

def make_third_plot(filename:str):
    # Read the CSV file, skipping the first two rows
    # and considering the third row as the header
    data = pd.read_csv(filename, delimiter='	')
    data['Id(Mp1)'] *= 1e6
    data['Id(Mp2)'] *= 1e6
    data['Id(Mp3)'] *= 1e6
    data['time'] *= 1e6
    
    x_data = data['time']
    y1_data = data['Id(Mp1)']
    y2_data = data['Id(Mp2)']
    y3_data = data['Id(Mp3)']
    # Plot the data
    plt.plot(x_data, y1_data, label='Id(M1)')
    plt.plot(x_data, y2_data, label='Id(M2)')
    plt.plot(x_data, y3_data, label='Id(Mp3)')

    plt.axvline(x=25, color='r', linestyle='--')

    plt.xlabel(r'$t [\mu s]$')
    plt.ylabel(r'$I [\mu A]$')
    plt.legend()
    plt.xlim(0,50)
    plt.ylim(bottom=0)
    plt.grid(True)  # Add gridlines
    plt.xticks(list(plt.gca().get_xticks())+[25])
    plt.savefig("3/tex/img/3-1-6.pdf")
    plt.show()


def another_plot():
    # Read the CSV file, skipping the first two rows
    # and considering the third row as the header
    data = pd.read_csv('3/tex/data/3-2-3a.txt', delimiter='	')
    x1_data = data['vcc']
    y1_data = data['V(u_out)']
    data = pd.read_csv('3/tex/data/3-2-3b.txt', delimiter='	')
    x2_data = data['vcc']
    y2_data = data['V(u_out)']
    # Plot the data
    plt.plot(x1_data, y1_data, label='V(u_out) - rezistor')
    plt.plot(x2_data, y2_data, label='V(u_out) - proud. zdroj')

    # First difference
    x_values = [0.9*1.8, 1.1*1.8]
    y_values = [y1_data[(x1_data >= x_values[0]).idxmax()], y1_data[(x1_data >= x_values[1]).idxmax()]]
    calc_value=abs(y_values[1]-y_values[0])*1000
    plt.plot(x_values, [y_values[1],y_values[1]], color='b', linestyle=':')
    plt.plot([x_values[0],x_values[0]], y_values, color='b', linestyle=':')
    plt.annotate(r'$\Delta U='+f'{calc_value:.2f} mV'+r'(U_{CC}\pm 10\%)$', 
                xy=(x_values[0],y_values[1]), 
                xytext=(x_values[0]-0.4,y_values[1]), 
                arrowprops=dict(facecolor='black', arrowstyle='->'), 
                fontsize=10)
    
    # First difference
    x_values = [0.9*1.8, 1.1*1.8]
    y_values = [y2_data[(x2_data >= x_values[0]).idxmax()], y2_data[(x2_data >= x_values[1]).idxmax()]]
    calc_value=abs(y_values[1]-y_values[0])*1000
    plt.plot(x_values, [y_values[0],y_values[0]], color='b', linestyle=':')
    plt.plot([x_values[1],x_values[1]], y_values, color='b', linestyle=':')
    plt.annotate(r'$\Delta U='+f'{calc_value:.2f} mV'+r'(U_{CC}\pm 10\%)$', 
                xy=(x_values[1],y_values[0]), 
                xytext=(x_values[1]-0.35,y_values[0]-0.1), 
                arrowprops=dict(facecolor='black', arrowstyle='->'), 
                fontsize=10)

    plt.xlabel(r'$U_{CC} [V]$')
    plt.ylabel(r'$U [V]$')
    plt.legend()
    plt.xlim(1,2)
    # plt.ylim(bottom=0)
    plt.grid(True)  # Add gridlines
    # plt.xticks(list(plt.gca().get_xticks())+[25])
    plt.savefig("3/tex/img/3-2-3.pdf")
    plt.show()


# others funny things
def make_regresion(x_data,y_data):
    # Perform linear regression
    coefficients = np.polyfit(x_data, y_data, 1)
    slope = coefficients[0]
    intercept = coefficients[1]
    reg_data = slope * x_data + intercept
    return reg_data

def make_latex_table(data:pd.DataFrame,filename):
    latex_data=pd.DataFrame({
        "$p_{{ref}} [\\unit{{\\milli\\bar}}]$":data['p_alm'],
        "$p_{{ref}} [\\unit{{\\kilo\\pascal}}]$":data['p_alm_kpa'],
        "$U_{{out}} [\\unit{{\\volt}}]$":data['v_out'],
        "$p_{{out}} [\\unit{{\\kilo\\pascal}}]$":data['mpx_kpa_with_error'],
        "$\\Delta_{{p}} [\\unit{{\\kilo\\pascal}}]$":data['Delta_p'],
        "$\\delta_{{ref}} [\\unit{{\\percent}}]$":data['delta_p'],
    })

    latex_table = latex_data.to_latex(index=False, 
                            float_format="%.3f",
                            decimal=',')
    
    with open(filename,'w') as f:
        f.write(latex_table)

def main():
    make_first_plot('3/tex/data/3-1-4.txt')
    make_second_plot('3/tex/data/3-1-5.txt')
    make_third_plot('3/tex/data/3-1-6.txt')
    another_plot()
    # make_latex_table(data,'4/tex/tables/hodnoty.tex')
   
    # make_third_plot(data)
    


if __name__ == "__main__":
    main()
