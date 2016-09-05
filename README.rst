monzo-api-stub
==============

Stub API for Monzo.

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
