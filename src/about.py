from dash_bootstrap_components._components.CardBody import CardBody
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html


card_amalio = dbc.Card(
    [
        dbc.CardImg(
            src="https://avatars.githubusercontent.com/u/22647389?v=4", top=True),
        dbc.CardBody(
            html.P("Amalio Cabeza Palacios", className="card-text")
        ),
        dbc.CardFooter([
            html.Li([""])
        ], style={"class": "bi-github", "role": "img", 'aria-label': "GitHub"})
    ], className='h-100 my-4 mx-1 shadow-lg',
)

card_marcos = dbc.Card(
    [
        dbc.CardImg(
            src="https://avatars.githubusercontent.com/u/57869508?v=4", top=True),
        dbc.CardBody(
            html.P("Marcos Witzl Daza", className="card-text")
        ),
        dbc.CardFooter([
            html.Li([""])
        ], style={"class": "bi-github", "role": "img", 'aria-label': "GitHub"})
    ], className='h-100 my-4 mx-1 shadow-lg',
)
card_alvaro = dbc.Card(
    [
        dbc.CardImg(
            src="https://avatars.githubusercontent.com/u/48862983?v=4", top=True),
        dbc.CardBody(
            html.P("Álvaro Navaro Mora", className="card-text")
        ),
        dbc.CardFooter([
            html.Li([""])
        ], style={"class": "bi-github", "role": "img", 'aria-label': "GitHub"})
    ], className='h-100 my-4 mx-1 shadow-lg',
)
card_luka = dbc.Card(
    [
        dbc.CardImg(
            src="https://avatars.githubusercontent.com/u/5711591?v=4", top=True),
        dbc.CardBody(
            html.P("Luka Bubalo", className="card-text")
        ),
        dbc.CardFooter([
            html.Li([""])
        ], style={"class": "bi-github", "role": "img", 'aria-label': "GitHub"})
    ], className='h-100 my-4 mx-1 shadow-lg',
)

card_sobre_nosotros = html.Div([
    dbc.Col([
        dbc.Card([
            dbc.CardHeader(
                html.H3("Cuadro de mandos",
                        className="card-text")
            ),
            dbc.CardBody([
                html.P("Conclusión del documento", className="card-text"),
                html.P("Este proyecto ha sido desarrollado aprovechando las tecnologías Dash y Python", className="card-text"),
            ])
        ])
    ], width=5),
    dbc.Col([
        dbc.Card([
            dbc.CardHeader(
                html.H3("Desarrolladores del proyecto",
                        className="card-text")
            )
        ]),
        html.Div([
            dbc.Col(card_amalio),
            dbc.Col(card_marcos),
            dbc.Col(card_alvaro),
            dbc.Col(card_luka)
        ], className='d-flex')
    ], width=7)
], className="d-flex h-100 my-4 mx-3")

layout=card_sobre_nosotros


def get_layout():
    return layout
