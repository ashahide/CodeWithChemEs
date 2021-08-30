def solve_balance_equations(equation_function, initial_conditions, 
                            t = None, 
                            state_labels = None,
                            x_label = None,
                            y_label = None,
                            title = None,
                            fontsize = None,
                            linewidth = None):

    from scipy.integrate import odeint
    import numpy as np 

    solutions = odeint(equation_function, initial_conditions, t)

    """
    Plots
    """

    if state_labels is None:
        state_labels = [f'State {i}' for i in np.arange(1, len(initial_conditions) + 1)]

    if fontsize is None:
        fontsize = 15

    if linewidth is None:
        linewidth = 3

    import matplotlib.pyplot as plt 
    plt.style.use('seaborn-darkgrid')
    plt.figure(figsize = (14,8))

    for i in range(len(initial_conditions)):
        plt.plot(t, solutions[:,i], linewidth = linewidth, label = f"{state_labels[i]}")

    if x_label is None:
        plt.xlabel('Time', fontsize = fontsize)
    else:
        plt.xlabel(x_label, fontsize = fontsize)

    if y_label is None:
        plt.ylabel('Output', fontsize = fontsize)
    else:
        plt.ylabel(y_label, fontsize = fontsize)

    if title is not None:
        plt.title(title, fontsize = fontsize)

    plt.xticks(fontsize = fontsize)
    plt.yticks(fontsize = fontsize)
    plt.legend(fontsize = fontsize)

    import os 
    plt.savefig(f"{os.getcwd()}" + f"\Simulation")

    plt.show()


    return solutions

def batch_equations(x,t):
    dx1dt = -x[0]

    dx2dt = x[0]


    return dx1dt, dx2dt

import numpy as np
solutions = solve_balance_equations(batch_equations, [10, 0], t = np.linspace(1, 10, 100), 
                                    x_label = 'Time',
                                    y_label= 'Concentration', 
                                    title= r'Batch Reactor $A \rightarrow B$', 
                                    state_labels=[r'$C_{A}$', r'$C_{B}$'])