from logging import PlaceHolder
import dash
from dash_bootstrap_components._components.CardHeader import CardHeader
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
    dbc.CardHeader(html.H4(children='Products that are often visited together'),),
    
    dbc.CardBody([
        
        pbt.getTable()
    ])
], className='h-100 my-4 mx-1 shadow-lg')
tabla_ventas_card = dbc.Card([
    dbc.CardHeader(html.H4(children='Most visited products by month'),),
    dbc.CardBody([
        
        bsbm.getTable(),
    ])
], className='h-100 my-4 mx-1 shadow-lg')

grafica_precio_card = dbc.Card([
    dbc.CardHeader(html.H4(children="Average price by country"),),
    
    dbc.CardBody([
        
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
