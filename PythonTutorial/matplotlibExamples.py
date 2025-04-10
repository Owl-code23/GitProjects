import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])
#plt.plot(xpoints, ypoints)
#plt.show()

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
#plt.plot(xpoints, ypoints, 'o')
#plt.show()

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8 , 1, 10])
#plt.plot(xpoints, ypoints)
#plt.show()

ypoints = np.array([3, 8, 1, 10, 5, 7])
#plt.plot(ypoints)
#plt.show()

ypoints = np.array([3, 8, 1, 10])
#plt.plot(ypoints, marker = 'o')
#plt.show()

#plt.plot(ypoints, marker = "*")
#plt.show()

#Format Strings fmt: marker|line|color
#plt.plot(ypoints, 'o:r')
#plt.show()

#markersize or ms 
#plt.plot(ypoints, marker = 'o', ms = 20)
#plt.show()

#markeredgecolor or mec
#plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
#plt.show()

#markerfacecolor or mfc
#plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
#plt.show()

#mec and mfc
#plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')
#plt.show()

#hex color value
#plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
#plt.show()

#colornames
#plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
#plt.show()

#Linestyle or ls
#ypoints = np.array([3, 8, 1, 10])
#plt.plot(ypoints, linestyle = 'dotted')
#plt.show()

#plt.plot(ypoints, ls = ':')
#plt.show()

#color
#ypoints = np.array([3, 8, 1, 10])
#plt.plot(ypoints, color = 'r')
#plt.show()

#plt.plot(ypoints, c = '#4CAF50')
#plt.show()

#plt.plot(ypoints, c = 'hotpink')
#plt.show()

#linewidth or lw
#plt.plot(ypoints, linewidth = '20.5')
#plt.show()

#Multiple Lines
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
#plt.plot(y1)
#plt.plot(y2)
#plt.show()

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])
#plt.plot(x1, y1, x2, y2)
#plt.show()

#label() and title()
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#plt. plot(x, y)
#plt.xlabel("Average Pulse")
#plt.ylabel("Calorie Burnage")
#plt.title("Sports Watch Data")
#plt.show()

#Font Properties for Title and Labels
font1 = {'family':'serif', 'color':'blue', 'size':20}
font2 = {'family':'serif', 'color':'darkred', 'size':15}

#Position the Title with loc
#plt.title("Sport Watch Data", fontdict = font1, loc = 'left')
#plt.xlabel("Average Pulse", fontdict = font2)
#plt.ylabel("Calorie Burnage", fontdict = font2)
#plt.plot(x, y)

#grid() or grid(axis = 'both')
#plt.grid()

#Only x axis
#plt.grid(axis = 'x')

#grid(color = 'color', linestyle = 'linestyle', linewidth = number)
#plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

#plt.show()

#Subplot(row, columns, index)
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
#plt.subplot(2, 1, 1)
#plt.subplot(1, 2, 1)
#plt.plot(x, y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
#plt.subplot(2, 1, 2)
#plt.subplot(1, 2, 2)
#plt.plot(x, y)
#suptitle()
#plt.suptitle("MY TITLE")
#plt.show()

#scatter()
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
#plt.scatter(x, y, color = 'hotpink')

#Compare Plots
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
#plt.scatter(x, y, color = '#88c999')
#plt.show()

#Color each dot
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red", "green", "blue", "yellow", "pink", "black", "orange", "purple", "beige", "brown", "gray", "cyan", "magenta"])
#plt.scatter(x, y, c = colors)
#plt.show()

#ColorMap cmap
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
#plt.scatter(x, y, c = colors, cmap = 'viridis')
#colorbar()
#plt.colorbar()
#plt.show()

#Size s
sizes = np.array([20, 50, 100, 200, 500, 1000, 60, 90, 10, 300, 600, 800, 75])
#plt.scatter(x, y, s = sizes)
#plt.show()

#Transparency alpha
#plt.scatter(x, y, s = sizes, alpha = 0.5)
#plt.show()

#Combine color size and alpha
x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
#colors = np.random.randint(100, size=(100))
#sizes = 10 * np.random.randint(100, size=(100))

#plt.scatter(x, y, c = colors, s = sizes, alpha = 0.5, cmap='nipy_spectral')
#plt.colorbar()
#plt.show()

#Bars
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
#plt.bar(x,y)
#plt.show()

#Horizontal Bars
#plt.barh(x,y)
#plt.show()

#Color
#plt.bar(x, y, color = "red") # color = "hotpink", color = "#4CAF50"
#plt.show()

#Bar width
#plt.bar(x, y, width = 0.1)
#plt.show()

#Bar height
#plt.barh(x, y, height = 0.1)
#plt.show()

#Histograms hist()
x = np.random.normal(170, 10, 250)
#print(x)
#plt.hist(x)
#plt.show()

#Pie Charts pie()
y = np.array([35, 25, 25, 15]) # x/sum(x)
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
#plt.pie(y, labels = mylabels)
#plt.show()

#changed start angle
#plt.pie(y, labels = mylabels, startangle = 90)
#plt.show()

#Explode
myexplode = [0.2, 0, 0, 0]
#plt.pie(y, labels = mylabels, explode = myexplode)
#plt.show()

#Shadow
#plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
#plt.show()

#Colors
mycolors = ["black", "hotpink", "b", "#4CAF50"]
#plt.pie(y, labels = mylabels, colors = mycolors)
#plt.show()

#Legend
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show()