import pandas as pd
import numpy as np

import pickle

import os

from bokeh.io import output_file, show, export_svgs
from bokeh.layouts import widgetbox, row, column
from bokeh.models.widgets import Select, CheckboxGroup
from bokeh.models.widgets import RangeSlider, Slider
from bokeh.models import ColumnDataSource, HoverTool, Div, Range1d
from bokeh.plotting import curdoc, figure
from bokeh.client import push_session
from bokeh.layouts import layout, widgetbox
from bokeh.charts import Donut
from bokeh.embed import components

f = open('dataframe-final', 'rb')
df = pickle.load(f)
df=df.sort_values(['year'], ascending=[0])
df=df.reset_index()
df=df.drop_duplicates(subset='artist_name', keep='first')

genre_color={'blues':'#75bbfd','country':'#653700','electronica':'#9a0eea','folk':'#f97306','jazz':'#fac205',
             'pop':'#ff81c0','metal':'#000000','rock':'#2242c7','orchestral':'#929591','hiphop':'#e50000',
             'reggae':'#02ab2e','world':'#a0bf16','all':'#0485d1'}

df['color']=df.genre.apply(lambda genre: genre_color[genre])

genre_list=['all']

for g in df['genre'].unique():
    genre_list.append(g)


N=100

df = df[(df.year >= 1940) & (df.year <= 2011)]


df1=df.sort_values(['artist_hotttnesss'], ascending=[0])
df1=df1.head(N)

df2=df.sort_values(['artist_hotttnesss'], ascending=[1])
df2=df2.head(N)

df3=df.sort_values(['artist_familiarity'], ascending=[0])
df3=df3.head(N)

df4=df.sort_values(['artist_familiarity'], ascending=[1])
df4=df4.head(N)


count = df1.genre.value_counts()
colors = [genre_color[x] for x in count.index.sort_values()]
p1 = Donut(count, label='index', color=colors, height=400, width=400,hover_text='#Artist')
p1.title.text = "100 hotttest Artist"


count = df2.genre.value_counts()
colors = [genre_color[x] for x in count.index.sort_values()]
p2 = Donut(count, label='index', color=colors, height=400, width=400,hover_text='#Artist')
p2.title.text = "100 less hottt Artist"


count = df3.genre.value_counts()
colors = [genre_color[x] for x in count.index.sort_values()]
p3 = Donut(count, label='index', color=colors, height=400, width=400,hover_text='#Artist')
p3.title.text = "100 most familiar Artist"


count = df4.genre.value_counts()
colors = [genre_color[x] for x in count.index.sort_values()]
p4 = Donut(count, label='index', color=colors, height=400, width=400,hover_text='#Artist')
p4.title.text = "100 less familiar Artist"



layout = row(p1,p2,p3,p4)

curdoc().add_root(layout)
curdoc().title = "Hottness_familiarity"
plots = {'1': p1, '2': p2,'3':p3,'4':p4}

script, div = components(plots)

file = open("testfile.txt", "w")

file.write(script)

print(div)