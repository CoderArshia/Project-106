import csv 
import plotly_express as px
import pandas as pd

df=pd.read_csv("coffee.csv")
fig= px.scatter(df,x="Coffee in ml",y="sleep in hours")
fig.show()