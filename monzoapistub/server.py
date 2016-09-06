from urllib import parse
from flask import Flask, json, request, redirect, abort

from .database import db
from .datatypes import generate_token


server = Flask('monzo-api-stub')


@server.route('/')
def root():
    state = request.args['state']
    redirect_uri = request.args['redirect_uri']
    code = generate_token()

    uri = parse.urlparse(redirect_uri)
    query = parse.parse_qsl(uri.query) + [('state', state), ('code', code)]
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


@server.route('/ping/whoami')
def whoami():
    return json.dumps({
        'authenticated': True,
        'client_id': generate_token(),
        'user_id': db['user'].user_id,
    })


@server.route('/accounts')
def accounts():
    return json.dumps({
        'accounts': [
            {
                'id': account.account_id,
                'description': account.description,
                'created': rfc3339(account.created),
            }
            for account in db['accounts'].values()
        ]
    })


@server.route('/balance')
def balance():
    account_id = request.args['account_id']

    try:
        account = db['accounts'][account_id]
    except KeyError:
        abort(400)

    return json.dumps({
        'balance': account.balance,
        'spend_today': account.spend_today,
        'currency': account.currency,
    })



def rfc3339(d):
    if d is None:
        return ''
    return d.strftime('%Y-%m-%dT%H:%M:%SZ')
