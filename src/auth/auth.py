from flask import Blueprint, render_template

auth_bp = Blueprint('auth_bp', __name__, template_folder="templates/auth", static_folder="static", static_url_path="assets")

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

