from .HtmlElements import *
from flask import render_template


class HtmlProvider:
    def __init__(self):
        self.__all_buttons = [HtmlButton('index', '/'),
                              HtmlButton('produkty', 'products'),
                              HtmlButton('klienci', 'clients'),
                              HtmlButton('pracownicy', 'workers'),
                              HtmlButton('dostawcy', 'suppliers'),
                              HtmlButton('zamowienia', 'orders')]
        self.__in = HtmlInputs()
        pass

    def __render(self, **kwargs):
        buttons = []
        content = ''
        tables = []
        inputs = []
        if kwargs is not None:
            if 'buttons' in kwargs:
                buttons = kwargs['buttons']
            if 'content' in kwargs:
                content = kwargs['content']
            if 'tables' in kwargs:
                tables = kwargs['tables']
            if 'inputs' in kwargs:
                inputs = kwargs['inputs']
        return render_template('layout.html',
                               buttons=buttons,
                               body_content=content,
                               tables=tables,
                               inputs=inputs)

    def index(self):
        return self.__render(buttons=self.__all_buttons,
                             content='To jest mój projekt z BD2.')

    def products(self, table_content):
        tables = [HtmlTable(['#', 'nazwa', 'kategoria', 'cena netto', 'vat', 'cena brutto', 'ilość', 'dostawca'], table_content)]
        inputs = [self.__in.nazwa(),
                  self.__in.cena(),
                  self.__in.vat(),
                  self.__in.ilosc(),
                  self.__in.kategoria(),
                  self.__in.dostawca()]
        return self.__render(buttons=self.__all_buttons,
                             content='Produkty:',
                             tables=tables,
                             inputs=inputs)

    def clients(self, table_content):
        tables = [HtmlTable(['#', 'login', 'haslo', 'imie', 'nazwisko', 'miasto', 'ulica', 'nr budynku', 'nr lokalu', 'poczta', 'kod', 'nr telefonu', "email"], table_content)]
        inputs = [self.__in.imie(),
                  self.__in.nazwisko(),
                  self.__in.login(),
                  self.__in.haslo(),
                  self.__in.telefon(),
                  self.__in.email(),
                  self.__in.miasto(),
                  self.__in.ulica(),
                  self.__in.nr_budynku(),
                  self.__in.nr_lokalu(),
                  self.__in.poczta(),
                  self.__in.kod_pocztowy()]
        return self.__render(buttons=self.__all_buttons,
                             content='Klienci:',
                             tables=tables,
                             inputs=inputs)

    def workers(self, table_content):
        tables = [HtmlTable(['#', 'login', 'haslo', 'imie', 'nazwisko', 'stanowisko', 'data zatrudnienia', 'miasto', 'ulica', 'nr budynku', 'nr lokalu', 'poczta', 'kod', 'nr telefonu', "email"], table_content)]
        inputs = [self.__in.imie(),
                  self.__in.nazwisko(),
                  self.__in.login(),
                  self.__in.haslo(),
                  self.__in.telefon(),
                  self.__in.email(),
                  self.__in.miasto(),
                  self.__in.ulica(),
                  self.__in.nr_budynku(),
                  self.__in.nr_lokalu(),
                  self.__in.poczta(),
                  self.__in.kod_pocztowy(),
                  self.__in.stanowisko(),
                  self.__in.data_zatrudenienia()]
        return self.__render(buttons=self.__all_buttons,
                             content='Pracownicy:',
                             tables=tables,
                             inputs=inputs)

    def suppliers(self, table_content):
        tables = [HtmlTable(['#', 'nazwa', 'miasto', 'ulica', 'nr budynku', 'nr lokalu', 'poczta', 'kod', 'nr telefonu', "email"], table_content)]
        inputs = [self.__in.nazwa(),
                  self.__in.telefon(),
                  self.__in.email(),
                  self.__in.miasto(),
                  self.__in.ulica(),
                  self.__in.nr_budynku(),
                  self.__in.nr_lokalu(),
                  self.__in.poczta(),
                  self.__in.kod_pocztowy()]
        return self.__render(buttons=self.__all_buttons,
                             content='Dostawcy:',
                             tables=tables,
                             inputs=inputs)

    def orders(self, table_content):
        tables = [HtmlTable(['#', '#', 'imie klienta', 'nazwisko klienta', 'produkt', 'ilosc', 'cena', 'imie pracownika', 'nazwisko pracownika', 'data zlozenia zamowienia', "data realizacji zamowienia"], table_content)]
        inputs = [self.__in.imie_klienta(),
                  self.__in.nazwisko_klienta(),
                  self.__in.imie_pracownika(),
                  self.__in.nazwisko_pracownika(),
                  self.__in.produkt(),
                  self.__in.ilosc(),
                  self.__in.data_zlozenia_zamowienia(),
                  self.__in.data_realizacji_zamowienia()]
        return self.__render(buttons=self.__all_buttons,
                             content='Zamówienia:',
                             tables=tables,
                             inputs=inputs)
