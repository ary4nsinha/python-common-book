from scipy.stats import skew 
import matplotlib.pyplot as plt
import seaborn

dataset = [88,85,82,97,67,77,74,86,81,95,77,88,85,76,81]
print(skew(dataset))
import seaborn as sns 
sns.kdeplot(dataset)
plt.show()