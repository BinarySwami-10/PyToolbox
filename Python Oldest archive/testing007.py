# from numpy import random as rnd
# import multiprocessing;import time
# import numpy as np
	
# 	# t1=multiprocessing.Process(target=arand)
# 	# t2=multiprocessing.Process(target=arand)

# # importing matplotlib module  
# from matplotlib import pyplot as plt 
# x = []
# y = [] 
# def plotter(z):
# 	fig = plt.figure()
# 	for j in range(z):
# 		for i in range(100):
# 			t=np.random.randint(100)
# 			x.append(t)
# 			# print(t)
# 			t=np.random.randint(100)
# 			y.append(t)
# 		plt.plot(y,x) 
# 		fig.canvas.draw()
# 		fig.canvas.flush_events()
# 		time.sleep(1)
# 	# Function to plot 
	  
# 	# function to show the plot 
# plotter(3)
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 6*np.pi, 1000)
y = np.sin(x)

# You probably won't need this if you're embedding things in a tkinter plot...
plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x, y, 'r-') # Returns a tuple of line objects, thus the comma

for phase in np.linspace(0, 10*np.pi, 500):
    line1.set_ydata(np.sin(x + phase))
    fig.canvas.draw()
    fig.canvas.flush_events()