"""

Création de la HomePage qui présente différents KPIs

KPIs : Nb de chansons écoutées, Nb d'artistes différents écoutés, Nb d'heures passées
Tableaux : Classement des chansons, artistes, albums.

"""
import dash_bootstrap_components as dbc
from dash import html
from Components.DashCards import CreateCards
from Components.Navbar import create_navbar


def HomePage():
    homepage = html.Div(children=[
        create_navbar(),
        dbc.Row(
            [
                dbc.Col(html.Div(), width=1),
                dbc.Col(CreateCards('test', 'test', 'test', 'primary'), width=2),
                dbc.Col(CreateCards('test', 'test', 'test', 'primary'), width=2),
                dbc.Col(CreateCards('test', 'test', 'test', 'primary'), width=2),
                dbc.Col(CreateCards('test', 'test', 'test', 'primary'), width=2),
                dbc.Col(CreateCards('test', 'test', 'test', 'primary'), width=2),
                dbc.Col(html.Div(), width=1)
            ]
        )

    ])
    return homepage


nav = create_navbar()
header = HomePage()


def create_page_home():
    layout = html.Div([
        nav,
        header,
    ])
    return layout
