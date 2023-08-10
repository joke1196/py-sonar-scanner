"""
Module Docstring
"""

__author__ = "Python Squad"
__version__ = "0.1.0"

from py_sonar_scanner.configuration import Configuration
from py_sonar_scanner.environment import Environment


def scan():
    cfg = Configuration()
    cfg.setup()

    env = Environment(cfg)
    env.setup()
    env.scanner().scan()
    env.cleanup()

if __name__ == "__main__":
    scan()