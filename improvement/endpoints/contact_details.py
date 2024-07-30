from flask import Blueprint, request, jsonify
import mariadb
from utils.dbConnections import get_db_connection
from utils.validations import is_email_unique, validate_phone_number, is_phone_number_unique

contact_details_blueprint = Blueprint('contact_details', __name__)


@contact_details_blueprint.route('/details/<int:contact_id>', methods=['GET', 'POST'])
def contact_details(contact_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        if request.method == 'POST':
            name = request.form.get('full_name')
            email = request.form.get('email')
            phone = request.form.get('phone_number')

            if not name or not phone:
                raise ValueError("Name and phone are required")

            if email and not is_email_unique(email):
                cur.execute("SELECT id FROM contacts WHERE email=? AND id!=?", (email, contact_id))
                if cur.fetchone():
                    raise ValueError("Email is already in use")

            if not validate_phone_number(phone):
                raise ValueError("Invalid phone number format")

            cur.execute("SELECT id FROM contacts WHERE phone=? AND id!=?", (phone, contact_id))
            if cur.fetchone():
                raise ValueError("Phone number is already in use")

            cur.execute("UPDATE contacts SET name=?, email=?, phone=? WHERE id=?", (name, email, phone, contact_id))
            conn.commit()
            return jsonify({'message': 'Contact updated successfully'}), 200

        cur.execute("SELECT * FROM contacts WHERE id=?", (contact_id,))
        contact = cur.fetchone()
        return jsonify({'contact': {
            'id': contact[0],
            'name': contact[1],
            'email': contact[2],
            'phone': contact[3]
        }}), 200
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except mariadb.Error as e:
        return jsonify({'error': 'Database error: ' + str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500
