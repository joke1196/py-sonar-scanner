#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Python Squad"
__version__ = "0.1.0"

from configuration_properties_config import ConfigurationPropertiesConfig
from context import Context
from environment_config import EnvironmentConfig
from scanner import Scanner

def scan():
    ctx = Context()

    ConfigurationPropertiesConfig().setup(ctx)
    EnvironmentConfig().setup(ctx)
    Scanner().scan(ctx)

if __name__ == "__main__":
    scan()
