#!/usr/bin/python3
"""
AirBnB_clone_v3 API
"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ returns status """
    return jsonify({"status": "OK"})
