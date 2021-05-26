import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from Tendencies import TendenciesDatamart as TDM
from BirthsAndGdpHelper import BirthsAndGdpHelper

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
dm = TDM()
dataHelper = BirthsAndGdpHelper()

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='country-select',
                options=dm.getValues('country'),
                value='',
                placeholder="Select a country",
                multi=False,
                disabled=False
            ),
        ],
            style={'width': '100%', 'display': 'flex', 'flex-direction': 'column'}),
    ],
        style={'display': 'flex', 'justify-content': 'space-between', 'padding': '2rem'}),

    html.Div([
        dcc.RadioItems(
            id='crossfilter-yaxis-type',
            options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
            value='Linear',
            labelStyle={'display': 'inline-block', 'padding-left': '2rem'}),
        dcc.Graph(id='births-graph'),
    ],
        style={'width': '100%', 'display': 'flex', 'flex-direction': 'column'}),

    html.Div([
        dcc.RadioItems(
            id='crossfilter-yaxis-type-2',
            options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
            value='Linear',
            labelStyle={'display': 'inline-block', 'padding-left': '2rem'}),
        dcc.Graph(id='gdp-graph'),
    ],
        style={'width': '100%', 'display': 'flex', 'flex-direction': 'column'}),
])

## BIRTHS
def create_birth_graph(data, axis_type, prediction):
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=data['x'], y=data['y'], mode='lines+markers', name=data['name']))

    fig.add_trace(go.Scatter(x=prediction['x'], y=prediction['y'], mode='lines+markers', name=prediction['name']))

    fig.update_yaxes(type='linear' if axis_type == 'Linear' else 'log')

    fig.update_layout(title="Births", xaxis_title="Year", yaxis_title="Births number",
                      margin={'l': 20, 'b': 30, 'r': 10, 't': 40})

    return fig

@app.callback(
    Output('births-graph', 'figure'),
    [Input('country-select', 'value'),
     Input('crossfilter-yaxis-type', 'value')])
def update_births_graph(value, yaxis_type):
    data = dataHelper.getPlotDataBirths(value)
    predictionForNextYear = dataHelper.getBirthNumberPredictionForCountryAndYear(value, 2021)
    return create_birth_graph(data, yaxis_type, predictionForNextYear)

## GDP
def create_gdp_graph(data, axis_type, prediction):
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=data['x'], y=data['y'], mode='lines+markers', name=data['name']))

    fig.add_trace(go.Scatter(x=prediction['x'], y=prediction['y'], mode='lines+markers', name=prediction['name']))

    fig.update_yaxes(type='linear' if axis_type == 'Linear' else 'log')

    fig.update_layout(title="GDP", xaxis_title="Year", yaxis_title="GDP",
                      margin={'l': 20, 'b': 30, 'r': 10, 't': 40})

    return fig

@app.callback(
    Output('gdp-graph', 'figure'),
    [Input('country-select', 'value'),
     Input('crossfilter-yaxis-type-2', 'value')])
def update_gdp_graph(value, yaxis_type):
    data = dataHelper.getPlotDataGDP(value)
    predictionForNextYear = dataHelper.getGDPPredictionByYearAndCountry(value, 2021)
    return create_gdp_graph(data, yaxis_type, predictionForNextYear)

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080, debug=True)