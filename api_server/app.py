from wsgiref.simple_server import make_server
from pyramid.config import Configurator
import pyramid

import views

import json

if __name__ == '__main__':
    settings = json.loads(open('settings.json').read())

    config = Configurator(settings=settings)
    config.add_renderer(None, pyramid.renderers.JSON())
    config.include('routes')
    config.include('models')
    config.scan(views)

    app = config.make_wsgi_app()
    server = make_server(settings['host'], settings['port'], app)
    server.serve_forever()
