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
    data['Id(M1)'] *= 1e6
    data['Id(M2)'] *= 1e6

    # Display the data
    print(data)
    
    x_data = data['vout']
    y1_data = data['Id(M1)']
    y2_data = data['Id(M2)']
    # Plot the data
    plt.plot(x_data, y1_data, label='Id(M1)')
    plt.plot(x_data, y2_data, label='Id(M2)')
     # Add vertical dashed line at x=0.2
    plt.axvline(x=0.2, color='r', linestyle='--')
    # Find the index where y2_data equals 50
    idx = (y2_data >= 50).idxmax()
    # Plot a single point with label
    plt.plot(x_data[idx], y2_data[idx], 'rx')  # Plot the point
    plt.annotate('({}, {})'.format("%.02f" % x_data[idx], "%.02f" % y2_data[idx]), 
                 xy=(x_data[idx], y2_data[idx]), 
                 xytext=(x_data[idx]-0.1, y2_data[idx]+2),
                #  arrowprops=dict(facecolor='black', arrowstyle='->'), 
                 fontsize=10)
    
 # First difference
    x_values = [0.2, 1.8]
    y_values = [y2_data[(x_data >= x_values[0]).idxmax()], y2_data[len(x_data)-1]]
    r_out=abs(x_values[1]-x_values[0])/abs(y_values[1]-y_values[0])
    plt.plot(x_values, [y_values[0],y_values[0]], color='b', linestyle=':')
    plt.plot([x_values[1],x_values[1]], y_values, color='b', linestyle=':')
    plt.annotate(r'$\left|\frac{\Delta U}{\Delta I}\right|='+f'{r_out:.2f} M\Omega$', 
                xy=(x_values[1],y_values[0]), 
                xytext=(x_values[1]-0.3,y_values[0]-10), 
                arrowprops=dict(facecolor='black', arrowstyle='->'), 
                fontsize=10)
# Second difference
    x_values = [0.5, 1.3]
    y_values = [y2_data[(x_data >= x_values[0]).idxmax()], y2_data[(x_data >= x_values[1]).idxmax()]]
    r_out=abs(x_values[1]-x_values[0])/abs(y_values[1]-y_values[0])
    plt.plot(x_values, [y_values[0],y_values[0]], color='g', linestyle=':')
    plt.plot([x_values[1],x_values[1]], y_values, color='g', linestyle=':')
    plt.annotate(r'$\left|\frac{\Delta U}{\Delta I}\right|='+f'{r_out:.2f} M\Omega$', 
            xy=(x_values[1],y_values[0]), 
            xytext=(x_values[1]-0.5,y_values[0]-10), 
            arrowprops=dict(facecolor='black', arrowstyle='->'), 
            fontsize=10)

    plt.xlabel(r'$U_{out} [V]$')
    plt.ylabel(r'$I [\mu A]$')
    plt.legend()
    plt.xlim(0,1.9)
    plt.ylim(bottom=0)
    # Add a single y-axis tick at value 7
    plt.yticks(list(plt.gca().get_yticks())+[25,50])
    plt.grid(True)  # Add gridlines
    plt.savefig("2/tex/img/2-1.pdf")
    plt.show()

def make_second_plot(filename:str):
    # Read the CSV file, skipping the first two rows
    # and considering the third row as the header
    data = pd.read_csv(filename, delimiter='	')
    data['Id(M3)'] *= 1e6
    data['Id(M4)'] *= 1e6

    # Display the data
    print(data)
    
    x_data = data['vout2']
    y1_data = data['Id(M3)']
    y2_data = data['Id(M4)']
    # Plot the data
    plt.plot(x_data, y1_data, label='Id(M1)')
    plt.plot(x_data, y2_data, label='Id(M2)')
     # Add vertical dashed line at x=0.2
    plt.axvline(x=1.55, color='r', linestyle='--')
    # Find the index where y2_data equals 50
    idx = (y2_data <= 100).idxmax()
    # Plot a single point with label
    plt.plot(x_data[idx], y2_data[idx], 'rx')  # Plot the point
    plt.annotate('({}, {})'.format("%.02f" % x_data[idx], "%.02f" % y2_data[idx]), 
                 xy=(x_data[idx], y2_data[idx]), 
                 xytext=(x_data[idx]-0.1, y2_data[idx]+8),
                #  arrowprops=dict(facecolor='black', arrowstyle='->'), 
                 fontsize=10)
    
 # First difference
    x_values = [0.0, 1.55]
    y_values = [y2_data[(x_data >= x_values[0]).idxmax()], y2_data[(x_data >= x_values[1]).idxmax()]]
    r_out=abs(x_values[1]-x_values[0])/abs(y_values[1]-y_values[0])
    plt.plot(x_values, [y_values[1],y_values[1]], color='b', linestyle=':')
    plt.plot([x_values[0],x_values[0]], y_values, color='b', linestyle=':')
    plt.annotate(r'$\left|\frac{\Delta U}{\Delta I}\right|='+f'{r_out:.2f} M\Omega$', 
                xy=(x_values[0],y_values[1]), 
                xytext=(x_values[0]+0.05,y_values[1]-25), 
                arrowprops=dict(facecolor='black', arrowstyle='->'), 
                fontsize=10)
