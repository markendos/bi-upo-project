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

numberOfPBT = 5




def definirLayout():
    app.layout = html.Div(children=[
    html.H1(children='Sample App'),
    html.Div(children=[
            dbc.Tabs(
                [
                    dbc.Tab(label="Tab 1", tab_id="tab-1"),
                    dbc.Tab(label="Tab 2", tab_id="tab-2"),
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



definirLayout()
if __name__ == '__main__':
    app.run_server(debug=True)
