import matplotlib.pyplot as plt 

x = [10,20,30,40,50]
y = [30,30,30,30,30]

plt.plot(x,y)
plt.show()

plt.plot(y,x)
plt.show()

plt.plot(x,y, label = "line 1")
plt.plot(y,x, label = "line 2")

plt.legend()
plt.show()
