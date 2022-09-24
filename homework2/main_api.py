import flask

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
        flask.abort(415)
    if not flask.request or not 'key' in flask.request.json or not 'value' in flask.request.json:
        flask.abort(400)
    values[flask.request.json['key']] = flask.request.json['value']
    return flask.Response()


@app.route('/get/<string:key>', methods=['GET'])
def app_get(key):
    if key not in values:
        flask.abort(404)
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
        flask.abort(415)
    if not flask.request or not 'dividend' in flask.request.json or not 'divider' in flask.request.json:
        flask.abort(400)
    if flask.request.json['divider'] == 0:
        flask.abort(400)
    response = flask.Response(str(flask.request.json['dividend'] / flask.request.json['divider']))
    response.headers['Content-Type'] = 'text/plain'
    return response


@app.errorhandler(400)
def not_found(error):
    return flask.make_response('', 400)


@app.errorhandler(404)
def not_found(error):
    return flask.make_response('', 404)


@app.errorhandler(405)
def not_found(error):
    return flask.make_response('', 405)


@app.errorhandler(415)
def not_found(error):
    return flask.make_response('', 415)


if __name__ == '__main__':
    app.run()
