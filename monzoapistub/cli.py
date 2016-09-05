import click

from . import database
from .server import server

@click.command()
@click.option('--host', default='127.0.0.1', help='Address to bind to.')
@click.option('--port', default=3000, help='Port for the HTTP server.')
@click.option('--num-accounts', default=1,
    help='Number of accounts to give the user')
@click.option('--currency', default='GBP',
    help='Currency to use, pass "random" to use random currencies')
def cli(host, port, num_accounts, currency):
    """Stub Monzo API"""
    database.init(num_accounts, currency)
    server.run(host=host, port=port)

if __name__ == '__main__':
    cli()
