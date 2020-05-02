import traceback
import click

from bigserene_sdk.report import Report
from bscli.client import client_from_config


@click.group()
@click.option(
    "--file",
    "-f",
    "config_file",
    default="bigserene.ini",
    help="Bigserene SDK Configuration File to load",
)
@click.option(
    "--profile",
    "-p",
    "profile",
    default="default",
    help="Bigserene SDK Profile to use from configuration file",
)
@click.pass_context
def main(ctx, config_file, profile):
    ctx.ensure_object(dict)
    ctx.obj["client"] = client_from_config(config_file, profile=profile)


@main.command("download")
@click.argument("report_ids", nargs=-1, type=int)
@click.pass_context
def download_report(ctx, report_ids):
    """
    Given report_ids, check status & download results for each
    """
    client = ctx.obj["client"]
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
@click.pass_context
def run(ctx, report_ids):
    """
    Re-run an existing report from the command line
    """
    client = ctx.obj["client"]
    for report_id in report_ids:
        report = client.run_report(report_id)
        click.secho(f"Running {report}")


@main.command("list")
@click.option("--brand")
@click.pass_context
def list_reports(ctx, brand=None):
    """
    List reports that you have access to
    """
    client = ctx.obj["client"]
    opts = {}
    if brand:
        opts["brand"] = brand

    status_color = {"COMPLETE": "green", "FAILED": "red"}
    for report in client.list_reports(**opts):
        click.secho(f"{report}", fg=status_color.get(report.status, "white"))


@main.command("get")
@click.argument("report_ids", nargs=-1, type=int)
@click.pass_context
def get_report(ctx, report_ids):
    """
    Given report IDs, print out metadata for the associated Reports
    """
    client = ctx.obj["client"]
    for report_id in report_ids:
        report = client.get_report(report_id)
        click.secho(report.detailed)


if __name__ == "__main__":
    main()
