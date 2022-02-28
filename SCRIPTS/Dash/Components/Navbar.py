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
                ],
                id="tabs",
                active_tab="tab-1",
            ),
            html.Div(id="content"),
        ]
    )

    return navbar

#
#
# def create_navbar():
#     # Create the Navbar using Dash Bootstrap Components
#     navbar = dbc.NavbarSimple(
#         children=[
#             dbc.DropdownMenu(
#                 nav=True,
#                 in_navbar=True,
#                 label="Menu",  # Label given to the dropdown menu
#                 children=[
#                     # In this part of the code we create the items that will appear in the dropdown menu on the right
#                     # side of the Navbar.  The first parameter is the text that appears and the second parameter
#                     # is the URL extension.
#                     dbc.DropdownMenuItem("Home", href='/'),  # Hyperlink item that appears in the dropdown menu
#                     dbc.DropdownMenuItem(divider=True),  # Divider item that appears in the dropdown menu
#                     dbc.DropdownMenuItem("Page 2", href='/page-2'),  # Hyperlink item that appears in the dropdown menu
#                     dbc.DropdownMenuItem("Page 3", href='/page-3'),  # Hyperlink item that appears in the dropdown menu
#                 ],
#             ),
#         ],
#         brand="Home",  # Set the text on the left side of the Navbar
#         brand_href="/",  # Set the URL where the user will be sent when they click the brand we just created "Home"
#         sticky="top",  # Stick it to the top... like Spider Man crawling on the ceiling?
#         color="dark",  # Change this to change color of the navbar e.g. "primary", "secondary" etc.
#         dark=True,  # Change this to change color of text within the navbar (False for light text)
#     )
#
#     return navbar
