class HtmlButton:
    def __init__(self, text, link=None):
        self.text = text
        self.link = link


class HtmlTable:
    def __init__(self, headers, content):
        self.headers = headers
        self.content = content


class HtmlInputs:
    def __init__(self):
        pass

    def nazwa(self):
        return {'label': 'Nazwa', 'type': 'text'}

    def cena(self):
        return {'label': 'Cena', 'type': 'number', 'step': 0.01}

    def vat(self):
        return {'label': 'VAT', 'type': 'number', 'max': 100}

    def ilosc(self):
        return {'label': 'Ilosc', 'type': 'number'}

    def kategoria(self):
        return {'label': 'Kategoria', 'type': 'text'}

    def dostawca(self):
        return {'label': 'Dostawca', 'type': 'text'}

    def telefon(self):
        return {'label': 'Telefon', 'type': 'tel'}

    def email(self):
        return {'label': 'EMail', 'type': 'email'}

    def miasto(self):
        return {'label': 'Miasto', 'type': 'text'}

    def ulica(self):
        return {'label': 'Ulica', 'type': 'text'}

    def nr_budynku(self):
        return {'label': 'Nr budynku', 'type': 'number'}

    def nr_lokalu(self):
        return {'label': 'Nr lokalu', 'type': 'number'}

    def poczta(self):
        return {'label': 'Poczta', 'type': 'text'}

    def kod_pocztowy(self):
        return {'label': 'Kod pocztowy', 'type': 'text'}

    def imie(self):
        return {'label': 'Imie', 'type': 'text'}

    def nazwisko(self):
        return {'label': 'Nazwisko', 'type': 'text'}

    def login(self):
        return {'label': 'Login', 'type': 'text'}

    def haslo(self):
        return {'label': 'Haslo', 'type': 'password'}

    def imie_klienta(self):
        return {'label': 'Imie klienta', 'type': 'text'}

    def nazwisko_klienta(self):
        return {'label': 'Nazwisko klienta', 'type': 'text'}

    def imie_pracownika(self):
        return {'label': 'Imie pracownika', 'type': 'text'}

    def nazwisko_pracownika(self):
        return {'label': 'Nazwisko pracownika', 'type': 'text'}

    def produkt(self):
        return {'label': 'Produkt', 'type': 'text'}

    def data_zlozenia_zamowienia(self):
        return {'label': 'Data zlozenia zamowienia', 'type': 'date'}

    def data_realizacji_zamowienia(self):
        return {'label': 'Data realizacji zamowienia', 'type': 'date'}

    def stanowisko(self):
        return {'label': 'Stanowisko', 'type': 'text'}

    def data_zatrudenienia(self):
        return {'label': 'Data zatrudnienia', 'type': 'date'}
