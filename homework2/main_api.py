import flask
from werkzeug.exceptions import HTTPException

app = flask.Flask(__name__)
values = dict()


@app.route('/hello', methods=['GET'])
def hello():
    response = flask.Response("HSE One Love!")
    response.headers['Content-Type'] = 'text/plain'
    return response


@app.route('/set', methods=['POST'])
def app_set():
    if not 'Content-Type' in flask.request.headers or flask.request.headers['Content-Type'] != 'application/json':
        return flask.Response(status=415)
    if not flask.request or not 'key' in flask.request.json or not 'value' in flask.request.json:
        return flask.Response(status=400)
    values[flask.request.json['key']] = flask.request.json['value']
    return flask.Response()


@app.route('/get/<string:key>', methods=['GET'])
def app_get(key):
    if key not in values:
        return flask.Response(status=404)
    ans = {
        "key": key,
        "value": values[key]
    }
    return app.response_class(
        response=flask.json.dumps(ans),
        status=200,
        content_type="application/json"
    )


@app.route('/devide', methods=['POST'])
def devide():
    if not 'Content-Type' in flask.request.headers or flask.request.headers['Content-Type'] != 'application/json':
        return flask.Response(status=415)
    if not flask.request or not 'dividend' in flask.request.json or not 'divider' in flask.request.json:
        return flask.Response(status=400)
    if flask.request.json['divider'] == 0:
        return flask.Response(status=400)
    response = flask.Response(str(flask.request.json['dividend'] / flask.request.json['divider']))
    response.headers['Content-Type'] = 'text/plain'
    return response


@app.errorhandler(HTTPException)
def handle_exception(error):
    return flask.Response(status=405)


if __name__ == '__main__':
    app.run()
