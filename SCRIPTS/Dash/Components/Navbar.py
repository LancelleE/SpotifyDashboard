import dash_bootstrap_components as dbc
from dash import html


def create_navbar():
    # Create the Navbar using Dash Bootstrap Components
    navbar = html.Div(
        [

            dbc.Tabs(
                [
                    dbc.Tab(label="HomePage", tab_id="tab-0"),
                    dbc.Tab(label="Global Analysis", tab_id="tab-1"),
                    dbc.Tab(label="Artist Analysis", tab_id="tab-2"),
                    dbc.Tab(label="Some KPIs", tab_id="tab-3")
                ],
                id="tabs",
                active_tab="tab-0",
            )
        ]
    )

    return navbar
