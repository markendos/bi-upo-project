from logging import PlaceHolder
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
from AvgPriceByCountry import AvgPriceByCountry
from ProductsBoughtTogether import ProductsBoughtTogether
from BestSalesByMonth import BestSalesByMonth

from root import app

numberOfPBT = 5
pbt = ProductsBoughtTogether()
bsbm = BestSalesByMonth()
apbc = AvgPriceByCountry()



tabla_productos_card = dbc.Card([
    dbc.CardBody([
        html.H2(children='Products that are bought together often'),
        pbt.getTable()
    ])
], className='h-100 my-4 mx-1 shadow-lg')
tabla_ventas_card = dbc.Card([
    dbc.CardBody([
        html.H2(children='Best sales by month'),
        bsbm.getTable(),
    ])
], className='h-100 my-4 mx-1 shadow-lg')

grafica_precio_card = dbc.Card([
    dbc.CardBody([
        html.H2(children="Average price by country"),
        dcc.Graph(id="avg_price_country", figure=apbc.getPlot())
    ])
], className='h-100 my-4 mx-1 shadow-lg')


layout = html.Div(
    [html.Div([
        dbc.Col(tabla_productos_card, width=6), dbc.Col(tabla_ventas_card, width=6)]
        , className='d-flex'),
     html.Div([
         dbc.Col(grafica_precio_card)
     ], className='d-flex h-100 my-4')
     ])


def get_layout():
    return layout
