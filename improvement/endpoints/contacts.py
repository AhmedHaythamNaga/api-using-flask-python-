from flask import Blueprint, jsonify
import mariadb
from utils.dbConnections import get_db_connection

contacts_blueprint = Blueprint('contacts', __name__)

@contacts_blueprint.route('/list')
def contact_list():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, name, email, phone FROM contacts")
        contacts = cur.fetchall()

        contacts_list = []
        for contact in contacts:
            contacts_list.append({
                'id': contact[0],
                'name': contact[1],
                'email': contact[2],
                'phone': contact[3]
            })

        return jsonify(contacts_list), 200

    except mariadb.Error as e:
        return jsonify({'error': 'Database error: ' + str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500
