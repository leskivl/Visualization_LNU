import pandas as pd
from plotnine import *
import matplotlib.pyplot as plt

data = pd.read_csv("C:\\Users\\lilya\\Desktop\\LNU\\Візуалізація даних\\StudentsPerformance1.csv")
print("Назви стовпців\n ", data.columns.tolist())

# histogram
h = (ggplot(data) + aes(x='math_score', color='gender')
     + geom_histogram(binwidth=15) + ggtitle("Histogram of Math score"))
hist = h.draw()
plt.show()

# boxplot
b = ggplot(data) \
    + aes(x='parental level of education', y='reading_score', fill='parental level of education') \
    + geom_boxplot() + ggtitle("Boxplot of reading score")
box = b.draw()
plt.show()

# scatter plot
s = (ggplot(data)
     + aes(x='reading_score', y='writing_score')
     + geom_point(aes(color='gender'))) + ggtitle("Scatter plot")
scatter = s.draw()
plt.show()
