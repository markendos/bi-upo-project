import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from BirthsAndGdpHelper import BirthsAndGdpHelper


from root import app


dataHelper = BirthsAndGdpHelper()
graph_card=dbc.Card([
    dbc.CardBody([
        dcc.RadioItems(
            id='crossfilter-yaxis-type',
            options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
            value='Linear',
            labelStyle={'display': 'inline-block', 'padding-left': '2rem'}),
        dcc.Graph(id='births-clicks-graph')
    ])
], className='h-100 my-4 mx-1 shadow-lg')

layout=dbc.Col(graph_card,width=5)
## BIRTHS
def create_births_click_graph(data, axis_type):
    fig = go.Figure()

    maxZ = 0
    for record in data:
        maxZ = max(maxZ, max(record['z']))

    for record in data:
        fig.add_trace(go.Scatter(
            x=record['x'], y=record['y'],
            mode='lines+markers',
            name=record['name'],
            marker_size=record['z'],
            text=[
                'Country:' + str(record['name']) +
                '<br>GDP:' + str(record['x']) +
                '<br>Birth number:' + str(record['y']) +
                '<br>Clicks number:' + str(record['z'])
            ],
            marker=dict(
                size=record['z'],
                sizemode='area',
                sizeref=2. * maxZ / (40. ** 2),
                sizemin=4
            )
        ))

    fig.update_yaxes(type='linear' if axis_type == 'Linear' else 'log')

    fig.update_layout(title="GDP, clicks and births distribution for 2008", xaxis_title="GDP", yaxis_title="Births number",
                      margin={'l': 20, 'b': 30, 'r': 10, 't': 40})

    return fig

@app.callback(
    Output('births-clicks-graph', 'figure'),
    [Input('crossfilter-yaxis-type', 'value')])
def update_births_clicks_graph(yaxis_type):
    data = dataHelper.getPlotDataBirthsClicks()
    return create_births_click_graph(data, yaxis_type)

def get_layout():
    return layout
