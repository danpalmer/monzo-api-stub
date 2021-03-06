monzo-api-stub
==============

Stub API for Monzo.

Note about Monzo API deprecation
--------------------------------

The Monzo API is essentially deprecated at this point. It has not been in active development since early 2016 (as far as I can tell), and will likely not be worked on until mid-2018, as the UK are introducing new regulations for open banking infrastructure which will influence the future of Monzo's API. I'll happily accept PRs to this repo, but given the state of the API's development I have ceased working with the Monzo API myself so will not be maintaining this until API development picks up again.

Installation
------------

The package is available on PyPI::

    $ pip install monzo-api-stub

Usage
-----

To run a server::

    $ monzo-api

You can parse optional arguments to change the behaviour::

    $ monzo-api --help
    Usage: monzo-api [OPTIONS]

      Stub Monzo API

    Options:
      --host TEXT             Address to bind to.
      --port INTEGER          Port for the HTTP server.
      --num-accounts INTEGER  Number of accounts to give the user
      --currency TEXT         Currency to use, pass "random" to use random
                              currencies
      --help                  Show this message and exit.

Note: This is not guaranteed to be API compatible. It is a best-effort attempt
to provide a useful tool for developers building for the Monzo API.


Features
--------

- OAuth flow with immediate redirect, no need to enter an email address.
- Test with pre-defined or random currencies.
- Test as a user with multiple accounts.


Completeness
------------

Since this is a stub API, most "business logic" on the server side isn't
implemented, and likely won't be.

This should however be considered a work in progress, and any PRs that bring
responses/endpoints closer to those of the real API, or any that add entirely
missing endpoints, are very welcome.

Things that are missing:

- OAuth exchange is fake - I'd like to add this in a basic way to make it easier
  to test the OAuth flow.

- No auth headers required - Would be good to have a basic (optional?) auth
  check.

- Verbose request logging - to help see what your client application is sending.

- Loading custom data - to allow testing of specific cases that your app
  wants to handle.

- Webhooks.
