'''
NBA Game Predictor application
'''

from flask import Flask

def create_app():
    '''
    Create Flask app instance
    '''
    app = Flask(__name__)

    from .views import main
    app.register_blueprint(main)

    return app
