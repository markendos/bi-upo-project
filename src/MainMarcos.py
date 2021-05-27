import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from Tendencies import TendenciesDatamart as TDM

from root import app

dm = TDM()

selector_variables = html.Div([
    dcc.Dropdown(
        id='first-select',
        options=dm.getVariables(),
        value='',
        placeholder="Select a variable",
    )
],
    style={'width': '48%', 'display': 'flex', 'flex-direction': 'column'})
selector_values = html.Div([
    dcc.Dropdown(
        id='second-select',
        options=list(),
        value='',
        placeholder="Select a value",
        multi=True,
        disabled=True
    ),
],
    style={'width': '48%', 'display': 'flex', 'flex-direction': 'column'})
radio_items = dcc.RadioItems(
            id='crossfilter-yaxis-type',
            options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
            value='Linear',
            labelStyle={'display': 'inline-block', 'padding-left': '2rem'})

tendency_graph = dbc.Card([
    dbc.CardHeader([
        html.H4(children='Tendency Graph'),
    html.Span(
            children='This chart show the tendency of the numeric variables on the time.')
    ]),
    dbc.CardBody([
        html.Div([
        selector_variables,
        selector_values,
    ],style={'display': 'flex', 'justify-content': 'space-between', 'padding': '2rem'}),

    html.Div([
        radio_items,
        dcc.Graph(id='time-series'),
    ],
        style={'width': '100%', 'display': 'flex', 'flex-direction': 'column'}),

    ])
], className='h-100 my-4 mx-1 shadow-lg')

layout = html.Div([dbc.Col(tendency_graph)], className='d-flex')



def create_time_series(data, axis_type, variable):
    fig = go.Figure()
    for d in data:
        fig.add_trace(go.Scatter(x=d['x'], y=d['y'],
                                 mode='lines+markers', name=d['name']))

    fig.update_yaxes(type='linear' if axis_type == 'Linear' else 'log')
    if variable == '':
        variable = 'none'
    fig.update_layout(title="Tendency chart ({})".format(variable), xaxis_title="Date",
                      yaxis_title="Frequency", margin={'l': 20, 'b': 30, 'r': 10, 't': 40})

    return fig


@app.callback(
    Output('time-series', 'figure'),
    [Input('first-select', 'value'),
     Input('second-select', 'value'),
     Input('crossfilter-yaxis-type', 'value')])
def update_timeseries(variable, value, yaxis_type):
    data = dm.getPlotData(variable, value)
    return create_time_series(data, yaxis_type, variable)


@app.callback(
    Output('second-select', 'options'),
    Output('second-select', 'value'),
    [Input('first-select', 'value')])
def update_values_selector(value):
    if value in (None, ''):
        return list(), ''
    else:
        return dm.getValues(value), ''


@app.callback(
    Output('second-select', 'disabled'),
    [Input('first-select', 'value')])
def set_values_selector_state(value):
    return value in (None, '')


def get_layout():
    return layout


if __name__ == '__main__':
    app.run_server(debug=True)
