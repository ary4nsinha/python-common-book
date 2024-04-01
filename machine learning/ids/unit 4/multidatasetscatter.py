import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,3,5,7,11]

x1 = [2,3,4,5,6]
y1 = [1,4,9,16,25]  

x2 = [4,2,1,3,8]
y2 = [6,7,2,11,15]

plt.scatter(x,y, color='red',label='Data Set 1')
plt.scatter(x1,y1, color='blue', label='Data Set 2')
plt.scatter(x2,y2, color='green', label='Data Set 3')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter plot with multiple datasets')
plt.legend()
plt.grid(True)
plt.show()

#bar plots in matplotlib