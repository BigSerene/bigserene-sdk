### Research Access to Report Data

Follow README.md for setting up the SDK & CLI.

Using the CLI's `bscli download <report_id>` will download all metric tables and image group mappings for the report. It will alos download all the images in the same tiered structure as the JSON representation of the tables.

#### Using the SDK for programmatic access

Accessing the Bigserene Client & Report Client

```python3
from bigserene_sdk import config, BigsereneClient, ReportClient

# config_file is the path to the credentials configuration file (.ini)
config = Config.from_file("bigserene.ini")

report_client = ReportClient(config)
bigserene_client = BigsereneClient(config)

report = report_client.get_report(51)
print(report.artifacts)
```

report.artifacts

```json
{
  "facebook_metrics": "https://api.bigserene.com/files/reports/15/51/facebook_insights.csv",
  "instagram_metrics": "https://api.bigserene.com/files/reports/15/51/ig_discovery_insights.csv",
  "image_mapping": "https://api.bigserene.com/files/reports/15/51/ig_brands_image_groups.csv"
}
```

Download Files

```python3
bigserene_client.download("https://api.bigserene.com/files/reports/15/51/facebook_insights.csv", "facebook_insights.csv")
```
