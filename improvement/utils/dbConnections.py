import json
import mariadb

def get_db_connection():
    with open('JSON/databaseDetails.json', 'r') as file:
        config = json.load(file)
        conn = mariadb.connect(
          user=config['user'],
          password=config['password'],
          host=config['host'],
          port=config['port'],
          database=config['database']
    )
    return conn