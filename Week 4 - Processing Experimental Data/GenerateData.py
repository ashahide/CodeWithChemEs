import numpy as np 

T = np.linspace(290, 375, 100) + np.random.randint(-50, 50, 100)

P = 0.5*8.314*T + np.random.randint(-50, 50, 100)


import matplotlib.pyplot as plt 
import pandas as pd 

import os

Data = pd.DataFrame({'Temperature (K)': T, 'Pressure (Pa)': P})

Data.to_csv(os.getcwd() + '\Experimental Data.csv', index = False)

plt.subplot(2,1,1)
plt.plot(P, label = 'P')

plt.subplot(2,1,2)
plt.plot(T, label = 'T')

plt.show()