from bokeh.io import push_notebook, show, output_notebook
from bokeh.plotting import figure
import numpy as np
import pandas as pd

output_notebook()

data = pd.read_csv('StudentsPerformance1.csv')

p = figure(title="Scatter plot")
p.circle('math_score', 'reading_score', source=data, fill_alpha=0.2, size=10)
show(p)

hist, edges = np.histogram(data['math_score'], density=True, bins=20)
p = figure(title='Histogram plot')
p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color='#6c1c91',
       line_color="white")
show(p)
