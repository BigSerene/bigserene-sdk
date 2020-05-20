"""
Report Loading SDK
"""
import pytz
import json
import datetime
import time
from typing import Dict, List
from pathlib import Path

from bigserene_sdk.client import BigsereneClient
from .report import Report


class ReportClient(BigsereneClient):
    def status(self, report: Report):
        return self.get(f"/api/reports/{report.id}/status")["ready"]

    def get_report(self, report_id: int) -> Report:
        report_json = self.get(f"/api/reports/{report_id}")
        return Report.from_json(report_json)

    def run_report(self, report_id: int) -> Report:
        report_json = self.put(f"/api/reports/{report_id}")
        return Report.from_json(report_json)

    def list_reports(self, brand=None, before=None, after=None):
        reports_json = self.get(
            f"/api/reports", params={"brand": brand, "before": before, "after": after}
        )

        return [Report.from_json(report_json) for report_json in reports_json]

    def create_report(
        self, ad_account_id: str, instagram_id: str, competitor_handles: List[str]
    ):
        report_json = self.post(
            f"/api/reports",
            json={
                "adAccountId": ad_account_id,
                "instagramId": instagram_id,
                "instagramHandles": competitor_handles,
            },
        )
        return Report.from_json(report_json)

    def wait(self, report: Report):
        interval = 1
        while True:
            status = self.status(report)
            if status:
                return
            print(f"Waiting for job completion")
            time.sleep(interval)
            interval = min(interval * 2, 10)

    def results(self, report: Report) -> Dict:
        result = self.get(f"/api/reports/{report.id}/result")
        report = report.update_values(result)
        return report

    def download_results(self, report):
        report_dir = report.output_dir
        report_dir.mkdir(exist_ok=True, parents=True)
        for filename, url in report.tables.items():
            result = self.download(url, report_dir / filename)

        result = report_dir / "all_metrics.json"
        if result.exists():
            report_json = json.load(Path(result).open("r"))
            for group_number, group_json in report_json.items():
                group_dir = report_dir / str(group_number)
                group_dir.mkdir(exist_ok=True, parents=True)
                for url in group_json["rep_images"]:
                    self.download(url, (group_dir / url.rsplit("/", 1)[-1]))
        return str(report_dir.resolve())
