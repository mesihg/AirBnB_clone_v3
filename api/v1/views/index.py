#!/usr/bin/python3
"""
AirBnB_clone_v3 Views
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    """ returns status """
    return jsonify({"status": "OK"})
