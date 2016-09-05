from urllib import parse
from flask import Flask, json, request, redirect

from .database import db
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


@server.route('/oauth2/token')
def oauth2_token():
    return json.dumps({
        'access_token': generate_token(),
        'client_id': request.args['client_id'],
        'expires_in': 21600,
        'refresh_token': generate_token(),
        'token_type': 'Bearer',
        'user_id': db['user'].user_id,
    })
