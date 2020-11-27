# -*- coding: utf-8 -*-
"""1_plot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gwOdX2HOnRXV8JBXCUVYdzVvcpMk1k39
"""

import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np

x = np.arange(-3, 5, 0.1)


def f(x):
    return (x - 2) ** 2


def h(x):
    return np.cos(x) + 2


"""***Відображення двох графіків кривої + легенда***"""

fig = go.Figure()

# add y and x axes
fig.update_yaxes(range=[-2, 8], zeroline=True, zerolinewidth=2,
                 zerolinecolor='Black')
fig.update_xaxes(range=[-1, 5], zeroline=True, zerolinewidth=2,
                 zerolinecolor='Black')

# add f(x) to the graph
fig.add_trace(go.Scatter(x=x, y=f(x), mode='lines+markers',
                         name='f(x)=(x -2)<sup>2</sup>',
                         marker=dict(color='rgba(0, 255, 200, 0.8)')))
# add h(x) to the graph
fig.add_trace(go.Scatter(x=x, y=h(x), mode='lines+markers',
                         name='h(x)= cos(x)+ 2',
                         marker=dict(color='rgb(204, 0, 0)', size=10,
                                     line=dict(color='rgb(255, 77, 77)', width=3))))
fig.update_layout(legend_orientation="h", legend=dict(x=.5, xanchor="center"),
                  hovermode="x", margin=dict(l=0, r=0, t=0, b=0))

fig.show()

"""***Додавання теплової карти на графік***"""

fig = go.Figure()

# add y and x axes
fig.update_yaxes(range=[-1, 25], zeroline=True, zerolinewidth=2,
                 zerolinecolor='Black')
fig.update_xaxes(range=[-5, 5], zeroline=True, zerolinewidth=2,
                 zerolinecolor='Black')

fig.add_trace(go.Scatter(x=x, y=f(x), mode='lines+markers',
                         name='f(x)=(x-2)<sup>2</sup>',
                         marker=dict(color=f(x), colorbar=dict(title="f(x)=(x-2)**2"),
                                     colorscale='rdbu')))

fig.add_trace(go.Scatter(x=x, y=h(x), mode='lines+markers',
                         name='h(x)= cos(x)+ 2',
                         marker=dict(color=f(x))))

fig.update_layout(legend_orientation="h",
                  legend=dict(x=.5, xanchor="center"),
                  margin=dict(l=0, r=0, t=0, b=0))

fig.update_traces(hoverinfo="all", hovertemplate="Аргумент: %{x}<br> Функція: %{y}")

fig.show()

"""***Додавання анімації***"""

fig = go.Figure()
fig.add_trace(go.Scatter(x=[x[0]], y=[f(x)[0]], mode='lines+markers',
                         name='f(x)=(x-2)<sup>2</sup>', marker=dict(color=f(x[0]),
                                                                    colorbar=dict(title="f(x)=(x-2) **2"),
                                                                    colorscale='Inferno')))
frames = []
for i in range(1, len(x)):
    frames.append(go.Frame(data=[go.Scatter(x=x[:i + 3], y=f(x[:i + 3]),
                                            marker=dict(color=h(x[:i + 3])))]))
fig.frames = frames
fig.update_layout(legend_orientation="h", legend=dict(x=3, xanchor="center"),
                  updatemenus=[dict(direction="left", x=0.5, xanchor="center", y=0,
                                    type="buttons",
                                    buttons=[dict(label="►", method="animate", args=[None, {"fromcurrent": True}]),
                                             dict(label="❚❚",
                                                  method="animate",
                                                  args=[[None], {"frame": {"duration": 0, "redraw": False},
                                                                 "mode": "immediate",
                                                                 "transition": {"duration": 0}}])])],
                  margin=dict(l=0, r=0, t=0, b=0))

fig.update_traces(hoverinfo="all", hovertemplate="Аргумент: %{x}<br>Функція: %{y}")

fig.show()

"""***Додавання слайдера***"""

num_steps = len(x)
fig = go.Figure(
    data=[go.Scatter(x=[x[0]],
                     y=[f(x)[0]], mode='lines+markers',
                     name='f(x)=(x-2) **2',
                     marker=dict(color=[f(x[0])],
                                 colorbar=dict(yanchor='top', y=0.8, title="f(x)=(x-2)<sup>2</sup>"),
                                 colorscale='Inferno')),

          go.Scatter(x=[x[0]], y=[h(x)[0]],
                     mode='lines+markers', name='h(x)=cos(x)+2',
                     marker=dict(color=[h(x[0])], colorscale='Inferno'))])
