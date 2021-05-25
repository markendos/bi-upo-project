import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from Distributions import DistributionsDatamart as DDM
from Modes import ModesDatamart as MDM
import pandas as pd
import numpy as np
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
dm = DDM()
mm = MDM()

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='first-select',
                options=dm.getVariables(),
                value='Clicks',
                placeholder="Select a variable",
            )
        ],
        style={'width': '48%', 'display': 'flex', 'flex-direction': 'column'}),   
        html.Div([
        dcc.RadioItems(
                id='agg-operation',
                options=[{'label': i, 'value': i} for i in ['Avg', 'Max']],
                value='Avg',
                labelStyle={'display': 'inline-block', 'padding-left': '2rem'}),
        ],
        style={'width': '100%', 'display': 'flex', 'flex-direction': 'column'}),
    ],
    style={'display': 'flex', 'justify-content': 'space-between', 'padding': '2rem'}),
        
    html.Div([
        dcc.Graph(id='histogram'),
    ],
    style={'width': '100%', 'display': 'flex', 'flex-direction': 'column'}),
    html.Div([
        html.Div([
                dcc.Dropdown(
                    id='second-select',
                    options=mm.getVariables(),
                    value='General',
                    placeholder="Select a variable",
                )
        ],
        style={'width': '48%', 'display': 'flex', 'flex-direction': 'column'}),
        
        
    ],
    style={'display': 'flex', 'justify-content': 'space-between', 'padding': '2rem'}),
    html.Div([
            dcc.Graph(id='pie'),
    ],
    style={'width': '100%', 'display': 'flex', 'flex-direction': 'column'}),
])

def create_hist(datos, axis_type, variable):
    
    fig = go.Figure()
    
    fig.add_trace(go.Histogram(datos))

    fig.update_layout(title="Distribution Chart ({})".format(variable), xaxis_title="Date", yaxis_title="Frequency", margin={'l': 20, 'b': 30, 'r': 10, 't': 40})
    
    return fig

def create_pie(datos):
    
    fig = go.Figure()
    
    my_v=datos['v']
    my_n=datos["n"]
    fig.add_trace(go.Pie(labels=my_n, values=my_v))

    #fig.update_layout(title="Distribution Chart ({})".format(variable), xaxis_title="Date", yaxis_title="Frequency", margin={'l': 20, 'b': 30, 'r': 10, 't': 40})
    
    return fig


@app.callback(
    Output('histogram', 'figure'),
    [Input('first-select', 'value'),
    Input('agg-operation', 'value')])
def update_histogram(variable, operation):
    
    data = dm.getPlotData(variable,operation)
    return create_hist(data, operation, variable)

@app.callback(
    Output('pie', 'figure'),
    Input('second-select', 'value'))
def update_pies(value):
    data = mm.getPlotData(value)
    return create_pie(data)


if __name__ == '__main__':
    app.run_server(debug=True)