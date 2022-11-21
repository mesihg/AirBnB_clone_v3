#!/usr/bin/python3
"""
AirBnB_clone_v3 API
"""

from os import getenv
from flask import Flask
from models import storage
from app_views import api.v1.views
app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    """handle resource cleanup"""
    storage.close()


if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", '0.0.0.0')
    port = os.getenv("HBNB_API_PORT", '5000')

    app.run(host=host, port=port)
