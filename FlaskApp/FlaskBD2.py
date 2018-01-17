from flask import Flask, request
from flask_bootstrap import Bootstrap
from flaskext.mysql import MySQL
from app.DbConnector import DbConnector
from app.HtmlProvider import HtmlProvider
from app.RequestReader import RequestReader


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


@flask.route('/')
def main():
    return provider.index()


@flask.route('/test', methods=['GET', 'POST'])
def test():
    return provider.test()


@flask.route('/teste', methods=['GET', 'POST'])
def teste():
    return provider.teste()


@flask.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'GET':
        return provider.products(connector.all_products())
    elif request.method == 'POST':
        connector.add_product(reader.read_from_products(request.form))
        return provider.products(connector.all_products())


@flask.route('/clients', methods=['GET', 'POST'])
def clients():
    if request.method == 'GET':
        return provider.clients(connector.all_clients())
    elif request.method == 'POST':
        connector.add_client(reader.read_from_clients(request.form))
        return provider.clients(connector.all_clients())


@flask.route('/workers', methods=['GET', 'POST'])
def workers():
    if request.method == 'GET':
        return provider.workers(connector.all_workers())
    elif request.method == 'POST':
        connector.add_worker(reader.read_from_workers(request.form))
        return provider.workers(connector.all_workers())


@flask.route('/suppliers', methods=['GET', 'POST'])
def suppliers():
    if request.method == 'GET':
        return provider.suppliers(connector.all_suppliers())
    elif request.method == 'POST':
        connector.add_supplier(reader.read_from_suppliers(request.form))
        return provider.suppliers(connector.all_suppliers())


@flask.route('/orders', methods=['GET', 'POST'])
def orders():
    if request.method == 'GET':
        return provider.orders(connector.all_orders())
    elif request.method == 'POST':
        connector.add_order(reader.read_from_orders(request.form))
        return provider.orders(connector.all_orders())


if __name__ == '__main__':
    flask.run()
