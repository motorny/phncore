#!/usr/bin/env python
import falcon
import json
from wsgiref import simple_server


class StatusResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        server_status = {'PHNcore': 'OK'}
        resp.body = json.dumps(server_status)


app = falcon.API()
status_rsrc = StatusResource()


app.add_route('/status', status_rsrc)

if __name__ == '__main__':
    port = 8200
    httpd = simple_server.make_server('127.0.0.1', port, app)
    print('Server listening on port: {0}'.format(port))
    print('For shutdown press Ctrl+C and then send a request')
    httpd.serve_forever()
