from flask import flask

app = Flask(__name__)

from general.general import general_bp

app.register_blueprint(general_bp url_prefix='/')

if __name__ == '__main__':
    debug = True
    