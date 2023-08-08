import os.path
import shutil
import urllib
import zipfile

from src.py_sonar_scanner_DAVID_K.context import Context


class ScannerConfig:
    def setup(self, ctx: Context):
        if os.path.exists(ctx.sonar_scanner_path):
            shutil.rmtree(ctx.sonar_scanner_path)

        # Download the binaries and unzip them
        # https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${version}-${os}.zip
        system_name = 'linux'
        scanner_res = urllib.request.urlopen(f'https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-{ctx.sonar_scanner_version}-{system_name}.zip')
        with open('scanner.zip', 'wb') as output:
            output.write(scanner_res.read())

        with zipfile.ZipFile("scanner.zip", "r") as zip_ref:
            zip_ref.extractall(ctx.sonar_scanner_path)

        ctx.scanner_bin_path = os.path.join(ctx.sonar_scanner_path, f'sonar-scanner-{ctx.sonar_scanner_version}-{system_name}', 'bin', 'sonar-scanner')


class EnvironmentConfig:
    def setup(self, ctx: Context):
        ScannerConfig().setup(ctx)
