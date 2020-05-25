### Research Access to Report Data

Follow README.md for setting up the SDK & CLI.

Using the CLI's `bscli download <report_id>` will download all metric tables and image group mappings for the report. It will alos download all the images in the same tiered structure as the JSON representation of the tables.

#### Using the SDK for programmatic access

Accessing the Bigserene Client & Report Client

```python3
from bigserene_sdk.reports import ReportClient
from bigserene_sdk.config import Config

# config_file is the path to the credentials configuration file (.ini)
config = Config.from_file(config_file)

report_client = ReportClient(config)
bigserene_client = BigsereneClient(config)
```
