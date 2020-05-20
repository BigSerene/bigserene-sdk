from bigserene_sdk.reports import ReportClient
from bigserene_sdk.config import Config


def client_from_config(config_file, profile):
    config = Config.from_file(config_file, profile=profile)
    return ReportClient(config)
