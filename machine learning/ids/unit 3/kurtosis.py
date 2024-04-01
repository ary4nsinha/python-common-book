from scipy.stats import kurtosis 
import matplotlib.pyplot as plt
dataset = [88,85,82,97,67,77,74,86,81,95,77,88,85,76,81]
print(kurtosis(dataset))
import seaborn as sns

sns.kdeplot(dataset)
plt.show()