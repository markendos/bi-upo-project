import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from Tendencies import Datamart as dm

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='first-select',
                options=dm.get_variables(),
                value='',
                placeholder="Select a variable",
            )
        ],
            style={'width': '48%', 'display': 'flex', 'flex-direction': 'column'}),

        html.Div([
            dcc.Dropdown(
                id='second-select',
                options=dm.get_values('country'),
                value='',
                placeholder="Select a value",
                multi=True,
                disabled=True
            ),
        ],
            style={'width': '48%', 'display': 'flex', 'flex-direction': 'column'}),
    ],
        style={'display': 'flex', 'justify-content': 'space-between', 'padding': '2rem'}),

    html.Div([
        dcc.RadioItems(
            id='crossfilter-yaxis-type',
            options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
            value='Linear',
            labelStyle={'display': 'inline-block', 'padding-left': '2rem'}),
        dcc.Graph(id='time-series'),
    ],
        style={'width': '100%', 'display': 'flex', 'flex-direction': 'column'}),
])


def create_time_series(data, axis_type, variable):
    fig = go.Figure()
    for d in data:
        fig.add_trace(go.Scatter(x=d['x'], y=d['y'], mode='lines+markers', name=d['name']))

    fig.update_yaxes(type='linear' if axis_type == 'Linear' else 'log')
    if variable == '':
        variable = 'none'
    fig.update_layout(title="Tendency chart ({})".format(variable), xaxis_title="Date", yaxis_title="Frequency",
                      margin={'l': 20, 'b': 30, 'r': 10, 't': 40})

    return fig


@app.callback(
    Output('time-series', 'figure'),
    [Input('first-select', 'value'),
     Input('second-select', 'value'),
     Input('crossfilter-yaxis-type', 'value')])
def update_timeseries(variable, value, yaxis_type):
    data = dm.get_plot_data(variable, value)
    return create_time_series(data, yaxis_type, variable)


@app.callback(
    Output('second-select', 'options'),
    Output('second-select', 'value'),
    [Input('first-select', 'value')])
def update_values_selector(value):
    if value in (None, ''):
        return list(), ''
    else:
        return dm.get_values(value), ''


@app.callback(
    Output('second-select', 'disabled'),
    [Input('first-select', 'value')])
def set_values_selector_state(value):
    return value in (None, '')


if __name__ == '__main__':
    app.run_server(debug=True)