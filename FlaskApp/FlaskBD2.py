from flask import Flask, request
from flask_bootstrap import Bootstrap
from flaskext.mysql import MySQL
from app.DbConnector import DbConnector
from app.HtmlProvider import HtmlProvider
from app.RequestReader import RequestReader
from app.CurrentUser import CurrentUser


flask = Flask(__name__)
Bootstrap(flask)
flask.config['MYSQL_DATABASE_USER'] = 'bd2'
flask.config['MYSQL_DATABASE_PASSWORD'] = 'bd2'
flask.config['MYSQL_DATABASE_DB'] = 'bd2'
flask.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql = MySQL()
mysql.init_app(flask)
connector = DbConnector(mysql)
provider = HtmlProvider()
reader = RequestReader()
user = CurrentUser()


@flask.route('/', methods=['GET', 'POST'])
def main():
    global user
    if request.method == 'POST':
        login_data = reader.read_from_index(request.form)
        client = connector.login_client(login_data)
        if client:
            user = CurrentUser(client[0], True, False, False)
        else:
            worker = connector.login_worker(login_data)
            if worker:
                user = CurrentUser(worker[0], False, True, False)
            elif request.form['inputLogin'] == 'admin' and request.form['inputHaslo'] == 'admin':
                user = CurrentUser('Admin', False, False, True)
            else:
                user = CurrentUser()
    return provider.index(user)


@flask.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'POST':
        connector.add_product(reader.read_from_products(request.form))
    return provider.products(user, connector.all_products())


@flask.route('/clients', methods=['GET', 'POST'])
def clients():
    if request.method == 'POST':
        connector.add_client(reader.read_from_clients(request.form))
    return provider.clients(user, connector.all_clients())


@flask.route('/workers', methods=['GET', 'POST'])
def workers():
    if request.method == 'POST':
        connector.add_worker(reader.read_from_workers(request.form))
    return provider.workers(user, connector.all_workers())


@flask.route('/suppliers', methods=['GET', 'POST'])
def suppliers():
    if request.method == 'POST':
        connector.add_supplier(reader.read_from_suppliers(request.form))
    return provider.suppliers(user, connector.all_suppliers())


@flask.route('/orders', methods=['GET', 'POST'])
def orders():
    if request.method == 'POST':
        connector.add_order(reader.read_from_orders(request.form))
    return provider.orders(user, connector.all_orders())


if __name__ == '__main__':
    flask.run()
