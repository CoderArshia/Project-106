import csv
import plotly_express as px
import numpy as np

def getDataSource(data_path):
   marksInPercentage=[]
   Days_Present=[]
   with open(data_path) as f: 
       csv_reader=csv.DictReader(f)
       for row in csv_reader:
           marksInPercentage.append(float(row["Marks In Percentage"]))
           Days_Present.append(float(row["Days Present"]))
   return{"x": marksInPercentage,"y": Days_Present}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print ("correlation between marks and days present:-->",correlation[0,1])
    
def setup():
    data_path="marks and days present.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)

setup()







