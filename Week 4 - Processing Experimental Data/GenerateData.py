import numpy as np 

T = np.linspace(290, 375, 100) + np.random.randint(-25, 25, 100)

P = (0.5*8.314*T + np.random.randint(-25, 25, 100)) / 1000


import matplotlib.pyplot as plt 
import pandas as pd 

import os

Data = pd.DataFrame({'Temperature (K)': T, 'Pressure (kPa)': P})

Data.to_csv(os.getcwd() + '\Experimental Data.csv', index = False)

plt.subplot(2,1,1)
plt.plot(P, label = 'P')

plt.xlabel('Time')
plt.ylabel('Pressure (kPa)')

plt.subplot(2,1,2)
plt.plot(T, label = 'T')

plt.xlabel('Time')
plt.ylabel('Temperature (K)')

plt.show()