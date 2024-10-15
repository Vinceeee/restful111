from eventlet import wsgi
import eventlet

def hello_world(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Hello, World!\r\n']

def info(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Hello, info!\r\n']


wsgi.server(eventlet.listen(('0.0.0.0', 8090)), hello_world)
