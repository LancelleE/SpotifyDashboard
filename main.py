### IMPORT MODULES ###
from SCRIPTS.DataScripts.RecupHistory import import_all
from dash import Dash
from SCRIPTS.Dash.Components.DashCards import CreateCards
import dash_bootstrap_components as dbc

### APPLICATION PARAMETERS ###
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Avocado Analytics: Understand Your Avocados!"
app.layout = CreateCards('test', 'test', 'test', 'primary')

if __name__ == '__main__':
    app.run_server(use_reloader=False)
