from flask import Flask

app = Flask(__name__)

from general.general import general_bp
from auth.auth import auth_bp

app.register_blueprint(general_bp, url_prefix='/')
app.register_blueprint(auth_bp, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)