#!/usr/bin/env python
"""A simple web server that accepts POSTS containing a list of feed urls,
and returns the titles of those feeds.
"""

import os
import eventlet
from eventlet.tpool import execute
from mylogger import getLocalFileLogger

# the pool provides a safety limit on our concurrency

GET = "GET"
POST = "POST"
PUT = "PUT"
DELETE = "DELETE"
HEAD = "HEAD"
PATCH = "PATCH"
OPTIONS = "OPTIONS"


class MyWSGI(object):
    def __init__(self,
                 host='127.0.0.1',
                 port=10620,
                 logger=getLocalFileLogger(),
                 pool=1000):
        self.host = host
        self.port = port
        #       self.logger = getSysLogger()
        self.logger = logger
        self.rules = {
        }  # url_mapping format : {"/": (func,"method":"GET",...),"/xxx/":(...) ...}
        os.environ['EVENTLET_THREADPOOL_SIZE'] = str(pool)

    def add_url_rule(self, url, func, **options):
        self.logger.info("Add url rule {0}".format(url))
        options.setdefault("methods", "GET")

        if url in self.rules:
            raise AssertionError(
                "Function mapping is overwriting an existing endpoint : {0}".
                format(func.__name__))

        self.rules[url] = (func, options)

    def route(self, url, **options):
        def deco(func):
            self.add_url_rule(url, func, **options)
            return func

        return deco

    def _split_query_string(self, query_string):
        output_dict = {}
        for group in query_string.split("&"):
            parms = group.split("=")
            output_dict[parms[0]] = parms[1]

        return output_dict

    def __call__(self, environ, start_response):
        self.logger.debug(environ)

        urlPath = environ['PATH_INFO']
        method = environ['REQUEST_METHOD'] or GET

        # formating the dict for query_strings
        if "QUERY_STRING" in environ and environ["QUERY_STRING"]:
            query_string = self._split_query_string(environ["QUERY_STRING"])

        # verify the avalibility of the URL and the correction on the request method
        if urlPath not in self.rules:
            start_response('404 NOT FOUND', [('Content-type', 'text/plain')])
            return []

        endpoint = self.rules[urlPath]
        if method not in endpoint[1]['methods']:
            start_response('405 Method Not Allowed',
                           [('Content-type', 'text/plain')])
            return []

        func = endpoint[0]

        #       request_body = wsgiInput.read()
        response = execute(
            func, environ=environ, start_response=start_response
        )  # All you want could be found in environ

        return response

    def run(self):
        from eventlet import wsgi
        # the minimun_chunk_size help identity the transimition chunk size , which is very helpful in large file delivery
        self.logger.info(
            "if you see this line in the log , that means this one is not a release version !"
        )
        wsgi.server(
            eventlet.listen((self.host, self.port)),
            self,
            log=self.logger,
            minimum_chunk_size=2048 * 2048)


if __name__ == '__main__':
    app = MyWSGI()
    app.run()
