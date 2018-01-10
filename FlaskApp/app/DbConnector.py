class DbConnector:
    def __init__(self, mysql):
        self._mysql = mysql
        self._cursor = mysql.connect().cursor()

    def take_one(self, call):
        self._cursor.execute(call)
        data = self._cursor.fetchone()
        return data

    def take_all(self, call):
        self._cursor.execute(call)
        data = self._cursor.fetchall()
        return data

    def all_suppliers(self):
        return self.take_all("SELECT * from widok_dostawcy")

    def all_clients(self):
        return self.take_all("SELECT * from widok_klienci")

    def all_workers(self):
        return self.take_all("SELECT * from widok_pracownicy")

    def all_products(self):
        return self.take_all("SELECT * from widok_produkty")

    def all_orders(self):
        return self.take_all("SELECT * from widok_zamowienia;")

