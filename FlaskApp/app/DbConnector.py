class DbConnector:
    def __init__(self, mysql):
        self.__conn = mysql.connect()
        self.__cursor = self.__conn.cursor()

    def __take_one(self, call):
        self.__cursor.execute(call)
        return self.__cursor.fetchone()

    def __take_all(self, call):
        self.__cursor.execute(call)
        return self.__cursor.fetchall()

    def __call_procedure(self, procedure, values):
        self.__cursor.callproc(procedure, values)
        self.__conn.commit()

    def all_suppliers(self):
        return self.__take_all("SELECT * from widok_dostawcy")

    def all_clients(self):
        return self.__take_all("SELECT * from widok_klienci")

    def all_workers(self):
        return self.__take_all("SELECT * from widok_pracownicy")

    def all_products(self):
        return self.__take_all("SELECT * from widok_produkty")

    def all_orders(self):
        return self.__take_all("SELECT * from widok_zamowienia;")

    def add_product(self, values):
        self.__call_procedure('DODAJ_PRODUKT', values)

    def add_supplier(self, values):
        self.__call_procedure('DODAJ_DOSTAWCE', values)

    def add_client(self, values):
        self.__call_procedure('DODAJ_KLIENTA', values)

    def add_worker(self, values):
        self.__call_procedure('DODAJ_PRACOWNIKA', values)

    def add_order(self, values):
        self.__call_procedure('DODAJ_ZAMOWIENIE', values)