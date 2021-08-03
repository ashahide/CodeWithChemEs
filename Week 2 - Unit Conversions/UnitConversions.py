def convert_temperature(T, T_Unit):
    if type(T) not in [int, float]:
        raise TypeError(f'T must be an integer or a float and NOT a {type(T)}')
    if type(T_Unit) not in [str]:
        raise TypeError(f'T_Unit must be a string and NOT a {type(T_Unit)}')

    if T_Unit == 'K':
        T_Kelvin     = round(T, 3) 
        T_Celsius    = round(T_Kelvin - 273, 3) 
        T_Fahrenheit = round((9/5)*(T_Kelvin - 273.15) + 32, 3)

    elif T_Unit == 'C':
        T_Celsius    = round(T, 3) 
        T_Kelvin     = round(T_Celsius + 273.15, 3) 
        T_Fahrenheit = round((9/5)*(T_Kelvin - 273.15) + 32, 3)

    elif T_Unit == 'F':
        T_Fahrenheit = round(T, 3)
        T_Celsius    = round((T_Fahrenheit - 32)/1.8, 3) 
        T_Kelvin     = round(T_Celsius + 273.15, 3) 

    print('\nTemperature Conversion')
    print(f'F: {T_Fahrenheit}')
    print(f'C: {T_Celsius}')
    print(f'K: {T_Kelvin}')

    return T_Kelvin, T_Celsius, T_Fahrenheit

def convert_pressure(P, P_Unit):
    if type(P) not in [int, float]:
        raise TypeError(f'P must be an integer or a float and NOT a {type(P)}')
    if type(P_Unit) not in [str]:
        raise TypeError(f'P_Unit must be a string and NOT a {type(P_Unit)}')

    if P_Unit == 'Pa':
        P_Pa     = round(P, 3) 
        P_bar    = P_Pa*1e-5
        P_atm    = P_Pa*9.867e-6

    elif P_Unit == 'bar':
        P_bar    = round(P, 3) 
        P_Pa     = P_bar*1e-5
        P_atm    = P_Pa*9.867e-2

    elif P_Unit == 'atm':
        P_atm = round(P, 3)
        P_bar = P_atm*1.01325
        P_Pa  = P_atm*101325

    print('\nPressure Conversion')
    print(f'Pa: {P_Pa}')
    print(f'bar: {P_bar}')
    print(f'atm: {P_atm}')

    return P_Pa, P_bar, P_atm

convert_temperature(273.15, 'K')
convert_pressure(1, 'bar')





