def calc_heat(m,C,T1,T2):
    print("\n>>> Calculating Heat")
    if type(T2) == list and len(T2) > 1:
        Q  = [m*C*(T2[i] - T1) for i in range(len(T2))]

        import matplotlib.pyplot as plt 

        plt.style.use('seaborn-darkgrid')

        plt.figure() 

        plt.title('Steady-State Heat for Different Temperature Gradients')

        plt.plot(T2, Q, color = 'r', label = 'Heat')
        plt.hlines(0, T2[0], T2[-1], color = 'k', linestyle = 'dashed', label = 'Thermal Equilibrium')
        
        plt.xlabel('Temperature 2')

        plt.ylabel('Q')

        plt.legend()

        plt.show()

    else:

        Q = round(m*C*(T2 - T1),3)

    print(f'Q = {Q}')

    return Q

import numpy as np 
calc_heat(1, 1, 3, 2)