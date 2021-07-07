import plotly_express as px
import csv
import numpy as np

def getDataSource(data_path):
    marks = []
    days_p = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for mark in csv_reader:
            marks.append(float(mark["Roll No"]))
            days_p.append(float(mark["Marks In Percentage"]))

    return{"x":marks,"y":days_p}

def findCorrel(datasource):
    correl = np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between Temperature and Ice Cream :\n", correl[0,1])

def setup():
    data_path = "b.csv"
    datasource = getDataSource(data_path)
    findCorrel(datasource)

setup()