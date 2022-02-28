from dash import html
from dash.dependencies import Input, Output

from SCRIPTS.Dash.Components.Navbar import create_navbar
from SCRIPTS.Dash.HomePage import HomePage
from SCRIPTS.Dash.AnalysisPage import GlobalAnalysis
from SCRIPTS.app import webapp

webapp.layout = html.Div(children=[
    create_navbar(),
    html.Div(id='main-content')
])


@webapp.callback(Output('main-content', 'children'), [Input('tabs', 'active_tab')])
def switch_tab(at):
    if at == 'tab-0':
        return HomePage()
    elif at == 'tab-1':
        return GlobalAnalysis()
    return html.P("oops")
