#!/usr/bin/env python3
import ast
import plotly.express as px
import os

DATA_DIRECTORY = './data/'
Imported_Data = {}

# Loads and parses data in txt files into a dictionary
for file in os.listdir(DATA_DIRECTORY):
  if file.endswith(".txt"):
    Imported_Data[file] = {}
    Imported_Data[file]['Time'] = []
    Imported_Data[file]['Occupancy'] = []
    lines = open(DATA_DIRECTORY + file, 'r').readlines()
    for l in lines:
      line_as_list = ast.literal_eval(l.rstrip())
      Imported_Data[file]['Time'].append(line_as_list[0])
      Imported_Data[file]['Occupancy'].append(int(line_as_list[1]))

    df = Imported_Data[file]
    fig = px.line(df, x="Time", y="Occupancy", line_shape='linear')
    fig.update_layout(title=file)
    fig.show()