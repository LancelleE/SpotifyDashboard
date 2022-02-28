import dash_bootstrap_components as dbc
import dash

# APPLICATION PARAMETERS
webapp = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
webapp.title = "Spotify Analytics: Understand Your Music Habits!"
