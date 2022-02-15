"""

Ici on va créer la fonction qui permet de générer des cartes.
Arguments :
- Titre.
- KPI Principal.
- Petit texte qui apporte une précision.

"""
import dash_bootstrap_components as dbc
from dash import html


def CreateCards(Header, MainKPI, SmallText, color):
    MyCard = dbc.Card(
        [
            dbc.CardHeader(Header),
            dbc.CardBody(
                [
                    html.H5(MainKPI),
                    html.P(SmallText)
                ]
            )
        ],
        color=color
    )
    return MyCard
