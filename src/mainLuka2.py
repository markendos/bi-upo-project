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
            id='crossfilter-query-type',
            options=[{'label': i, 'value': i} for i in ['Clicks', 'Sessions (users)']],
            value='Clicks',
            labelStyle={'display': 'inline-block', 'padding-left': '1rem'}),
        dcc.Graph(id='births-clicks-graph')
    ])
], className='h-100 my-4 mx-1 shadow-lg')

layout=dbc.Col(graph_card,width=5)
## BIRTHS
def create_births_click_graph(data, queryType):
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
                'Country: {}'.format(record['name']) +
                '<br>GDP: {}'.format(record['x']) +
                '<br>Birth number: {}'.format(record['y']) +
                '<br>Number of {}: {}'.format(queryType, record['z'])
            ],
            marker=dict(
                size=record['z'],
                sizemode='area',
                sizeref=2. * maxZ / (40. ** 2),
                sizemin=4
            )
        ))

    fig.update_layout(title="GDP, {} and births distribution by country in 2008".format(queryType), xaxis_title="GDP", yaxis_title="Births number",
                      margin={'l': 20, 'b': 30, 'r': 10, 't': 40})

    return fig

@app.callback(
    Output('births-clicks-graph', 'figure'),
    [Input('crossfilter-query-type', 'value')])
def update_births_clicks_graph(queryType):
    data = dataHelper.getPlotDataBirthsClicks(queryType == 'Clicks')
    return create_births_click_graph(data, queryType)

def get_layout():
    return layout
