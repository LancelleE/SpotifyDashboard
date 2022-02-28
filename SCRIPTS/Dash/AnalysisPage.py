from dash import html
import dash_bootstrap_components as dbc


from SCRIPTS.Dash.Components.DashCards import CreateCards

def GlobalAnalysis():
    page = html.Div(children=[
        dbc.Row(
            [
                dbc.Col(html.Div(), width=1),
                dbc.Col(CreateCards('prout', 'test', 'test', 'primary'), width=2),
                dbc.Col(CreateCards('test', 'test', 'test', 'primary'), width=2),
                dbc.Col(CreateCards('test', 'test', 'test', 'primary'), width=2),
                dbc.Col(CreateCards('test', 'test', 'test', 'primary'), width=2),
                dbc.Col(CreateCards('test', 'test', 'test', 'primary'), width=2),
                dbc.Col(html.Div(), width=1)
            ]
        )

    ])
    return page