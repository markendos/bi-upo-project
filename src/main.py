from logging import PlaceHolder
import dash
import dash_core_components as dcc
import dash_html_components as html
from ProductsBoughtTogether import ProductsBoughtTogether
from dash.dependencies import Input, Output

numberOfPBT = 5
def definirLayout():
    pbt = ProductsBoughtTogether()
    app.layout = html.Div(children=[
    html.H1(children='Sample App'),

    html.Div(children='''
        Sample App.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': ["Lunes", "Martes", "Miercoles"], 'y': [150, 200, 109], 'type': 'bar', 'name': '2015'},
                {'x': ["Lunes", "Martes", "Miercoles"], 'y': [150, 150, 150], 'type': 'bar', 'name': '2018'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),
    html.H2(children='Products that are bought together often'),
    pbt.getTable()
    
])




external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
definirLayout()


if __name__ == '__main__':
    app.run_server(debug=True)
