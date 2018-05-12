"""A simple web server that accepts POSTS containing a list of feed urls,
and returns the titles of those feeds.
"""

import eventlet
import pprint

printf = pprint.PrettyPrinter(indent=4).pprint

# the pool provides a safety limit on our concurrency


GET = "GET"
POST = "POST"
PUT = "PUT"
DELETE = "DELETE"
HEAD = "HEAD"


class HandlerWSGI(object):

    def __init__(self, host, port=10618):
        self.host = host
        self.port = port
        self.rules = {}  # url_mapping format : {"/": (func,"method":"GET",...),"/xxx/":(...) ...}

    def add_url_rule(self, url, func, **options):
        options.setdefault("methods", "GET")

        if self.rules.has_key(url):
            raise AssertionError("Function mapping is overwriting an existing endpoint : {0}".format(func.__name__))

        self.rules[url] = (func, options)
        print(self.rules)

    def route(self, url, **options):
        def deco(func):
            self.add_url_rule(url, func, **options)
            return func

        return deco

    def _split_query_string(self, query_string):
        '''
        '''
        output_dict = {}
        for group in query_string.split("&"):
            parms = group.split("=")
            output_dict[parms[0]] = parms[1]

        return output_dict

    def __call__(self, environ, start_response):
        print(environ)

        urlPath = environ['PATH_INFO']
        method = environ['REQUEST_METHOD'] or GET
        wsgiInput = environ['wsgi.input']  # it is a eventlet.wsgi.Input Object

        # formating the dict for query_strings
        query_string = self._split_query_string(environ["QUERY_STRING"]) if environ.has_key("QUERY_STRING") else None

        # verify the avalibility of the URL and the correction on the request method
        if urlPath not in self.rules:
            start_response('404 NOT FOUND', [('Content-type', 'text/plain')])
            return []

        endpoint = self.rules[urlPath]
        if method not in endpoint[1]['methods']:
            start_response('405 Method Not Allowed', [('Content-type', 'text/plain')])
            return []

        func = endpoint[0]

        request_body = wsgiInput.read()
        print("request body : " + request_body)  # check request body
        printf("start_response detail --> : {0}".format(start_response.__dict__))
        response = func(environ=environ,start_response=start_response)  # All you want could be found in environ

        return response

    def run(self):
        from eventlet import wsgi
	# the minimun_chunk_size help identity the transimition chunk size , which is very helpful in large file delivery
        wsgi.server(eventlet.listen((self.host, self.port)),self, minimum_chunk_size=2048*2048)


if __name__ == '__main__':
    pass
