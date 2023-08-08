import os

from src.py_sonar_scanner_DAVID_K.context import Context


class Scanner:
    def scan(self, ctx: Context):
        command = os.path.join(ctx.sonar_scanner_bin_path, 'sonar-scanner')
        print(command)
