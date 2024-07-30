from flask import session, redirect, url_for, flash, jsonify

from app import app
from utils.dbConnections import get_db_connection


@app.route('/contacts/remove/<int:contact_id>', methods=['POST'])
def remove_contact(contact_id):
    if 'user_id' not in session:
        return redirect(url_for('login.login'))

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
        conn.commit()
        conn.close()
        flash('Contact successfully removed', 'success')
        return jsonify({'message': 'Contact successfully removed'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
