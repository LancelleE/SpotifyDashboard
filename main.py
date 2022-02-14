from SCRIPTS.DataScripts.RecupHistory import import_all
from dash import Dash
import brotli

def main():
    streaming_history, library = import_all()
    app = Dash(__name__)


if __name__ == '__main__':
    main()
