from logging import PlaceHolder
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from ProductsBoughtTogether import ProductsBoughtTogether
from BestSalesByMonth import BestSalesByMonth

numberOfPBT = 5
def definirLayout():
    pbt = ProductsBoughtTogether()
    bsbm = BestSalesByMonth()
    app.layout = html.Div(children=[
    html.H1(children='Alvaro\'s Components'),
    html.H2(children='Products that are bought together often'),
    pbt.getTable(),
    html.H2(children='Best sales by month'),
    bsbm.getTable()
])

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
definirLayout()


if __name__ == '__main__':
    app.run_server(debug=True)
