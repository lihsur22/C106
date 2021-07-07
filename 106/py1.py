import plotly_express as px
import csv
import numpy as np

def getDataSource(data_path):
    icec_sales = []
    cold_sales = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            icec_sales.append(float(row["Temperature"]))
            cold_sales.append(float(row["Ice-cream Sales( â‚¹ )"]))

    return{"x":icec_sales,"y":cold_sales}

def findCorrel(datasource):
    correl = np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between Temperature and Ice Cream : \n",correl[0,1])

def setup():
    data_path = "c.csv"
    datasource = getDataSource(data_path)
    findCorrel(datasource)

setup()