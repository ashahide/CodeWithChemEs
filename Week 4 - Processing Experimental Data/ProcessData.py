def ProcessExperimentalData(EquationFunction):
    import os, pandas

    CurrentWorkingDirectory = os.getcwd()
    FilesInDirectory        = os.listdir() 

    for File in FilesInDirectory:
        FileName, FileExtension = os.path.splitext(File)
        if FileExtension == '.csv':
            Data = pandas.read_csv(os.getcwd() + f'\{File}')

            x_Data = Data.iloc[:,0]
            y_Data = Data.iloc[:,1]

    import scipy.optimize

    parameters, parameter_covariance = scipy.optimize.curve_fit(
                                    EquationFunction, 
                                    xdata= x_Data, 
                                    ydata= y_Data,
                                    bounds = (0, 10)
                                    )

    y_Estimated = EquationFunction(x_Data, *parameters)

    import numpy as np 

    RMSE = round(np.sqrt(sum([(y_Data[i] - y_Estimated[i])**2 for i in range(len(y_Data))]) / len(y_Data)), 3)

    import matplotlib.pyplot as plt 

    plt.style.use('seaborn-darkgrid')

    plt.plot(x_Data, y_Data, 'kx', label = 'Data')
    plt.plot(x_Data, y_Estimated, 'r', label = f'Fit (C = {round(parameters[0], 2)}, RMSE = {RMSE})')

    plt.xlabel(Data.columns[0])
    plt.ylabel(Data.columns[1])

    plt.legend()

    plt.show()




    return


def EquationFunction(T, C):
    return C*8.314*T

ProcessExperimentalData(EquationFunction)