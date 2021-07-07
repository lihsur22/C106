import plotly_express as px
import csv

with open("b.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x= "Marks In Percentage",y="Days Present")
    fig.show()