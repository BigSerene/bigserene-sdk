import traceback
import click

from bigserene_sdk.report import Report
from bscli.client import client


@click.group()
def main():
    pass


@main.command("check")
@click.argument("report_ids", nargs=-1, type=int)
def check(report_ids):
    for report_id in report_ids:
        try:
            report = Report(id=report_id)
            client.wait(report)
            client.results(report)
            result = client.download_results(report)
            click.secho(f"Success {report.id}: {result}", fg="green")
        except Exception:
            traceback.print_exc()
            click.secho(f"Failed {report_id}", fg="red")


@main.command("run")
@click.argument("report_ids", nargs=-1, type=int)
def run(report_ids):
    for report_id in report_ids:
        job_id = client.run_report(report_id)
        click.secho(f"Running {report_id} with job {job_id}")


@main.command("list")
@click.option("--brand")
def run(brand=None):
    opts = {}
    if brand:
        opts["brand"] = brand

    status_color = {"COMPLETE": "green", "FAILED": "red"}
    for report in client.list_reports(**opts):
        click.secho(f"{report}", fg=status_color.get(report.status, "white"))


@main.command("get")
@click.argument("report_ids", nargs=-1, type=int)
def run(report_ids):
    for report_id in report_ids:
        report = client.get_report(report_id)
        click.secho(report.detailed)


if __name__ == "__main__":
    main()
