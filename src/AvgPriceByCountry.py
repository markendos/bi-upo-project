from DBConnection import DBConnection
import plotly.graph_objs as go
import numpy as np

class AvgPriceByCountry:
    plot = None

    def __init__(self) -> None:
        pass

    def getPlot(self):
        db = DBConnection().db
        cursor = db.cursor()
        cursor.execute("select country, avg(price) from bi_solutions.shop group by country")
        result = cursor.fetchall()
        c = []
        p = []
        for row in result:
            c.append(row[0])
            p.append(row[1])
            
        data = [go.Bar(
            x = c,
            y = p
        )]
        fig = go.Figure(data=data)
        cursor.close()
        db.close()
        return fig