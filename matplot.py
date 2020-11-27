import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("C:\\Users\\lilya\\Desktop\\LNU\\Візуалізація даних\\StudentsPerformance.csv")

print("Перші 5 рядків\n ", data.head(5))
print("Назви стовпців\n ", data.columns.tolist())


# histogram
x = data['math_score']
y = data['writing_score']
plt.hist([x, y], color=['#32a87d', '#d627bf'])
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.title('Histogram for math and writing score')
plt.legend(['math score', 'writing score'])
plt.show()


# histograms
sns.set(style='whitegrid')
grid = sns.FacetGrid(data, row='gender', col='race/ethnicity',
                     margin_titles=True)
grid.map(plt.hist, 'math_score', color='crimson')
plt.show()

# boxplot 1
sns.set(style='whitegrid')
sns.boxplot(x='parental level of education', y='math_score',
            hue='test preparation course', data=data, palette='Set3')
plt.show()

# boxplot 2
sns.catplot(x='gender', y='math_score',
            hue='test preparation course', col='race/ethnicity',
            data=data, kind='box', height=4, aspect=.7)
plt.show()


# scatter plot
sns.scatterplot(data=data, x='reading_score', y='writing_score',
                hue='gender', style='gender')
plt.show()


# correlation
corr = data.corr()
print(corr)
plt.title('Correlation matrix')
sns.heatmap(corr, cmap="YlGnBu", linewidths=0.1)
plt.show()
