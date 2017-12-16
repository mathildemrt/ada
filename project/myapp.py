import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.preprocessing import OneHotEncoder
from pandas.plotting import scatter_matrix
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import cross_val_score
from scipy import stats
import seaborn as sns
import re

import tables as tb

import pickle
import requests
import geocoder
from bs4 import BeautifulSoup
from collections import*
import matplotlib
import matplotlib.pyplot as plt
from PythonSrc.hdf5_getters import *

import PythonSrc.hdf5_getters as GETTERS

import os
import sys
import time
import glob
import datetime


import unidecode


from bokeh.io import output_file, show,export_svgs
from bokeh.layouts import widgetbox,row,column
from bokeh.models.widgets import Select,CheckboxGroup
from bokeh.models.widgets import RangeSlider, Slider
from bokeh.models import ColumnDataSource, HoverTool, Div,Range1d
from bokeh.plotting import curdoc, figure
from bokeh.client import push_session
from bokeh.layouts import layout, widgetbox
from bokeh.charts import Donut

from bokeh.io import push_notebook, output_notebook

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

def song_selected():
    if genre_s.value=='all':
        selected=df[(df.artist_hotttnesss>0) & (df.artist_familiarity>0)]
    else :
        selected=df[(df.genre==genre_s.value) & (df.artist_hotttnesss>0) & (df.artist_familiarity>0)]

    (start, end)=year_slider.value
    #if 0 in checkbox_year.active:
    #    selected=selected[(selected.year>=start) & (selected.year<=end) | (selected.year==0)]
    #else:
    #    selected = selected[(selected.year >= start) & (selected.year <= end)]
    selected = selected[(selected.year >= start) & (selected.year <= end)]

    return selected

def outlier(row,coeff,var):
    x=row.artist_familiarity
    y=row.artist_hotttnesss
    
    d=y-coeff[0]*x-coeff[1]
    
    if abs(d)<=var:
        d=0
        
    return d


def update(attr, old, new):
    p,q= create_figure()
    layout.children[1] = p
    layout.children[2] = q
    
genre_s = Select(title="Genre:", value="all", options=genre_list)
genre_s.on_change('value', update)

genre_d = Select(title="If Genre is all, pie chart of songs:", value="all", options=["all", "between the limit","upward outlier","downward outliers"])
genre_d.on_change('value', update)

var_slider = Slider(start=0.04, end=0.2, value=0.1, step=.02, title="Outlier limit")
var_slider.on_change('value', update)

checkbox_group = CheckboxGroup(labels=["Show regression line","Show outlier limits"], active=[0,1])
checkbox_group.on_change('active', update)

#checkbox_year = CheckboxGroup(labels=["Show songs with missing year"], active=[])
#checkbox_year.on_change('active', update)


year_slider = RangeSlider(start=1940, end=2010, value=(1940,2000), step=10, title="year")
year_slider.on_change('value', update)



def create_figure():

    q = figure(plot_height=400, plot_width=400,tools=[])

    data = song_selected()

    p = figure(plot_height=400, plot_width=400)
    if len(data)>0:

        hover = HoverTool(tooltips=[
            ("Artist", "@artist"),
            ("Genre", "@genre"),
            ("Year", "@year")
        ])

        source = ColumnDataSource(data=dict(artist=data.artist_name,genre=data.genre,year=data.year))


        # Get the linear models
        coeff = np.polyfit(data.artist_familiarity, data.artist_hotttnesss	, 1)

        var = var_slider.value
        x_ = np.copy([0, 1.])
        ymean = x_ * coeff[0] + coeff[1]

    
        data['outlier']=data.apply(lambda row: outlier(row,coeff,var),raw=True,axis=1)


        n_out=len(data[data['outlier']!=0])
        corr=np.corrcoef(x=data.artist_familiarity, y=data.artist_hotttnesss)
        corr=corr[0,1]
        title='correlation = {:.2f}   ;  #outliers={}'.format(corr,n_out)
        p = figure(plot_height=400, plot_width=400,title=title,tools=[hover,'box_zoom','wheel_zoom'])
        p.xaxis.axis_label = "Artist familiarity"
        p.yaxis.axis_label = "Artist hotttnesss"
        p.circle(x=data.artist_familiarity, y=data.artist_hotttnesss,source=source, color=data.color, line_color="White", alpha=0.6,
              hover_color='white', hover_alpha=0.5)

        p.x_range = Range1d(0, 1)
        p.y_range = Range1d(0, 1)


        if 0 in  checkbox_group.active:
            p.line(x_,ymean,color="black",line_width=2)
        if 1 in checkbox_group.active:
            y1 = ymean - var
            y2 = ymean + var
            p.multi_line([x_, x_], [y1, y2],color=["black", "black"], alpha=[0.8, 0.8], line_width=2, line_dash='dashed')

        if genre_s.value=='all':
            data_high = data[data['outlier'] > 0]
            data_r = data[data['outlier'] == 0]
            data_low = data[data['outlier'] < 0]


            if (genre_d.value == 'upward outlier') & (len(data_high)>0):

                count = data_high.genre.value_counts()

                colors = [genre_color[x] for x in count.index.sort_values()]

                q = Donut(count, label='index', color=colors, height=400, width=400,hover_text='#songs')
                q.title.text = "#Artists = {}".format(len(data_high))



            elif (genre_d.value == 'between the limit') & (len(data_r)>0):

                count = data_r.genre.value_counts()

                colors = [genre_color[x] for x in count.index.sort_values()]

                q = Donut(count, label='index', color=colors, height=400, width=400,hover_text='#songs')
                q.title.text = "#Artists = {}".format(len(data_r))

            elif (genre_d.value == 'downward outliers') & (len(data_low)>0):

                count = data_low.genre.value_counts()

                colors = [genre_color[x] for x in count.index.sort_values()]

                q = Donut(count, label='index', color=colors, height=400, width=400,hover_text='#songs')
                q.title.text = "#Artists = {}".format(len(data_low))

            elif genre_d.value == 'all':
                count = data.genre.value_counts()


                colors = [genre_color[x] for x in count.index.sort_values()]


                q = Donut(count,label='index',color=colors, height=400, width=400,hover_text='#songs')
                q.title.text = "#Artists = {}".format(len(data))


    return p,q













controls = widgetbox([genre_s,year_slider,var_slider,checkbox_group,genre_d], width=200)

#layout =row(controls, create_figure())
a,b=create_figure()
layout =row(controls, a,b)



curdoc().add_root(layout)
curdoc().title = "Hottness_familiarity"

