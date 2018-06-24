#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
For SI 507 Waiver, fall 2018
@author: oshinnayak, onayak @umich.edu

"""
import plotly

plotly.tools.set_credentials_file(username='oshinnayak', api_key='dzwXJKLmD5S1bndnc7RR')


import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd 
import csv

# Code here should involve creation of the bar chart as specified in instructions
# And opening / using the CSV file you created earlier with noun data from tweets
# Define a csv reader function

csvfile= '/Users/oshinnayak/Desktop/noun_data.csv'
df = pd.read_csv(csvfile)
#print(df['Noun'])
trace1 = go.Bar(x=df['Noun'], y=df['Number'],text=df['Noun'])           
data = [trace1]
layout = go.Layout(title='Nouns Analysis', width=500, height=600)
fig = go.Figure(data=data, layout=layout)
py.image.save_as(fig, filename='part4_viz_image.png')
