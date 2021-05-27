from dash_bootstrap_components._components.CardBody import CardBody
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html


card_amalio = dbc.Card(
    [
        dbc.CardImg(
            src="https://avatars.githubusercontent.com/u/22647389?v=4", top=True),
        dbc.CardBody(
            html.A(href="https://github.com/AmalioF96",target="_blank", children="Amalio Cabeza Palacios" ,className="card-text")
        ),
    ], className='h-100 my-4 mx-1 shadow-lg',
)

card_marcos = dbc.Card(
    [
        dbc.CardImg(
            src="https://avatars.githubusercontent.com/u/57869508?v=4", top=True),
        dbc.CardBody(
            html.A(href="https://github.com/markendos", target="_blank", children="Marcos Witzl Daza", className="card-text")
        ),
    ], className='h-100 my-4 mx-1 shadow-lg',
)
card_alvaro = dbc.Card(
    [
        dbc.CardImg(
            src="https://avatars.githubusercontent.com/u/48862983?v=4", top=True),
        dbc.CardBody(
            html.A(href="https://github.com/AlvaroNavarroMora", target="_blank", children="Álvaro Navaro Mora", className="card-text")
        ),
    ], className='h-100 my-4 mx-1 shadow-lg',
)
card_luka = dbc.Card(
    [
        dbc.CardImg(
            src="https://avatars.githubusercontent.com/u/5711591?v=4", top=True),
        dbc.CardBody(
            html.A(href="https://github.com/lukebee", target="_blank", children="Luka Bubalo", className="card-text")
        ),
    ], className='h-100 my-4 mx-1 shadow-lg',
)

card_sobre_nosotros = html.Div([
    dbc.Col([
        dbc.Card([
            dbc.CardHeader(
                html.H3("Developers",
                        className="card-text")
            )
        ]),
        html.Div([
            dbc.Col(card_luka),
            dbc.Col(card_amalio),
            dbc.Col(card_alvaro),
            dbc.Col(card_marcos),
        ], className='d-flex')
    ], width=7),
    dbc.Col([
        dbc.Card([
            dbc.CardHeader(
                html.H3("About this project",
                        className="card-text")
            ),
            dbc.CardBody([
                dbc.CardImg(
                    src="https://www.upo.es/escuela-politecnica-superior/wp-content/uploads/2019/11/Logo-UPO-1.png", top=True),
                ]),
                html.P("This project has been developed for the Business Inteligence course of the GIISI degree of the UPO EPS.")
        ])
    ], width=5)
], className="d-flex h-100 my-4 mx-3")

layout=card_sobre_nosotros


def get_layout():
    return layout
