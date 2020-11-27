import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:\\Users\\lilya\\Desktop\\LNU\\Візуалізація даних\\StudentsPerformance.csv")

print("Перші 5 рядків\n ", data.head(5))
print("Назви стовпців\n ", data.columns.tolist())


# jointplot
sns.set(style='whitegrid')
sns.jointplot(x='writing_score', y='reading_score', data=data, kind='reg', color='#d627bf')
plt.savefig('jointplot.png')
plt.show()


# pairplot
sns.pairplot(data, hue='test preparation course', markers=['o', 's'], palette='Set1')
plt.savefig('pairplot.png')
plt.show()


# PairGrid
g = sns.PairGrid(data, hue='test preparation course', palette='Set2')
g.map_diag(sns.distplot)
g.map_offdiag(sns.scatterplot).add_legend()
plt.savefig('PairGrid.png')
plt.show()


# FaceGrid
color = {'color': ['r', 'b']}
g = sns.FacetGrid(data, col='lunch', row='test preparation course', hue='gender', hue_kws=color)
g = g.map(plt.scatter, 'reading_score', 'writing_score').add_legend()
plt.savefig('FaceGrid.png')
plt.show()


# barplot
sns.set_style('darkgrid')
b = sns.barplot(x='race/ethnicity', y='math_score', data=data, palette='rocket')
b.set_title('Barplot')
plt.savefig('barplot.png')
plt.show()


# countplot
sns.set_style('darkgrid')
c = sns.countplot(x='race/ethnicity', hue='parental level of education', data=data, palette='viridis')
c.set_title('Countplot with style')
c.set_ylabel('Count')
plt.savefig('countplot.png')
plt.show()


# violinplot + swarmplot
sns.violinplot(x='race/ethnicity', y='math_score', data=data, palette='rocket')
s = sns.swarmplot(x='race/ethnicity', y='math_score', data=data, color='black', size=2)
s.set_title('Violinplot and swarmplot')
plt.savefig('violin_swarm.png')
plt.show()


# heatmap
corr = data.corr()
h = sns.heatmap(corr, cmap='coolwarm', annot=True)
h.set_title('Heatmap')
plt.savefig('heatmap.png')
plt.show()


# clustermap
score_data = data.pivot_table(values='math_score',
                              index='parental level of education',
                              columns='race/ethnicity')
c = sns.clustermap(score_data, cmap='mako')
plt.title('Clustermap')
plt.savefig('clustermap.png')
plt.show()
