from flask import Flask
from listapp.views.index import bp as index_bp
# from listapp.views.createnote import bp as createnote_bp
from listapp.model import model

# def create_app(debug=False):
#     app = Flask(__name__)
#     app.register_blueprint(index_bp)
#     # app.register_module(model)
#
#     return app

app = Flask(__name__)

app.register_blueprint(index_bp)
# app.register_blueprint(createnote_bp)
