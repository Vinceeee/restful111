"""A simple web server that accepts POSTS containing a list of feed urls,
and returns the titles of those feeds.
"""
import eventlet
import action

# the pool provides a safety limit on our concurrency
pool = eventlet.GreenPool(5)


GET = "GET"
POST = "POST"
PUT = "PUT"
DELETE = "DELETE"
HEAD = "HEAD"

# register the url mapping here 
# endpoint handling need to be imported in advance
URL_MAPPING = {
    u"/": (action.do_sth1,"GET"),
    u"/postOnly":(action.do_sth2,"POST"),
    u"/getOrpost":(action.do_sth3,["GET","POST"])
}

def split_query_string(query_string):
    '''
    '''
    output_dict = {}
    for group in query_string.split("&"):
        parms =  group.split("=")
        output_dict[parms[0]] = parms[1]

    return output_dict

def app(environ, start_response):

    print(environ)

    urlPath = environ['PATH_INFO']
    method = environ['REQUEST_METHOD']
    wsgiInput = environ['wsgi.input'] # it is a eventlet.wsgi.Input Object

    # formating the dict for query_strings
    query_string = split_query_string(environ["QUERY_STRING"]) if environ.has_key("QUERY_STRING") else None

    action = None
    allow_method = None

    # verify the avalibility of the URL and the correction on the request method
    if urlPath not in URL_MAPPING.keys():
        start_response('404 NOT FOUND', [('Content-type', 'text/plain')])
        return []
    else:
        allow_method = URL_MAPPING[urlPath][1] 
        if method not in allow_method:
            start_response('405 Method Not Allowed', [('Content-type', 'text/plain')])
            return []
        action = URL_MAPPING[urlPath][0]

    # the pile collects the result of a concurrent operation 
    pile = eventlet.GreenPile(pool)
    request_body = wsgiInput.read()
    print("request body : "+request_body) # check request body
    pile.spawn(action, query_string=query_string ,request_body=request_body) # use keyword arguement while 
    # since the pile is an iterator over the results,
    # you can use it in all sorts of great Pythonic ways
    response = pile
    start_response('200 OK', [('Content-type', 'text/plain')])
    return response


if __name__ == '__main__':
    from eventlet import wsgi
    IP = "localhost"
    PORT = 9010
    WSGIAPP = app   # actually , all the WSGI app implementation is similar with this format
    wsgi.server(eventlet.listen((IP,PORT)) , WSGIAPP)