### IMPORT MODULES ###
import dash_bootstrap_components as dbc
from dash import Dash, html

### APPLICATION PARAMETERS ###
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Avocado Analytics: Understand Your Avocados!"
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    ''')
])
if __name__ == '__main__':
    app.run_server(use_reloader=False)
