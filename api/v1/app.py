#!/usr/bin/python3
""" Module for start the API """

from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_appcontext(self):
    """call method to close"""
    storage.close()


@app.errorhandler(404)
def page_not_found(err):
    """error handler"""
    err_dict = {"error": "Not found"}
    return jsonify(err_dict), 404


if __name__ == "__main__":
    host_env = getenv('HBNB_API_HOST')
    port_env = getenv('HBNB_API_PORT')
    if not host_env:
        host = "0.0.0.0"
    if not port_env:
        port = 5000
    app.run(host=host_env, port=int(port_env), threaded=True)
