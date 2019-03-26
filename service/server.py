from flask import (Flask,
                   request,
                   Response)
import requests
application = Flask(__name__)


@application.route('/', defaults={'path': ''})
@application.route('/<path:path>',
                   methods=['GET',
                            'HEAD',
                            'POST',
                            'PUT',
                            'DELETE',
                            'CONNECT',
                            'OPTIONS',
                            'TRACE',
                            'PATCH'])
def route_forwarding(path):
    forward_path = ('http://{}/{}')
    host = 'browser-client'
    forward_path = forward_path.format(host, path)
    forward_response = requests.request(
        method=request.method,
        url=forward_path,
        headers={key: value
                 for (key, value) in request.headers
                 if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)
    return Response(forward_response.content,
                    forward_response.status_code,
                    headers=forward_response.raw.headers.items())
