import configparser


class Config(object):
    host = "https://api.bigserene.com"
    email = None
    password = None
    token = None

    def __init__(self, **attrs):
        for key, value in attrs.items():
            if hasattr(self, key) and value:
                setattr(self, key, value)

    @classmethod
    def from_file(cls, config_file, profile="default"):
        parser = configparser.ConfigParser()
        parser.read(config_file)
        if profile not in parser:
            raise ValueError(f"Profile {profile} does not exist in file {config_file}")

        return cls(**parser[profile])
