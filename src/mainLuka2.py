import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from BirthsAndGdpHelper import BirthsAndGdpHelper

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
dataHelper = BirthsAndGdpHelper()

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[
    html.Div([
        dcc.RadioItems(
            id='crossfilter-yaxis-type',
            options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
            value='Linear',
            labelStyle={'display': 'inline-block', 'padding-left': '2rem'}),
        dcc.Graph(id='births-clicks-graph'),
    ],
        style={'width': '100%', 'display': 'flex', 'flex-direction': 'column'}),
])

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

if __name__ == '__main__':
    app.run_server(debug=True)