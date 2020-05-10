from random import randint 
from itertools import count 
import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation 

file_dir = '/Users/emiliano/codebase/python/gui_apps/files/'
file_nm  = file_dir+'data.csv'
plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()

def animate(i):
    data = pd.read_csv(file_nm,engine='python')
    x = data['x_val']
    y1= data['total_1']
    y2= data['total_2']

  
    plt.cla()

    plt.plot(x,y1, label='Channel 1')
    plt.plot(x,y2, label='Channel 2')

    plt.legend(loc='upper left')
    plt.tight_layout()

    

ani = FuncAnimation(plt.gcf(),animate,interval=1000)


plt.tight_layout()
plt.show()



