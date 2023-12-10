import numpy as np 
import matplotlib.pyplot as plt 

years = [2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]#smart way of adding years 
weight = [80,83,85,81,79,82,84,82,85,81,80,83,86,85,87,82,90]

plt.plot(years,weight, c="red", lw=3, linestyle="--")
plt.show()