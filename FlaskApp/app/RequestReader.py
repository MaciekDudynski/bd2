class RequestReader:
    def __init__(self):
        pass

    def read_from_products(self, form):
        return [form['inputNazwa'],
                float(form['inputCena']),
                int(form['inputVAT']),
                int(form['inputIlosc']),
                form['inputKategoria'],
                form['inputDostawca']]

    def read_from_suppliers(self, form):
        return [form['inputNazwa'],
                form['inputTelefon'],
                form['inputEMail'],
                form['inputMiasto'],
                form['inputUlica'],
                int(form['inputNr budynku']),
                int(form['inputNr lokalu']),
                form['inputPoczta'],
                form['inputKod pocztowy']]

    def read_from_clients(self, form):
        return [form['inputImie'],
                form['inputNazwisko'],
                form['inputLogin'],
                form['inputHaslo'],
                form['inputTelefon'],
                form['inputEMail'],
                form['inputMiasto'],
                form['inputUlica'],
                int(form['inputNr budynku']),
                int(form['inputNr lokalu']),
                form['inputPoczta'],
                form['inputKod pocztowy']]

    def read_from_workers(self, form):
        return [form['inputImie'],
                form['inputNazwisko'],
                form['inputLogin'],
                form['inputHaslo'],
                form['inputTelefon'],
                form['inputEMail'],
                form['inputMiasto'],
                form['inputUlica'],
                int(form['inputNr budynku']),
                int(form['inputNr lokalu']),
                form['inputPoczta'],
                form['inputKod pocztowy'],
                form['inputStanowisko'],
                form['inputData zatrudnienia']]

    def read_from_orders(self, form):
        return [form['inputImie klienta'],
                form['inputNazwisko klienta'],
                form['inputImie pracownika'],
                form['inputNazwisko pracownika'],
                form['inputProdukt'],
                int(form['inputIlosc']),
                form['inputData zlozenia zamowienia'],
                form['inputData realizacji zamowienia']]
