from bigserene_sdk.report import ReportClient
from bigserene_sdk.config import Config

config = Config.from_file("bigserene.ini")
client = ReportClient(config)
