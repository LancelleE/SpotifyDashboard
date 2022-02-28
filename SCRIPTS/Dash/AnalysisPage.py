from Components.Navbar import create_navbar
from dash import html

nav = create_navbar()

header1 = html.H5('Welcome to page 2 pouet pouet!')


def create_page_2():
    layout = html.Div([
        nav,
        header1,
    ])
    return layout
