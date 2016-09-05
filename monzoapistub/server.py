from urllib import parse
from flask import Flask, json, request, redirect

from .datatypes import generate_token


server = Flask('monzo-api-stub')


@server.route('/')
def root():
    state = request.args['state']
    redirect_uri = request.args['redirect_uri']
    code = generate_token()

    uri = parse.urlparse(redirect_uri)
    query = parse.parse_qsl(uri.query)
    query.append(('state', state))
    query.append(('code', code))
    uri = uri._replace(query=parse.urlencode(query))

    return redirect(parse.urlunparse(uri))
