def ideal_gas_law(R, P = None, V = None, N = None, T = None):
    """
    Function to solve the ideal gas equation for each variable. 

    Inputs:
        - R MUST be input to the function as an integer or float 
        - Three out of P, V, N, and T must be defined to solve for the fourth value 

    Outputs:
        - P, V, N, R, T
    
    """
    
    if type(R) not in [int, float]:
        raise TypeError(f"R must be an integer or a float not {type(R)}")

    Variables_with_none_values = []
    for idx, val in enumerate([P, V, N, T]):
        if val is None:
            Variables_with_none_values.append(['P', 'V', 'N', 'T'][idx])

    if len(Variables_with_none_values) > 1:
        raise TypeError(f'Too many variables undefined. Make sure 3 variables are input to the function. Undefined: {Variables_with_none_values}')

    print('\n>>> Ideal Gas Law Calculations')
    if   P is None:
        Variables = ['V', 'N', 'T']
        for index, variable_values in enumerate([V, N, T]):
            if type(variable_values) not in [int, float]:
                raise TypeError(f"{Variables[index]} must be an integer or a float not {type(variable_values)}")

        print('...Solving for Pressure...')
        P = round(N*R*T/V, 3)

    elif V is None:
        Variables = ['P', 'N', 'T']
        for index, variable_values in enumerate([P, N, T]):
            if type(variable_values) not in [int, float]:
                raise TypeError(f"{Variables[index]} must be an integer or a float not {type(variable_values)}")

        print('...Solving for Volume...')
        V = round(N*R*T/P, 3)

    elif N is None: 
        Variables = ['P', 'V', 'T']
        for index, variable_values in enumerate([P, V, T]):
            if type(variable_values) not in [int, float]:
                raise TypeError(f"{Variables[index]} must be an integer or a float not {type(variable_values)}")

        print('...Solving for Moles...')
        N = round(P*V/(R*T), 3)

    elif T is None:
        Variables = ['P', 'V', 'N']
        for index, variable_values in enumerate([P, V, N]):
            if type(variable_values) not in [int, float]:
                raise TypeError(f"{Variables[index]} must be an integer or a float not {type(variable_values)}")

        print('...Solving for Temperature...')
        T = round((P*V) / (N*R), 3)

    print(f'P = {P}')
    print(f'V = {V}')
    print(f'N = {N}')
    print(f'R = {R}')
    print(f'T = {T}')


    return P, V, N, R, T

ideal_gas_law(R = 8.314, V = 1, T = 1)