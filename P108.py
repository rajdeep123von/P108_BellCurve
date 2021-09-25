import csv
import pandas as pd 
import plotly.figure_factory as ff

readcsv = pd.read_csv("ProjectData.csv")
plot = ff.create_distplot([readcsv["Avg Rating"].tolist()],["Avg Rating"],show_hist=True)
 
plot.show() 

