### IMPORT MODULES ###
import dash_bootstrap_components as dbc
from dash import Dash, html

from SCRIPTS.Dash.HomePage import create_page_home

# APPLICATION PARAMETERS
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Avocado Analytics: Understand Your Avocados!"
app.layout = html.Div(children=[
    create_page_home()
])
if __name__ == '__main__':
    app.run_server(use_reloader=False)
