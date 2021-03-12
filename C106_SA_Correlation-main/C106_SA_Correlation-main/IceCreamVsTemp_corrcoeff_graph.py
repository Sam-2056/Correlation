import plotly.express as px
import pandas as pd
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = pd.read_csv(csv_file)
        fig = px.scatter(df,x="Temperature", y="IcecreamSales")
        fig.show()

def getDataSource(data_path):
    temperature = []
    ice_cream_sales = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            temperature.append(float(row["Temperature"]))
            ice_cream_sales.append(float(row["IcecreamSales"]))

    return {"x" : temperature, "y": ice_cream_sales}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Temperature vs Ice Cream Sales :-  \n--->",correlation[0,1])

def setup():
    data_path  = "./data/Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()
