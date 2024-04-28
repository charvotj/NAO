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
    file_path = '5/tex/data/aplikace_AC.txt'
    # prepare AC data file
    with open(file_path, 'r',encoding='windows-1252') as file:
        file_content = file.read()

    # Perform the replacement
    file_content = file_content.replace('Freq.	V(u_out)', 'f	Au	phase')
    file_content = file_content.replace(',', '	')
    file_content = file_content.replace('°)', '')
    file_content = file_content.replace('(', '')
    file_content = file_content.replace('dB', '')

    # Write the modified content back to the file
    with open(file_path, 'w',encoding='utf-8') as file:
        file.write(file_content)

    # Read data
    data = pd.read_csv(file_path, delimiter='	')

    # Subtract 180 from values greater than 0
    data.loc[data['phase'] > 0, 'phase'] -= 360
    data['phase'] += 180
    
    x_data = data['f']
    y1_data = data['Au']
    y2_data = data['phase']

    fig, ax1 = plt.subplots()

    ax1.semilogx(x_data, y1_data, label='Id(Mp1)', color='blue')
    ax1.set_xlabel(r'f [Hz]')
    ax1.set_ylabel(r'$A_{U}$ [dB]', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    x = 100
    y = y1_data[(x_data >= x).idxmax()]
    ax1.annotate(r'$A_{U0}$='+f'{y:.2f} dB (f={(x):.2f} Hz)', 
                xy=(x,y), 
                xytext=(x+0.2,y-25), 
                arrowprops=dict(facecolor='black', arrowstyle='->'), 
                fontsize=10)


    y -= 3    # -3dB
    x = x_data[(y1_data <= y).idxmax()-1]
    ax1.axvline(x=x, color='black', linestyle=':')
    ax1.annotate(r'$A_{U}$='+f'{y:.2f} dB '+r'($f_{-3dB}$'+f'={(x/1e3):.2f} kHz)', 
                xy=(x,y), 
                xytext=(1e4,y), 
                arrowprops=dict(facecolor='black', arrowstyle='->'), 
                fontsize=10)
    
    y = 0  # GBW
    x = x_data[(y1_data <= y).idxmax()]
    ax1.axvline(x=x, color='black', linestyle=':')
    ax1.axhline(y=y, color='black', linestyle=':')
    ax1.annotate(f'GBW={(x/1e6):.2f} MHz '+r'($A_{U}$='+f'{y:.2f} dB)', 
                xy=(x,y), 
                xytext=(1e4,6), 
                arrowprops=dict(facecolor='black', arrowstyle='->'), 
                fontsize=10)


    # Create a secondary y-axis for phase plot
    ax2 = ax1.twinx()
    ax2.plot(x_data, y2_data, label='Phase', color='red')
    ax2.set_ylabel(r'Fáze [$^\circ$]', color='red')
    ax2.tick_params(axis='y', labelcolor='red')
    #   # Add ticks on ax2 with specific values
    # existing_ticks = ax2.get_yticks()
    # new_ticks = [-180]  # Adjust the new ticks as needed
    # all_ticks = sorted(list(set(list(existing_ticks) + new_ticks)))
    # ax2.set_yticks(all_ticks)
    ax2.set_ylim(0,180)

    # PM
    index = (y1_data <= 0).idxmax()
    x = x_data[index]
    y = y2_data[index]
    # ax1.axvline(x=x, color='black', linestyle=':')
    # ax1.axhline(y=y, color='black', linestyle=':')
    ax2.annotate(f'PM={y:.2f} '+r'$^\circ$', 
                xy=(x,y), 
                xytext=(1e8,y), 
                arrowprops=dict(facecolor='black', arrowstyle='<-',relpos=(0,0),shrinkA=0,shrinkB=0,patchA=0,patchB=0), 
                fontsize=10)
    
    # PM
    index = (y2_data <= 0).idxmax()
    x = x_data[index]
    y = y1_data[index]
    ax1.axvline(x=x, color='black', linestyle=':')
    ax1.annotate(f'AM={y:.2f} dB', 
                xy=(x,y), 
                xytext=(1e2,y), 
                arrowprops=dict(facecolor='black', arrowstyle='<-',relpos=(0,0),shrinkA=0,shrinkB=0,patchA=0,patchB=0), 
                fontsize=10)
    

    
    # plt.legend()
    plt.xlim(1e2,10e7)
    # plt.ylim(bottom=0)
    plt.grid(True)  # Add gridlines
    plt.tight_layout()
    plt.savefig("5/tex/img/AC.pdf")
    plt.show()

def make_ICMR_plot():
    data = pd.read_csv('5/tex/data/aplikace_ICMR.txt', delimiter='	')
    
    x_data = data['v_in']
    y_data = data['V(u_out)']

    fig, ax1 = plt.subplots()
    
    # Plot the original data
    ax1.plot(x_data, y_data, label='Original Data', zorder=4)
    ax1.set_xlabel(r'$U_{in} [V]$')
    ax1.set_ylabel(r'$U_{out} [V]$')




    # Compute first derivative (gradient)
    dy_dx = np.gradient(y_data,x_data)
    # dy_dx = np.gradient(dy_dx,x_data)

    ax2 = ax1.twinx()
    ax2.plot(x_data, dy_dx, label='First Derivative', linestyle='--', color='red', zorder=2)
    ax2.set_ylabel('První derivace', color='red')
    ax2.tick_params(axis='y', labelcolor='red')
    ax2.set_ylim(bottom=0.9, top = 1.1)

    th = 8e-4
    # th = 0
    center = 1
    zero_indices = np.where((dy_dx >= center-th) & (dy_dx <= center+th) & (x_data > 0.2) & (x_data < 1.75))[0]

    x = x_data[zero_indices[0]]
    y = y_data[zero_indices[0]]
    ax2.axvline(x=x, color='black', linestyle=':')
    ax1.annotate(r'$U_{out}$='+f'{y:.2f} V ', 
        xy=(x,y), 
        xytext=(0.5,y), 
        arrowprops=dict(facecolor='black', arrowstyle='->'), 
        fontsize=10)
    
    x = x_data[zero_indices[-1]]
    y = y_data[zero_indices[-1]]
    ax2.axvline(x=x, color='black', linestyle=':')
    ax1.annotate(r'$U_{out}$='+f'{y:.2f} V ', 
        xy=(x,y), 
        xytext=(0.6,y), 
        arrowprops=dict(facecolor='black', arrowstyle='->'), 
        fontsize=10)


    # plt.xlim(0,1)
    # plt.ylim(bottom=-0.2,top=2)
    plt.grid(True)  # Add gridlines
    plt.tight_layout()
    plt.savefig("5/tex/img/ICMR.pdf")
    plt.show()

def make_OVS_plot():
    data = pd.read_csv('5/tex/data/aplikace_OVS.txt', delimiter='	')
    
    x_data = data['v_in']
    y_data = data['V(u_out)']

    fig, ax1 = plt.subplots()
    
    # Plot the original data
    ax1.plot(x_data, y_data, label='Original Data', zorder=4)
    ax1.set_xlabel(r'$U_{in} [V]$')
    ax1.set_ylabel(r'$U_{out} [V]$')




    # Compute first derivative (gradient)
    dy_dx = np.gradient(y_data,x_data)
    dy_dx = np.gradient(dy_dx,x_data)

    ax2 = ax1.twinx()
    ax2.plot(x_data, dy_dx, label='Second Derivative', linestyle='--', color='red', zorder=2)
    ax2.set_ylabel('Druhá derivace', color='red')
    ax2.tick_params(axis='y', labelcolor='red')
    ax2.set_ylim(bottom=-10, top = 10)

    th = 0.6
    zero_indices = np.where((dy_dx >= -th) & (dy_dx <= th) & (x_data > 0.8) & (x_data < 1))[0]

    x = x_data[zero_indices[0]]
    y = y_data[zero_indices[0]]
    ax2.axvline(x=x, color='black', linestyle=':')
    ax1.annotate(r'$U_{out}$='+f'{y:.2f} V ', 
        xy=(x,y), 
        xytext=(0.5,1.6), 
        arrowprops=dict(facecolor='black', arrowstyle='->'), 
        fontsize=10)
    
    x = x_data[zero_indices[-1]]
    y = y_data[zero_indices[-1]]
    ax2.axvline(x=x, color='black', linestyle=':')
    ax1.annotate(r'$U_{out}$='+f'{y:.2f} V ', 
        xy=(x,y), 
        xytext=(1.1,y), 
        arrowprops=dict(facecolor='black', arrowstyle='->'), 
        fontsize=10)


    # plt.xlim(0,1)
    # plt.ylim(bottom=-0.2,top=2)
    plt.grid(True)  # Add gridlines
    plt.tight_layout()
    plt.savefig("5/tex/img/OVS.pdf")
    plt.show()

def make_TRAN_plot():
    # Read the CSV file, skipping the first two rows
    # and considering the third row as the header
    data = pd.read_csv('5/tex/data/aplikace_TRAN.txt', delimiter='	')
    data['time'] *= 1e6

    # data = data.iloc[10:]
    
    x_data = data['time']
    y1_data = data['V(u_in)']
    y2_data = data['V(u_out)']
    # Plot the data
    plt.plot(x_data, y1_data, label='V(u_in)')
    plt.plot(x_data, y2_data, label='V(u_out)')

    # SR rise
    # y_values = [0.1*1.8, 0.9*1.8]
    # x_values = [x_data[(x_data > 6 and y2_data >= y_values[0]).idxmax()], x_data[(x_data > 6 and y2_data >= y_values[1]).idxmax()]]
    y_values = [0.1*1.8, 0.9*1.55]
    x_values = [x_data[(y2_data >= y_values[0]).idxmax()], x_data[(y2_data >= y_values[1]).idxmax()]]
    calc_value=abs(y_values[1]-y_values[0])/abs(x_values[1]-x_values[0])
    plt.annotate(r'$SR_{rise}='+f'{calc_value:.2f} '+r'V/\mu s $', 
                xy=(x_values[1],y_values[1]), 
                xytext=(x_values[1]+0.2,y_values[1]-0.2), 
                arrowprops=dict(facecolor='black', arrowstyle='->'), 
                fontsize=10)

    # SR fall
    y_values = [0.1*1.8, 0.9*1.55]
    plt.axhline(y_values[0],color='black', linestyle=':')
    plt.axhline(y_values[1],color='black', linestyle=':')
    x_values = [x_data[((x_data > 6) & (y2_data <= y_values[0])).idxmax()], x_data[((x_data > 6) & (y2_data <= y_values[1])).idxmax()]]
    calc_value=abs(y_values[1]-y_values[0])/abs(x_values[1]-x_values[0])
    plt.annotate(r'$SR_{fall}='+f'{calc_value:.2f} '+r'V/\mu s $', 
                xy=(x_values[0],y_values[0]), 
                xytext=(x_values[0]-3,y_values[0]+0.2), 
                arrowprops=dict(facecolor='black', arrowstyle='->'), 
                fontsize=10)





    plt.xlabel(r'$t [\mu s]$')
    plt.ylabel(r'$U [V]$')
    plt.legend()
    plt.xlim(0,10)
    # plt.ylim(bottom=0)
    plt.grid(True)  # Add gridlines
    plt.savefig("5/tex/img/TRAN.pdf")
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
    make_OVS_plot()
    make_ICMR_plot()
    make_TRAN_plot()
    


if __name__ == "__main__":
    main()
