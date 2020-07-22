import datetime
import json
from pathlib import Path

import pytz


class Report(object):
    id = None
    user_id = None
    ad_account_id = None
    instagram_brands = None
    instagram_id = None
    brand = None
    job_id = None
    created_at = None
    url = None
    tables = None
    artifacts = None
    status = None
    error = None

    def __init__(self, **values):
        for key, value in values.items():
            if hasattr(self, key) and not key.startswith("_"):
                setattr(self, key, value)

    @property
    def created_date(self):
        date = datetime.datetime.fromtimestamp(self.created_at).astimezone(
            pytz.timezone("est")
        )
        return date.strftime("%Y-%m-%d, %I:%M:%S %p")

    @classmethod
    def from_json(cls, values):
        report = cls()
        report.update_values(values)
        return report

    def update_values(self, values):
        for key, value in values.items():
            if hasattr(self, key):
                setattr(self, key, value)

    @property
    def output_dir(self):
        return Path("reports", str(self.user_id), str(self.id))

    def __repr__(self):
        return f"Report[{self.created_date}, {self.id}, {self.status}, {self.brand}, ig:{','.join(sorted(self.instagram_brands))}]"

    @property
    def detailed(self):
        return f"""
ID: {self.id}
USER_ID: {self.user_id}
AD_ACCOUNT_ID: {self.ad_account_id}
INSTAGRAM_BRANDS: {json.dumps(self.instagram_brands, indent=4)}
INSTAGRAM_ID: {self.instagram_id}
BRAND: {self.brand}
JOB_ID: {self.job_id}
CREATED_AT: {self.created_date}
URL: {self.url}
TABLES: \n{json.dumps(self.tables, indent=4)}
ARTIFACTS: \n{json.dumps(self.artifacts, indent=4)}
STATUS: {self.status}
ERROR: {self.error}"""
