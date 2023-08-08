import os.path
import platform
import shutil
import urllib.request
import zipfile

from src.py_sonar_scanner_DAVID_K.context import Context

systems = {
    'Darwin': 'macosx',
    'Windows': 'windows'
}

class ScannerConfig:
    def setup(self, ctx: Context):
        if os.path.exists(ctx.sonar_scanner_path):
            shutil.rmtree(ctx.sonar_scanner_path)

        os.mkdir(ctx.sonar_scanner_path)

        system_name = systems.get(platform.uname().system, 'linux')

        # Download the binaries and unzip them
        # https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${version}-${os}.zip
        scanner_res = urllib.request.urlopen(f'https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-{ctx.sonar_scanner_version}-{system_name}.zip')
        scanner_zip_path = os.path.join(ctx.sonar_scanner_path, 'scanner.zip')
        with open(scanner_zip_path, 'wb') as output:
            output.write(scanner_res.read())

        with zipfile.ZipFile(scanner_zip_path, "r") as zip_ref:
            zip_ref.extractall(ctx.sonar_scanner_path)

        os.remove(scanner_zip_path)

        ctx.scanner_bin_path = os.path.join(ctx.sonar_scanner_path, f'sonar-scanner-{ctx.sonar_scanner_version}-{system_name}', 'bin', 'sonar-scanner')
        print(ctx.scanner_bin_path)


class EnvironmentConfig:
    def setup(self, ctx: Context):
        ScannerConfig().setup(ctx)
