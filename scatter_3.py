import csv 
import plotly_express as px
import pandas as pd

df=pd.read_csv("marks and days present.csv")
fig= px.scatter(df,x="Marks In Percentage",y="Days Present")
fig.show()