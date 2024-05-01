import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

# plt.plot(xpoints, ypoints)
# plt.show()

# ** Plotting without line

# plt.plot(xpoints, ypoints, 'o') # Rings in the diagram
# plt.show()

# ** Multiple points

xpoints = np.array([1,2,6,8])
ypoints = np.array([3,8,1,10])

# plt.plot(xpoints, ypoints) 
# plt.show()

# ** Delfault X-Points (get the default value of 0,1,2,3)

ypoints = np.array([3,8,1,10,5,7])
# plt.plot(ypoints)
# plt.show()

# ** Markers
"""
'o'	Circle	
'*'	Star	
'.'	Point	
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline
"""

ypoints = np.array([3,8,1,10])
# plt.plot(ypoints, marker = 'o')
# plt.plot(ypoints, marker = '*')
# plt.show()

# ** Line Reference
"""
'-'	Solid line	
':'	Dotted line	
'--'	Dashed line	
'-.'	Dashed/dotted line
"""

# ** Color reference
"""
'r'	Red	
'g'	Green	
'b'	Blue	
'c'	Cyan	
'm'	Magenta	
'y'	Yellow	
'k'	Black	
'w'	White
"""

# ** marker size (ms)
ypoints = np.array([3,8,1,10])
# plt.plot(ypoints, marker='o', ms=20)
# plt.show()

# ** Text in the diagram

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.title("Sports Watch Data", loc = 'left')
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")

# plt.plot(x, y)
# plt.grid(axis = 'x') # add a grid
# plt.show()

# ** Subplot

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

# plt.subplot(1, 2, 1)
# plt.plot(x,y)
# plt.title("SALES")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

# plt.subplot(1, 2, 2)
# plt.plot(x,y)
# plt.title("INCOME")

# plt.suptitle("MY SHOP")
# plt.show()

# ** Creating Bars

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

# plt.bar(x,y, width = 0.1)
# plt.show()

# ** Histogram

x = np.random.normal(170, 10, 250)

# plt.hist(x)
# plt.show() 


# ** Pie chart

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show() 