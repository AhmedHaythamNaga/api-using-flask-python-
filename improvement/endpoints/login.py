from flask import Blueprint, request, session, jsonify, render_template
from utils.dbConnections import get_db_connection
import sqlite3

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            email = request.form.get('email')
            password = request.form.get('password')

            if not email or not password:
                raise ValueError("Email and password are required")

            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("SELECT id FROM users WHERE email=? AND password=?", (email, password))
            user = cur.fetchone()

            if user:
                session['user_id'] = user[0]
                return jsonify({'message': 'Login successful'}), 200

            else:
                raise ValueError("Invalid email or password")

        except ValueError as ve:
            return jsonify({'error': str(ve)}), 400
        except sqlite3.Error as e:
            return jsonify({'error': 'Database error: ' + str(e)}), 500
        except Exception as e:
            return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500
    else:
        return render_template('login.html')
