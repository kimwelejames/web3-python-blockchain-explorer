from flask import Flask
from app.routes import main

def create_app():
    app = Flask(__name__)

    print("Static folder :", app.static_folder)
    print("Template folder:", app.template_folder)
    print("Root path      :", app.root_path)

    app.register_blueprint(main)

    return app