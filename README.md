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

## Setting Up Credentials

1. Copy the `bigserene.sample.ini` as `bigserene.ini` in the directory you will be working in or in your \$HOME directory.
2. Open the `bigserene.ini` and fill in the email & password associated with your Bigserene App account. Example:

```
[default]
email = user@example.com
password = password123
```

3. Test your access by running `bscli list`. You should not receive a Permission error.

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
