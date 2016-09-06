from urllib import parse
from flask import Flask, json, request, redirect, abort

from .database import db
from .datatypes import generate_token


server = Flask('monzo-api-stub')


@server.after_request
def access_control_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Authorization'
    return response


@server.route('/')
def root():
    state = request.args['state']
    redirect_uri = request.args['redirect_uri']
    code = generate_token()

    uri = parse.urlparse(redirect_uri)
    query = parse.parse_qsl(uri.query) + [('state', state), ('code', code)]
    uri = uri._replace(query=parse.urlencode(query))

    return redirect(parse.urlunparse(uri))


@server.route('/oauth2/token/')
def oauth2_token():
    return json.dumps({
        'access_token': generate_token(),
        'client_id': request.args['client_id'],
        'expires_in': 21600,
        'refresh_token': generate_token(),
        'token_type': 'Bearer',
        'user_id': db['user'].user_id,
    })


@server.route('/ping/whoami/')
def whoami():
    return json.dumps({
        'authenticated': True,
        'client_id': generate_token(),
        'user_id': db['user'].user_id,
    })


@server.route('/accounts/')
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


@server.route('/balance/')
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


@server.route('/transactions/<transaction_id>/')
def transaction(transaction_id):
    # Search all the accounts for the matching transaction
    transaction = None
    for _, transactions in db['transactions'].items():
        transaction = transactions.get(transaction_id)
        if transaction:
            break

    if not transaction:
        abort(404)

    expand_merchant = request.args.get('expand[]') == 'merchant'

    return json.dumps({
        'transaction': transaction_dict(transaction, expand_merchant),
    })


@server.route('/transactions/')
def transactions():
    account_id = request.args['account_id']

    try:
        transactions = db['transactions'][account_id]
    except KeyError:
        abort(400)

    expand_merchant = request.args.get('expand[]') == 'merchant'

    return json.dumps({
        'transactions': [
            transaction_dict(t, expand_merchant) for t in transactions.values()
        ],
    })


def transaction_dict(t, expand_merchant):
    if expand_merchant:
        merchant = merchant_dict(t.merchant)
    else:
        merchant = t.merchant.merchant_id

    return {
        'account_balance': t.account_balance,
        'amount': t.amount,
        'created': rfc3339(t.created),
        'currency': t.currency,
        'description': t.description,
        'id': t.transaction_id,
        'merchant': merchant,
        'metadata': t.metadata,
        'notes': t.notes,
        'is_load': t.is_load,
        'settled': rfc3339(t.settled),
    }


def merchant_dict(m):
    return {
        'address': {
            'address': m.address.address,
            'city': m.address.city,
            'country': m.address.country,
            'latitude': float(m.address.latitude),
            'longitude': float(m.address.longitude),
            'postcode': m.address.postcode,
            'region': m.address.region,
        },
        'created': rfc3339(m.created),
        'group_id': m.merchant_group_id,
        'id': m.merchant_id,
        'logo': m.logo,
        'emoji': m.emoji,
        'name': m.name,
        'category': m.category,
    }


def rfc3339(d):
    if d is None:
        return ''
    return d.strftime('%Y-%m-%dT%H:%M:%SZ')
