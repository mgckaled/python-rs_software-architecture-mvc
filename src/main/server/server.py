from flask import Flask
from flask_cors import CORS

from src.main.routes.pets_routes import pet_route_db
from src.models.sqlite.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

app = Flask(import_name=__name__)
CORS(app=app)

app.register_blueprint(blueprint=pet_route_db)
