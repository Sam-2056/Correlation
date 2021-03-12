import plotly.express as px
import pandas as pd
import csv

with open("./data/Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv") as csv_file:
      df = pd.read_csv(csv_file)
      fig = px.scatter(df,x="Temperature", y="IcecreamSales")
      fig.show()
