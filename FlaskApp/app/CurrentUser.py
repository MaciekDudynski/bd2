class CurrentUser:
    def __init__(self, login='', is_client=False, is_worker=False, is_admin=False):
        self.login = login
        self.is_client = is_client
        self.is_worker = is_worker
        self.is_admin = is_admin