frames = []
for i in range(0, len(x)):
    frames.append(
        go.Frame(name=str(i), data=[go.Scatter(x=x[:i + 1], y=f(x[:i + 1]),
                                               mode='lines+markers', name='f(x)= (x-2)**2',
                                               marker=dict(color=f(x[:i + 1]),
                                                           colorscale='Inferno')),
                                    go.Scatter(x=x[:i + 1], y=h(x[:i + 1]), mode='lines+markers',
                                               name='h(x)=cos(x) + 2',
                                               marker=dict(color=h(x[:i + 1]), colorscale='Inferno'))]))

steps = []
for i in range(num_steps):
    step = dict(label=str(i), method="animate", args=[[str(i)]])
    steps.append(step)

sliders = [dict(currentvalue={"prefix": "Крок №", "font": {"size": 20}},
                len=0.9, x=0.1, pad={"b": 10, "t": 50}, steps=steps, )]

fig.update_layout(title="Будуємо квадратичну функцію і косинус покроково",
                  xaxis_title="ВісьX", yaxis_title="ВісьY", updatemenus=[dict(direction="left",
                                                                              pad={"r": 10, "t": 80}, x=0.1,
                                                                              xanchor="right", y=0, yanchor="top",
                                                                              showactive=False, type="buttons",
                                                                              buttons=[dict(label="►", method="animate",
                                                                                            args=[None, {
                                                                                                "fromcurrent": True}]),
                                                                                       dict(label="❚❚",
                                                                                            method="animate",
                                                                                            args=[[None], {
                                                                                                "frame": {"duration": 0,
                                                                                                          "redraw": False},
                                                                                                "mode": "immediate",
                                                                                                "transition": {
                                                                                                    "duration": 0}}])])], )

fig.layout.sliders = sliders
fig.frames = frames
fig.show()

num_steps = len(x)
fig = go.Figure(
    data=[go.Scatter(x=[x[0]],
                     y=[f(x)[0]], mode='lines+markers',
                     name='f(x)=(x-2) **2',
                     marker=dict(color=[f(x[0])],
                                 colorbar=dict(yanchor='top', y=0.8, title="f(x)=(x-2)<sup>2</sup>"),
                                 colorscale='Inferno')),

          go.Scatter(x=[x[0]], y=[h(x)[0]],
                     mode='lines+markers', name='h(x)=cos(x)+2',
                     marker=dict(color=[h(x[0])], colorscale='Inferno'))])
frames = []
for i in range(0, len(x)):
    frames.append(
        go.Frame(name=str(i), data=[go.Scatter(x=x[:i + 1], y=f(x[:i + 1]),
                                               mode='lines+markers', name='f(x)= (x-2)**2',
                                               marker=dict(color=f(x[:i + 1]),
                                                           colorscale='Inferno')),
                                    go.Scatter(x=x[:i + 1], y=h(x[:i + 1]), mode='lines+markers',
                                               name='h(x)=cos(x) + 2',
                                               marker=dict(color=h(x[:i + 1]), colorscale='Inferno'))]))

steps = []
for i in range(num_steps):
    step = dict(label=str(i), method="animate", args=[[str(i)]])
    steps.append(step)

sliders = [dict(currentvalue={"prefix": "Крок №", "font": {"size": 20}},
                len=0.9, x=0.1, pad={"b": 10, "t": 50}, steps=steps, )]

fig.update_layout(title="Будуємо квадратичну функцію і косинус покроково",
                  xaxis_title="ВісьX", yaxis_title="ВісьY", updatemenus=[dict(direction="left",
                                                                              pad={"r": 10, "t": 80}, x=0.1,
                                                                              xanchor="right", y=0, yanchor="top",
                                                                              showactive=False, type="buttons",
                                                                              buttons=[dict(label="►", method="animate",
                                                                                            args=[None, {
                                                                                                "fromcurrent": True}]),
                                                                                       dict(label="❚❚",
                                                                                            method="animate",
                                                                                            args=[[None], {
                                                                                                "frame": {"duration": 0,
                                                                                                          "redraw": False},
                                                                                                "mode": "immediate",
                                                                                                "transition": {
                                                                                                    "duration": 0}}])])], )

fig.layout.sliders = sliders
fig.frames = frames
fig.show()
