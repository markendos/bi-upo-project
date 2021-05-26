import mainLuka2 as ml2
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from Distributions import DistributionsDatamart as DDM
from Modes import ModesDatamart as MDM

from root import app

ddm = DDM()
mdm = MDM()


pie_chart = html.Div([
    dcc.Graph(id='pie'),
])
selector_paises = html.Div([
    dcc.Dropdown(
        id='paises-select',
        options=mdm.getVariables(),
        value='General',
        placeholder="Select a variable",
    )
])
selector_propiedades = html.Div([
    dcc.Dropdown(
        id='propiedades-select',
        options=ddm.getVariables(),
        value='clicks',
        placeholder="Select a variable",

    )
])

radio_items = html.Div([
    dcc.RadioItems(
        id='agg-operation',
        options=[{'label': i, 'value': i} for i in ['Avg', 'Max']],
        value='Avg',
        labelStyle={'display': 'inline-block', 'margin': '3px'}),
])

histograma = html.Div([
    dcc.Graph(id='histogram'),
])


hist_card = dbc.Card([
    dbc.CardHeader([
        html.H4(children='Frequency histogram'),
        html.Span(
            children='Histogram with the Maximun and Average by session of the elements Clicks, Page number and Price')
    ]),

    dbc.CardBody([
        selector_propiedades,
        radio_items,
        histograma
    ])

], className='h-100 my-4 mx-1 shadow-lg')

pie_card = dbc.Card([
    dbc.CardHeader(html.H4(children='Mode by country'),),
    dbc.CardBody([
        selector_paises,
        pie_chart
    ]),

], className='h-100 my-4 mx-1 shadow-lg')

bubble_plot = ml2.get_layout()

layout = html.Div([dbc.Col(hist_card, width=4), bubble_plot, dbc.Col(
    pie_card, width=3)], className='d-flex my-4')


def create_hist(datos, axis_type, variable):

    fig = go.Figure()

    fig.add_trace(go.Histogram(datos))

    fig.update_layout(title="Frequency Hist of ({})".format(variable), xaxis_title="Occurence count of {}".format(variable),
                      yaxis_title="Frequency", margin={'l': 20, 'b': 30, 'r': 10, 't': 40})

    return fig


def create_pie(datos, value):

    fig = go.Figure()

    my_v = datos['v']
    my_n = datos["n"]
    fig.add_trace(go.Pie(labels=my_n, values=my_v))

    # , margin={'l': 20, 'b': 30, 'r': 10, 't': 40})
    fig.update_layout(title="Mode of ({})".format(value))

    return fig


@app.callback(
    Output('histogram', 'figure'),
    [Input('propiedades-select', 'value'),
     Input('agg-operation', 'value')])
def update_histogram(variable, operation):

    data = ddm.getPlotData(variable, operation)
    return create_hist(data, operation, variable)


@app.callback(
    Output('pie', 'figure'),
    Input('paises-select', 'value'))
def update_pies(value):
    data = mdm.getPlotData(value)
    return create_pie(data, value)


def get_layout():
    return layout
