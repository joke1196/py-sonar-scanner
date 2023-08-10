import argparse
import os
import sys
from typing import Union

import toml


class Configuration:
    sonar_scanner_executable_path: str
    sonar_scanner_path: str
    sonar_scanner_version: str
    scan_arguments: list[str]

    def __init__(self):
        self.sonar_scanner_path = '.scanner'
        self.sonar_scanner_version = '4.6.2.2472'
        self.sonar_scanner_executable_path = ''
        self.scan_arguments = []

    def setup(self):
        """ This is executed when run from the command line """
        parser = argparse.ArgumentParser()

        # Required positional argument
        parser.add_argument("arg", help="Required positional argument")

        # Optional argument flag which defaults to False
        parser.add_argument("-f", "--flag", action="store_true", default=False)

        # Optional argument which requires a parameter (eg. -d test)
        parser.add_argument("-n", "--name", action="store", dest="name")

        # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
        parser.add_argument(
            "-v",
            "--verbose",
            action="count",
            default=0,
            help="Verbosity (-v, -vv, etc)")

        # Specify output of "--version"
        # parser.add_argument(
        #     "--version",
        #     action="version",
        #     version="%(prog)s (version {version})".format(version=__version__))

        # args = parser.parse_args()

        scan_arguments = []
        for arg in sys.argv:
            if arg.startswith("-D"):
                scan_arguments.append(arg)

        if not os.path.isfile('pyproject.toml'):
            return

        with open('pyproject.toml', 'r') as file:
            # TODO: actually search for pyproject.toml
            toml_data = file.read()
            parsed_data = toml.loads(toml_data)
            print(parsed_data)
            if 'sonar' in parsed_data:
                sonar_properties = parsed_data['sonar']
                for key, value in sonar_properties.items():
                    self._add_parameter_to_scanner_args(scan_arguments, key, value)

        self.scan_arguments = scan_arguments

    def _add_parameter_to_scanner_args(self, scan_arguments: list[str], key: str, value: Union[str, dict]):
        if isinstance(value, str):
            scan_arguments.append(f"-Dsonar.{key}={value}")
        if isinstance(value, dict):
            for k, v in value.items():
                self._add_parameter_to_scanner_args(scan_arguments, f"{key}.{k}", v)