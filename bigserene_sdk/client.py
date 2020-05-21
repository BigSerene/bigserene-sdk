"""
Bigserene Client Configuration
"""
from pathlib import Path
from functools import wraps

import requests

from bigserene_sdk.error import BigSereneError


class BigsereneClient(object):
    def __init__(self, config, headers=None):
        self.host = config.host
        self.headers = headers or {}
        self.session = requests.session()
        self._email = config.email
        self._password = config.password

        if config.token:
            self.headers["Authorization"] = f"Bearer {config.token}"
        else:
            self.login(self._email, self._password)

    def login(self, email, password):
        return self.post(
            "/api/auth/login", json={"email": email, "password": password}, login=False
        )

    def download(self, url, output_path=None):
        file_bytes = self.session.get(url).content
        if output_path:
            path = Path(output_path)
            path.parent.mkdir(exist_ok=True, parents=True)
            with path.open("wb") as f:
                f.write(file_bytes)
            return str(output_path.resolve())
        else:
            return file_bytes

    def _request(self, fn):
        @wraps(fn)
        def wrapper(url, *args, headers=None, login: bool = True, **kwargs):
            headers = headers or {}
            headers.update(self.headers)

            if not url.startswith("http"):
                url = self.host + url

            response = fn(url, *args, headers=headers, **kwargs)
            if response.status_code == 401:
                if not login:
                    raise BigSereneError(401, body="Invalid Login Credentials")
                self.login(self._email, self._password)
                response = fn(url, *args, headers=headers, **kwargs)
            if response.status_code >= 400:
                try:
                    error = response.json()
                    raise BigSereneError(response.status_code, body=error)
                except ValueError:
                    error = response.content
                    raise BigSereneError(response.status_code, body=None, raw=error)
            return response.json()

        return wrapper

    def __getattribute__(self, name):
        if name in ("post", "get", "delete", "head", "put"):
            return self._request(getattr(self.session, name))
        return super().__getattribute__(name)
