"""

Création de la HomePage qui présente différents KPIs

KPIs : Nb de chansons écoutées, Nb d'artistes différents écoutés, Nb d'heures passées
Tableaux : Classement des chansons, artistes, albums.

"""
import dash_bootstrap_components as dbc
from dash import html
from SCRIPTS.Dash.Components.DashCards import CreateCards


def HomePage():
    homepage = html.Div(children=[
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
