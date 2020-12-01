import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

data = np.loadtxt('sqisland2.csv', delimiter=",", skiprows=1)
xcoords = data[:,0]
ycoords = data[:,1]
gene1 = data[:,2]
gene2 = data[:,3]
gene3 = data[:,4]
gene4 = data[:,5]
gene5 = data[:,6]
gene6 = data[:,7]
gene7 = data[:,8]



plot1 = plt.figure(1)
plt.contourf(xcoords.reshape(10,10), ycoords.reshape(10,10), gene1.reshape(10,10), vmin = 0, vmax = 1)

plt.title("gene1")
plt.xlabel("X")
plt.ylabel("Y")

plot1 = plt.figure(8)
plt.contourf(xcoords.reshape(10,10), ycoords.reshape(10,10), gene1.reshape(10,10))
plt.title("gene1 - normalised values")
plt.xlabel("X")
plt.ylabel("Y")

plot2 = plt.figure(2)
plt.contourf(xcoords.reshape(10,10), ycoords.reshape(10,10), gene2.reshape(10,10), vmin = 0, vmax = 1)
plt.title("gene2")
plt.xlabel("X")
plt.ylabel("Y")

plot2 = plt.figure(9)
plt.contourf(xcoords.reshape(10,10), ycoords.reshape(10,10), gene2.reshape(10,10))
plt.title("gene2 - normalised values")
plt.xlabel("X")
plt.ylabel("Y")

plot3 = plt.figure(3)
plt.contourf(xcoords.reshape(10,10), ycoords.reshape(10,10), gene3.reshape(10,10), vmin = 0, vmax = 1)
plt.title("gene3")
plt.xlabel("X")
plt.ylabel("Y")

plot3 = plt.figure(10)
plt.contourf(xcoords.reshape(10,10), ycoords.reshape(10,10), gene3.reshape(10,10))
plt.title("gene3 - normalised values")
plt.xlabel("X")
plt.ylabel("Y")

plot4 = plt.figure(4)
plt.contourf(xcoords.reshape(10,10), ycoords.reshape(10,10), gene4.reshape(10,10), vmin = 0, vmax = 1)
plt.title("gene4")
plt.xlabel("X")
plt.ylabel("Y")

plot4 = plt.figure(11)
plt.contourf(xcoords.reshape(10,10), ycoords.reshape(10,10), gene4.reshape(10,10))
plt.title("gene4 - normalised values")
plt.xlabel("X")
plt.ylabel("Y")


plot5 = plt.figure(5)
plt.contourf(xcoords.reshape(10,10), ycoords.reshape(10,10), gene5.reshape(10,10), vmin = 0, vmax = 1)
plt.title("gene5")
plt.xlabel("X")
plt.ylabel("Y")

plot4 = plt.figure(12)
plt.contourf(xcoords.reshape(10,10), ycoords.reshape(10,10), gene5.reshape(10,10))
plt.title("gene5 - normalised values")
plt.xlabel("X")
plt.ylabel("Y")


plot6 = plt.figure(6)
plt.contourf(xcoords.reshape(10,10), ycoords.reshape(10,10), gene6.reshape(10,10), vmin = 0, vmax = 1)
plt.title("gene6")
plt.xlabel("X")
plt.ylabel("Y")

plot4 = plt.figure(13)
plt.contourf(xcoords.reshape(10,10), ycoords.reshape(10,10), gene6.reshape(10,10))
plt.title("gene6 - normalised values")
plt.xlabel("X")
plt.ylabel("Y")


plot7 = plt.figure(7)
plt.contourf(xcoords.reshape(10,10), ycoords.reshape(10,10), gene7.reshape(10,10), vmin = 0, vmax = 1)
plt.title("gene7")
plt.xlabel("X")
plt.ylabel("Y")

plot4 = plt.figure(14)
plt.contourf(xcoords.reshape(10,10), ycoords.reshape(10,10), gene7.reshape(10,10))
plt.title("gene7 - normalised values")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()



print("Var of Gene 1: " + str(np.var(gene1)))
print("Var of Gene 2: " + str(np.var(gene2)))
print("Var of Gene 3: " + str(np.var(gene3)))
print("Var of Gene 4: " + str(np.var(gene4)))
print("Var of Gene 5: " + str(np.var(gene5)))
print("Var of Gene 6: " + str(np.var(gene6)))
print("Var of Gene 7: " + str(np.var(gene7)))

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 