# Second difference
    x_values = [0.2, 0.7]
    y_values = [y2_data[(x_data >= x_values[0]).idxmax()], y2_data[(x_data >= x_values[1]).idxmax()]]
    r_out=abs(x_values[1]-x_values[0])/abs(y_values[1]-y_values[0])
    plt.plot(x_values, [y_values[1],y_values[1]], color='g', linestyle=':')
    plt.plot([x_values[0],x_values[0]], y_values, color='g', linestyle=':')
    plt.annotate(r'$\left|\frac{\Delta U}{\Delta I}\right|='+f'{r_out:.2f} M\Omega$', 
            xy=(x_values[0],y_values[1]), 
            xytext=(x_values[0]+0.05,y_values[1]-15), 
            arrowprops=dict(facecolor='black', arrowstyle='->'), 
            fontsize=10)

    plt.xlabel(r'$U_{out} [V]$')
    plt.ylabel(r'$I [\mu A]$')
    plt.legend()
    plt.xlim(-0.1,1.8)
    plt.ylim(bottom=0)
    plt.yticks(list(plt.gca().get_yticks())+[50,100])
    plt.grid(True)  # Add gridlines
    plt.savefig("2/tex/img/2-2.pdf")
    plt.show()

def make_third_plot(filename:str):
    # Read the CSV file, skipping the first two rows
    # and considering the third row as the header
    data = pd.read_csv(filename, delimiter='	')
    data['Id(M7)'] *= 1e6
    data['Id(M8)'] *= 1e6

    # Display the data
    print(data)
    
    x_data = data['vout3']
    y1_data = data['Id(M7)']
    y2_data = data['Id(M8)']
    # Plot the data
    plt.plot(x_data, y1_data, label='Id(M7)')
    plt.plot(x_data, y2_data, label='Id(M8)')
     # Add vertical dashed line at x=0.2
    plt.axvline(x=0.8, color='r', linestyle='--')
    # Find the index where y2_data equals 50
    # idx = (y2_data >= 100).idxmax()
    # # Plot a single point with label
    # plt.plot(x_data[idx], y2_data[idx], 'rx')  # Plot the point
    # plt.annotate('({}, {})'.format("%.02f" % x_data[idx], "%.02f" % y2_data[idx]), 
    #              xy=(x_data[idx], y2_data[idx]), 
    #              xytext=(x_data[idx]-0.1, y2_data[idx]+2),
    #             #  arrowprops=dict(facecolor='black', arrowstyle='->'), 
    #              fontsize=10)
    
 # First difference
    x_values = [0.8, 1.8]
    y_values = [y2_data[(x_data >= x_values[0]).idxmax()], y2_data[len(x_data)-1]]
    r_out=abs(x_values[1]-x_values[0])/abs(y_values[1]-y_values[0])
    plt.plot(x_values, [y_values[0],y_values[0]], color='b', linestyle=':')
    plt.plot([x_values[1],x_values[1]], y_values, color='b', linestyle=':')
    plt.annotate(r'$\left|\frac{\Delta U}{\Delta I}\right|='+f'{r_out:.2f} M\Omega$', 
                xy=(x_values[1],y_values[0]), 
                xytext=(x_values[1]-0.3,y_values[0]-10), 
                arrowprops=dict(facecolor='black', arrowstyle='->'), 
                fontsize=10)
# Second difference
    x_values = [1.2, 1.5]
    y_values = [y2_data[(x_data >= x_values[0]).idxmax()], y2_data[(x_data >= x_values[1]).idxmax()]]
    r_out=abs(x_values[1]-x_values[0])/abs(y_values[1]-y_values[0])
    plt.plot(x_values, [y_values[0],y_values[0]], color='g', linestyle=':')
    plt.plot([x_values[1],x_values[1]], y_values, color='g', linestyle=':')
    plt.annotate(r'$\left|\frac{\Delta U}{\Delta I}\right|='+f'{r_out:.2f} M\Omega$', 
            xy=(x_values[1],y_values[0]), 
            xytext=(x_values[1]-0.5,y_values[0]-10), 
            arrowprops=dict(facecolor='black', arrowstyle='->'), 
            fontsize=10)

    plt.xlabel(r'$U_{out} [V]$')
    plt.ylabel(r'$I [\mu A]$')
    plt.legend()
    plt.xlim(0,1.9)
    plt.ylim(bottom=0)
    plt.yticks(list(plt.gca().get_yticks())+[50,100])
    plt.grid(True)  # Add gridlines
    plt.savefig("2/tex/img/2-3.pdf")
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
    make_first_plot('2/tex/data/2-1.txt')
    make_second_plot('2/tex/data/2-2.txt')
    make_third_plot('2/tex/data/2-3.txt')
    # make_latex_table(data,'4/tex/tables/hodnoty.tex')
   
    # make_third_plot(data)
    


if __name__ == "__main__":
    main()
