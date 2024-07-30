from flask import Blueprint, request, jsonify
import mariadb
from utils.dbConnections import get_db_connection
from utils.validations import is_email_unique, validate_phone_number, is_phone_number_unique

add_contacts_blueprint = Blueprint('add_contacts', __name__)


@add_contacts_blueprint.route('/add', methods=['GET', 'POST'])
def add_contact():
    try:
        if request.method == 'POST':
            name = request.form.get('full_name')
            email = request.form.get('email')
            phone = request.form.get('phone_number')

            if not name or not phone:
                raise ValueError("Name and phone are required")

            if email and not is_email_unique(email):
                raise ValueError("Email is already in use")

            if not validate_phone_number(phone):
                raise ValueError("Invalid phone number format")

            if not is_phone_number_unique(phone):
                raise ValueError("Phone number is already in use")

            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
            conn.commit()
            return jsonify({'message': 'Contact added successfully'}), 201
        else:
            return jsonify({'error': 'Invalid request method'}), 405
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except mariadb.Error as e:
        return jsonify({'error': 'Database error: ' + str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500
