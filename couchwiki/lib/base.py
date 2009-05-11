"""The base Controller API

Provides the BaseController class for subclassing.
"""
from pylons.controllers import WSGIController
from pylons.templating import render_genshi as render
import couchwiki.lib.helpers as h
import couchdb.client

class BaseController(WSGIController):
    def _get_db(self):
        return couchdb.client.Database('http://localhost:5984/wiki')

    def __call__(self, environ, start_response):
        """Invoke the Controller"""
        # WSGIController.__call__ dispatches to the Controller method
        # the request is routed to. This routing information is
        # available in environ['pylons.routes_dict']
        return WSGIController.__call__(self, environ, start_response)
