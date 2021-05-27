import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from Tendencies import TendenciesDatamart as TDM
from BirthsAndGdpHelper import BirthsAndGdpHelper

from root import app

dm = TDM()
dataHelper = BirthsAndGdpHelper()

country_selector = html.Div([
    dcc.Dropdown(
        id='country-select',
        options=dm.getValues('country'),
        value='',
        placeholder="Select a country",
        multi=False,
        disabled=False
    ),
],
    style={'width': '100%', 'display': 'flex', 'flex-direction': 'column'})

radio_buttons1 = html.Div([
    dcc.RadioItems(
        id='crossfilter-yaxis-type',
        options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
        value='Linear',
        labelStyle={'display': 'inline-block', 'padding-left': '2rem'}),
    dcc.Graph(id='births-graph'),
],
    style={'width': '100%', 'display': 'flex', 'flex-direction': 'column'})
radio_buttons2 = html.Div([
    dcc.RadioItems(
        id='crossfilter-yaxis-type-2',
        options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
        value='Linear',
        labelStyle={'display': 'inline-block', 'padding-left': '2rem'}),
    dcc.Graph(id='gdp-graph'),
],
    style={'width': '100%', 'display': 'flex', 'flex-direction': 'column'})

selector_card = dbc.Card([
    dbc.CardBody([
        country_selector
    ])
], className='h-100 my-4 mx-1 shadow-lg ')

first_graph_card = dbc.Card([
     dbc.CardHeader([html.H4(children='Birth Predictions'),
                    html.Span(
        children='Prediction of births in each country.'),
    ]),
    dbc.CardBody([
        radio_buttons1
    ])
], className='h-100 my-4 mx-1 shadow-lg')
second_graph_card = dbc.Card([
     dbc.CardHeader([html.H4(children='GDP Predictions'),
                    html.Span(
        children='Prediction of GDP in each country.'),
    ]),
    dbc.CardBody([
        radio_buttons2
    ])
], className='h-100 my-4 mx-1 shadow-lg')

row_selector = html.Div([dbc.Col([selector_card], className="offset-6", width=6)])
row_graph = html.Div([dbc.Col(first_graph_card, width=12)])
row_graph2 = html.Div([dbc.Col(second_graph_card, width=12)])

layout = html.Div([row_selector, row_graph, row_graph2])
# BIRTHS


def create_birth_graph(data, axis_type, prediction):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=data['x'], y=data['y'], mode='lines+markers', name=data['name']))

    fig.add_trace(go.Scatter(
        x=prediction['x'], y=prediction['y'], mode='lines+markers', name=prediction['name']))

    fig.update_yaxes(type='linear' if axis_type == 'Linear' else 'log')

    fig.update_layout(title="Births", xaxis_title="Year", yaxis_title="Births number",
                      margin={'l': 20, 'b': 30, 'r': 10, 't': 40})

    return fig


@app.callback(
    Output('births-graph', 'figure'),
    [Input('country-select', 'value'),
     Input('crossfilter-yaxis-type', 'value')])
def update_births_graph(country, yaxis_type):
    data = dataHelper.getPlotDataBirths(country)
    predictionForNextYear = dataHelper.getBirthNumberPredictionForCountryAndYear(
        country, 2021)
    return create_birth_graph(data, yaxis_type, predictionForNextYear)

# GDP


def create_gdp_graph(data, axis_type, prediction):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=data['x'], y=data['y'], mode='lines+markers', name=data['name']))

    fig.add_trace(go.Scatter(
        x=prediction['x'], y=prediction['y'], mode='lines+markers', name=prediction['name']))

    fig.update_yaxes(type='linear' if axis_type == 'Linear' else 'log')

    fig.update_layout(title="GDP", xaxis_title="Year", yaxis_title="GDP",
                      margin={'l': 20, 'b': 30, 'r': 10, 't': 40})

    return fig


@app.callback(
    Output('gdp-graph', 'figure'),
    [Input('country-select', 'value'),
     Input('crossfilter-yaxis-type-2', 'value')])
def update_gdp_graph(country, yaxis_type):
    data = dataHelper.getPlotDataGDP(country)
    predictionForNextYear = dataHelper.getGDPPredictionByYearAndCountry(
        country, 2021)
    return create_gdp_graph(data, yaxis_type, predictionForNextYear)


def get_layout():
    return layout


if __name__ == '__main__':
    app.run_server(debug=True)
