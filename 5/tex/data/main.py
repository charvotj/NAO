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

def make_AC_plot():
    data = pd.read_csv('5/tex/data/aplikace_AC.txt', delimiter='	')
    
    x_data = data['f']
    y1_data = data['Au']
    y2_data = data['phase']

    fig, ax1 = plt.subplots()

    ax1.semilogx(x_data, y1_data, label='Id(Mp1)', color='blue')
    ax1.set_xlabel(r'f [Hz]')
    ax1.set_ylabel(r'$A_{U}$ [dB]', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    x = 1000
    y = y1_data[(x_data >= x).idxmax()]
    ax1.annotate(r'$A_{U0}$='+f'{y:.2f} dB (f={(x/1000):.2f} kHz)', 
                xy=(x,y), 
                xytext=(x+0.2,y-25), 
                arrowprops=dict(facecolor='black', arrowstyle='->'), 
                fontsize=10)


    y -= 3    # -3dB
    x = x_data[(y1_data <= y).idxmax()-1]
    ax1.annotate(r'$A_{U}$='+f'{y:.2f} dB '+r'($f_{-3dB}$'+f'={(x/1e6):.2f} MHz)', 
                xy=(x,y), 
                xytext=(x+4e4,y), 
                arrowprops=dict(facecolor='black', arrowstyle='->'), 
                fontsize=10)
    
    y = 0  # GBW
    x = x_data[(y1_data <= y).idxmax()]
    ax1.annotate(f'GBW={(x/1e6):.2f} MHz '+r'($A_{U}$='+f'{y:.2f} dB)', 
                xy=(x,y), 
                xytext=(1e4,y), 
                arrowprops=dict(facecolor='black', arrowstyle='->'), 
                fontsize=10)


    # Create a secondary y-axis for phase plot
    ax2 = ax1.twinx()
    ax2.plot(x_data, y2_data, label='Phase', color='red')
    ax2.set_ylabel(r'Fáze [$^\circ$]', color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    
    # plt.legend()
    plt.xlim(1e3,1e7)
    # plt.ylim(bottom=0)
    plt.grid(True)  # Add gridlines
    plt.savefig("5/tex/img/AC.pdf")
    plt.show()

def make_second_plot(filename:str):
    # Read the CSV file, skipping the first two rows
    # and considering the third row as the header
    data = pd.read_csv(filename, delimiter='	')
    data['time'] *= 1e6

    # data = data.iloc[10:]
    
    x_data = data['time']
    y1_data = data['V(u_in)']
    y2_data = data['V(u_out)']
    # Plot the data
    plt.plot(x_data, y1_data, label='V(u_in)')
    plt.plot(x_data, y2_data, label='V(u_out)')

    # SR fall
    y_values = [0.1*1.8, 0.9*1.8]
    plt.axhline(y_values[0],color='black', linestyle=':')
    plt.axhline(y_values[1],color='black', linestyle=':')
    x_values = [x_data[(y2_data <= y_values[0]).idxmax()], x_data[(y2_data <= y_values[1]).idxmax()]]
    calc_value=abs(y_values[1]-y_values[0])/abs(x_values[1]-x_values[0])
    plt.annotate(r'$SR_{fall}='+f'{calc_value:.2f} '+r'V/\mu s $', 
                xy=(x_values[0],y_values[0]), 
                xytext=(x_values[0]-3,y_values[0]+0.2), 
                arrowprops=dict(facecolor='black', arrowstyle='->'), 
                fontsize=10)



    # SR rise
    # y_values = [0.1*1.8, 0.9*1.8]
    # x_values = [x_data[(x_data > 6 and y2_data >= y_values[0]).idxmax()], x_data[(x_data > 6 and y2_data >= y_values[1]).idxmax()]]
    y_values = [0.1*1.8, 0.9*1.8]
    x_values = [x_data[((x_data > 6) & (y2_data >= y_values[0])).idxmax()], x_data[((x_data > 6) & (y2_data >= y_values[1])).idxmax()]]
    calc_value=abs(y_values[1]-y_values[0])/abs(x_values[1]-x_values[0])
    plt.annotate(r'$SR_{rise}='+f'{calc_value:.2f} '+r'V/\mu s $', 
                xy=(x_values[1],y_values[1]), 
                xytext=(x_values[1]+0.2,y_values[1]-0.2), 
                arrowprops=dict(facecolor='black', arrowstyle='->'), 
                fontsize=10)


    plt.xlabel(r'$t [\mu s]$')
    plt.ylabel(r'$U [V]$')
    plt.legend()
    # plt.xlim(0,1)
    # plt.ylim(bottom=0)
    plt.grid(True)  # Add gridlines
    plt.savefig("4/tex/img/4-1-3.pdf")
    plt.show()

def make_third_plot(filename:str):
    data = pd.read_csv(filename, delimiter='	')
    
    x_data = data['f']
    y1_data = data['Au']
    y2_data = data['phase']

    plt.semilogx(x_data, y1_data, label='Id(Mp1)')

    x = 1000
    y = y1_data[(x_data >= x).idxmax()]
    plt.annotate(r'$A_{U0}$='+f'{y:.2f} dB (f={(x/1000):.2f} kHz)', 
                xy=(x,y), 
                xytext=(x+0.2,y-5), 
                arrowprops=dict(facecolor='black', arrowstyle='->'), 
                fontsize=10)


    y -= 3    # -3dB
    x = x_data[(y1_data <= y).idxmax()-1]
    plt.annotate(r'$A_{U}$='+f'{y:.2f} dB '+r'($f_{-3dB}$'+f'={(x/1e3):.2f} kHz)', 
                xy=(x,y), 
                xytext=(x-18.7e4,y-9), 
                arrowprops=dict(facecolor='black', arrowstyle='->'), 
                fontsize=10)
    
    y = 0  # GBW
    x = x_data[(y1_data <= y).idxmax()]
    plt.annotate(f'GBW={(x/1e6):.2f} MHz '+r'($A_{U}$='+f'{y:.2f} dB)', 
                xy=(x,y), 
                xytext=(x-16.4e6,y-8), 
                arrowprops=dict(facecolor='black', arrowstyle='->'), 
                fontsize=10)



    plt.xlabel(r'f [Hz]')
    plt.ylabel(r'$A_{U}$ [dB]')
    # plt.legend()
    
    # plt.xlim(1,2)
    # plt.ylim(bottom=0)
    plt.grid(True)  # Add gridlines
    plt.savefig("4/tex/img/4-2-2.pdf")
    plt.show()


def another_plot(filename:str):
    # Read the CSV file, skipping the first two rows
    # and considering the third row as the header
    data = pd.read_csv(filename, delimiter='	')
    data['time'] *= 1e6

    # data = data.iloc[10:]
    
    x_data = data['time']
    y1_data = data['V(u_in)']
    y2_data = data['V(u_out)']
    # Plot the data
    plt.plot(x_data, y1_data, label='V(u_in)')
    plt.plot(x_data, y2_data, label='V(u_out)')

    # SR fall
    y_values = [0.1*1.8, 0.9*1.8]
    plt.axhline(y_values[0],color='black', linestyle=':')
    plt.axhline(y_values[1],color='black', linestyle=':')
    x_values = [x_data[(y2_data <= y_values[0]).idxmax()], x_data[(y2_data <= y_values[1]).idxmax()]]
    calc_value=abs(y_values[1]-y_values[0])/abs(x_values[1]-x_values[0])
    plt.annotate(r'$SR_{fall}='+f'{calc_value:.2f} '+r'V/\mu s $', 
                xy=(x_values[0],y_values[0]), 
                xytext=(x_values[0]-3,y_values[0]+0.2), 
                arrowprops=dict(facecolor='black', arrowstyle='->'), 
                fontsize=10)



    # SR rise
    # y_values = [0.1*1.8, 0.9*1.8]
    # x_values = [x_data[(x_data > 6 and y2_data >= y_values[0]).idxmax()], x_data[(x_data > 6 and y2_data >= y_values[1]).idxmax()]]
    y_values = [0.1*1.8, 0.9*1.8]
    x_values = [x_data[((x_data > 6) & (y2_data >= y_values[0])).idxmax()], x_data[((x_data > 6) & (y2_data >= y_values[1])).idxmax()]]
    calc_value=abs(y_values[1]-y_values[0])/abs(x_values[1]-x_values[0])
    plt.annotate(r'$SR_{rise}='+f'{calc_value:.2f} '+r'V/\mu s $', 
                xy=(x_values[1],y_values[1]), 
                xytext=(x_values[1]+0.2,y_values[1]-0.2), 
                arrowprops=dict(facecolor='black', arrowstyle='->'), 
                fontsize=10)


    plt.xlabel(r'$t [\mu s]$')
    plt.ylabel(r'$U [V]$')
    plt.legend()
    # plt.xlim(0,1)
    # plt.ylim(bottom=0)
    plt.grid(True)  # Add gridlines
    plt.savefig("4/tex/img/4-2-3.pdf")
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
    make_AC_plot()
    # make_first_plot('4/tex/data/4-1-2ac.txt')
    # make_second_plot('4/tex/data/4-1-3tran.txt')
    # make_third_plot('4/tex/data/4-2-2ac.txt')
    # another_plot('4/tex/data/4-2-3tran.txt')
    # make_latex_table(data,'4/tex/tables/hodnoty.tex')
   
    # make_third_plot(data)
    


if __name__ == "__main__":
    main()
