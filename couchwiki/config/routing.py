"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from pylons import config
from routes import Mapper

def make_map():
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = False

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('/error/{action}', controller='error')
    map.connect('/error/{action}/{id}', controller='error')

    # CUSTOM ROUTES HERE

    map.connect('/{controller}/{action}')
    map.connect('/{controller}/{action}/{id}')


#   mine
    map.redirect('/', '/pages')

    map.connect('/pages', controller='pages', action='index',
        conditions=dict(method=['GET']))
    map.connect('/pages', controller='pages', action='create_update',
        conditions=dict(method=['POST'])),
    map.connect('/pages/{page_id}/edit',
        conditions=dict(method=['GET']), controller='pages', action='edit')
    map.connect('/pages/{page_id}/create',
        conditions=dict(method=['GET']), controller='pages', action='create')
    map.connect('/pages/{page_id}',
        conditions=dict(method=['GET']), controller='pages', action='view')
    map.connect('/pages/{page_id}',
        conditions=dict(method=['POST']), controller='pages', action='create_update')

    return map
