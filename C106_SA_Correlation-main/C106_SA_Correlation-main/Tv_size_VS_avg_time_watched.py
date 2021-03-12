import plotly.express as px
import pandas as pd
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = pd.read_csv(csv_file)
        fig = px.scatter(df,x="Size of TV", y="Average time spent watching TV in a week (hours)")
        fig.show()

def getDataSource(data_path):
    Tv_Size = []
    Average_time_spent = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Tv_Size.append(float(row["Size of TV"]))
            Average_time_spent.append(float(row["Average time spent watching TV in a week (hours)"]))

    return {"x" : Tv_Size, "y": Average_time_spent}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Tv Size vs Average time spent:-  \n--->",correlation[0,1])

def setup():
    data_path  = "./data/SizeTV.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()
