class BigSereneError(Exception):
    def __init__(self, code, body, raw=None):
        self.code = code
        self.body = body
        self.raw = raw
        super().__init__(f"Code {self.code}: {self.body or self.raw}")

