from flask import Flask
from flaskext.mysql import MySQL
from app.DbConnector import DbConnector

flask = Flask(__name__)
flask.config['MYSQL_DATABASE_USER'] = 'bd2'
flask.config['MYSQL_DATABASE_PASSWORD'] = 'bd2'
flask.config['MYSQL_DATABASE_DB'] = 'bd2'
flask.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql = MySQL()
mysql.init_app(flask)
connector = DbConnector(mysql)


@flask.route('/')
def main():
    lol = '<br />'
    for i in connector.all_products():
        for j in i:
            lol = '{old}{new}<br />'.format(old=lol, new=str(j))
    return lol


if __name__ == '__main__':
    flask.run()
