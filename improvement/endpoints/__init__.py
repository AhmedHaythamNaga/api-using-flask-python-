from flask import Flask, url_for


def create_app():
    app = Flask(__name__)
    app.secret_key = "b'8 xf9\x1e \xd7\xaf\xf6\xd0\xd8\x08\x9c/\xb2\xca\x11-+\xc6\xcf(\xdb\xb9\xf3P|'"

    from endpoints.login import login_blueprint
    from endpoints.add_contacts import add_contacts_blueprint
    from endpoints.contact_details import contact_details_blueprint
    from endpoints.contacts import contacts_blueprint

    app.register_blueprint(login_blueprint, url_prefix='/login')
    app.register_blueprint(add_contacts_blueprint, url_prefix='/contacts')
    app.register_blueprint(contact_details_blueprint, url_prefix='/contact_details')
    app.register_blueprint(contacts_blueprint, url_prefix='/contacts')

    @app.route('/routes', methods=['GET'])
    def list_routes():
        output = []
        for rule in app.url_map.iter_rules():
            options = {}
            for arg in rule.arguments:
                options[arg] = f"<{arg}>"

            methods = ','.join(rule.methods)
            url = url_for(rule.endpoint, **options)
            line = f"{rule.endpoint:50s} {methods:20s} {url}"
            output.append(line)

        return "<pre>" + "\n".join(output) + "</pre>"

    return app
