import csv
import plotly_express as px
import numpy as np

def getDataSource(data_path):
    CoffeeInML=[]
    SleepInHours=[]
    with open(data_path) as f: 
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            CoffeeInML.append(float(row["Coffee in ml"]))
            SleepInHours.append(float(row["sleep in hours"]))
    return{"x":CoffeeInML,"y":SleepInHours}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print ("correlation between coffee amount and sleep hours:-->",correlation[0,1])
    
def setup():
    data_path="coffee.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)

setup()







