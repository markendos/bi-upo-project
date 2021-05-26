from logging import PlaceHolder
import dash
import dash_core_components as dcc
import dash_html_components as html
from ProductsBoughtTogether import ProductsBoughtTogether
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from root import app

import MainAmalio as ma
import MainMarcos as mm
import mainAlvaro as malv
import mainLuka as ml
import about as aboutus
numberOfPBT = 5




def definirLayout():
    app.layout = html.Div(children=[
    html.H1(children='Sample App'),
    html.Div(children=[
            dbc.Tabs(
                [
                    dbc.Tab(label="Tab 1", tab_id="tab-1"),
                    dbc.Tab(label="Tab 2", tab_id="tab-2"),
                    dbc.Tab(label="Tab 3", tab_id="tab-3"),
                    dbc.Tab(label="Estrategia", tab_id="tab-4"),
                    dbc.Tab(label="About us", tab_id="tab-5"),
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
        return ma.get_layout()
    elif tab == 'tab-2':
        return mm.get_layout()
    elif tab == 'tab-3':
        return malv.get_layout()
    elif tab == 'tab-4':
        return ml.get_layout()
    elif tab == 'tab-5':
        return aboutus.get_layout()



definirLayout()
if __name__ == '__main__':
    app.run_server(debug=True)
