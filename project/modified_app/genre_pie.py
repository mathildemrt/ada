import pandas as pd
import numpy as np

import pickle

import os

from bokeh.io import output_file, show, export_svgs
from bokeh.layouts import widgetbox, row, column,layout
from bokeh.models.widgets import Select, CheckboxGroup,RangeSlider, Slider
from bokeh.models import ColumnDataSource, HoverTool, Div, Range1d
from bokeh.plotting import curdoc, figure
from bokeh.client import push_session
from bokeh.charts import Donut

from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.embed import components






f = open('dataframe-final', 'rb')
df = pickle.load(f)

genre_color = {'blues': '#75bbfd', 'country': '#653700', 'electronica': '#9a0eea', 'folk': '#f97306', 'jazz': '#fac205',
               'pop': '#ff81c0', 'metal': '#000000', 'rock': '#2242c7', 'orchestral': '#929591', 'hiphop': '#e50000',
               'reggae': '#02ab2e', 'world': '#a0bf16'}




def update(attr, old, new):
    layout.children[1] = create_figure()




checkbox_year = CheckboxGroup(labels=["Show songs with missing location","Show songs with missing year"], active=[0])
checkbox_year.on_change('active', update)

year_slider = RangeSlider(start=1940, end=2011, value=(1940,2011), step=5, title="year")
year_slider.on_change('value', update)


(start, end) = year_slider.value

dfy=df[(df.year>=start) & (df.year<=end)]

dfyc = dfy[dfy.artist_latitude>=0]



def create_figure():


    p = figure(plot_height=400, plot_width=400)

    count = df.genre.value_counts()

    colors = [genre_color[x] for x in count.index.sort_values()]

    p = Donut(count, label='index', color=colors, height=400, width=400,hover_text='#songs')

    p.title.text = "#Songs = {}".format(len(df))




    py = figure(plot_height=400, plot_width=400)

    count = dfy.genre.value_counts()

    colors = [genre_color[x] for x in count.index.sort_values()]

    py = Donut(count, label='index', color=colors, height=400, width=400, hover_text='#songs')

    py.title.text = "#Songs w/o missing year = {}".format(len(dfy))




    pyc = figure(plot_height=400, plot_width=400)

    count = dfyc.genre.value_counts()

    colors = [genre_color[x] for x in count.index.sort_values()]

    pyc = Donut(count, label='index', color=colors, height=400, width=400, hover_text='#songs')

    pyc.title.text = "#Songs w/o missing year and location = {}".format(len(dfyc))


    return p,py,pyc


controls = widgetbox([checkbox_year,year_slider], width=200)

a,b,c=create_figure()
layout = row(controls, a,b,c)

curdoc().add_root(layout)
curdoc().title = "Hottness_familiarity"

plots = {'1':a,'2': b,'3':c}

script, div = components(plots)
print(script)
print(div)