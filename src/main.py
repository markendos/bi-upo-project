from logging import PlaceHolder
import dash
import dash_core_components as dcc
import dash_html_components as html
from ProductsBoughtTogether import ProductsBoughtTogether
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import datetime

from root import app

import MainAmalio as ma
import MainMarcos as mm
import mainAlvaro as malv
import mainLuka as ml
import mainLuka2 as ml2
import about as aboutus
numberOfPBT = 5




def definirLayout():
    app.layout = html.Div(children=[
        html.Div(children=[
            html.H1(children='BI Solutions', className="col"),
            html.H5(id='live-update-text', className="col text-right"),
            dcc.Interval(
                id='interval-component',
                interval=60*1000, # in milliseconds
                n_intervals=0
            ),    
        ], className="d-flex px-4 py-2 align-items-center"),
        html.Div(children=[
            dbc.Tabs(
                [
                    dbc.Tab(label="Tab 1", tab_id="tab-1"),
                    dbc.Tab(label="Tab 2", tab_id="tab-2"),
                    dbc.Tab(label="Stratergy", tab_id="tab-3"),
                    dbc.Tab(label="About us", tab_id="tab-4"),
                ],
                id="tabs",
                active_tab="tab-1",
            ),
            html.Div(id='content')

        ]),
    
    ])


@app.callback(Output('content', 'children'),
              Input('tabs', 'active_tab'))
def render_content(tab):
    if tab == 'tab-1':
        tab_1_card=html.Div([ma.get_layout(),mm.get_layout()])
        return tab_1_card
    
    elif tab == 'tab-2':
        return malv.get_layout()
    elif tab == 'tab-3':
        return ml.get_layout()
    elif tab == 'tab-4':
        return aboutus.get_layout()


@app.callback(Output('live-update-text', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_date(n):
      return [html.Span('Last updated ' +str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M")))]

definirLayout()
if __name__ == '__main__':
    app.run_server(debug=True)
