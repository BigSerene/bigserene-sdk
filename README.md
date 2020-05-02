# bigserene_sdk

Bigserene SDK to access Bigserene App Platform

Built on: Python3 and Docker (alpine)<br>
Maintained by: Chris Lee [chrisl@bigseren.com]

## Installation

```bash
pip3 install git+https://github.com/BigSerene/bigserene-sdk.git --user
```

## Configuration/Credentials

The SDK BigsereneClient class takes in a Config object that can be populated in code or by file. Files accepted are .ini files as shown in `bigserene.sample.ini`. Each section in the configuration file represents a profile. You can pass in a profile when calling `Config.from_file` to specify the profile to use; otherwise, the `default` profile is used.

## Command Line

```bash
$ bscli --help
Usage: bscli [OPTIONS] COMMAND [ARGS]...

Options:
  -f, --file TEXT     Bigserene SDK Configuration File to load
  -p, --profile TEXT  Bigserene SDK Profile to use from configuration file
  --help              Show this message and exit.

Commands:
  download  Given report_ids, check status & download results for each
  get       Given report IDs, print out metadata for the associated Reports
  list      List reports that you have access to
  run       Re-run an existing report from the command line
```

## Contribute & Develop

- Additional Python3 dependencies can be added to setup.py
- Tests are located in ./tests <br>
- To run the docker container with the basic requirements, dependencies, and the package installed:
  ```bash
  $ docker-compose up
  ```
