# -*- coding: utf-8 -*-
"""
1. read a CSV file

"""

#%%
import tkinter as tk
from tkinter import filedialog

#%%
## use GUI to select file
root = tk.Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
#print (root.filename)
root.withdraw()

#%%
# read a  CSV File
import pandas as pd 
df = pd.read_csv(root.filename)

#%%
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x =df['x']
y =df['y']
z =df['z']

ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel('Reaction in x dir.')
ax.set_ylabel('Reaction in y dir.')
ax.set_zlabel('swing rate')
#ax.invert_xaxis()


# control the angle of view
ax.view_init(azim=60)
plt.show()

#%%
x =df['x']
z =df['z']

plt.figure(figsize=(8,6))

plt.scatter(x, z, c='r', marker='o')
plt.title('basic scatter plot ')
plt.xlabel('Reaction in x dir.')
plt.ylabel('swing rate')

plt.legend(loc='upper right')

plt.show()

#%%

plt.figure(figsize=(8,6))

plt.scatter(y, z, c='r', marker='o')
plt.title('basic scatter plot ')
plt.xlabel('Reaction in y dir.')
plt.ylabel('swing rate')

plt.legend(loc='upper right')

plt.show()


#%%

plt.figure(figsize=(8,6))

plt.scatter(x, y, c='r', marker='o')
plt.title('basic scatter plot ')
plt.xlabel('Reaction in x dir.')
plt.ylabel('Reaction in y dir.')

plt.legend(loc='upper right')

plt.show()
