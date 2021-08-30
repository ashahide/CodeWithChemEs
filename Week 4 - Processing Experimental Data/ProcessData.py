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

    from sklearn.metrics import mean_squared_error, r2_score

    RMSE = round(mean_squared_error(y_Data, y_Estimated, squared=False), 2)
    r2   = round(r2_score(y_Data, y_Estimated), 2)

    import matplotlib.pyplot as plt 
    plt.style.use('seaborn-darkgrid')

    plt.plot(x_Data, y_Data, 'kx', label = 'Data')
    plt.plot(x_Data, y_Estimated, 'r', label = f'P = cRT (c = {round(parameters[0], 2)}' +  r' $\frac{mol}{L}$,' +  f' RMSE = {RMSE}, $R^{2}$ = {r2})')

    plt.xlabel(Data.columns[0])
    plt.ylabel(Data.columns[1])

    plt.legend()

    plt.show()




    return


def EquationFunction(T, C):
    return C*8.314*T

ProcessExperimentalData(EquationFunction)