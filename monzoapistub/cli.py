import click

from . import database
from .server import server

@click.command()
@click.option('--host', default='127.0.0.1', help='Address to bind to.')
@click.option('--port', default=3000, help='Port for the HTTP server.')
def cli(host, port):
    """Stub Monzo API"""
    database.init()
    server.run(host=host, port=port)

if __name__ == '__main__':
    cli()
