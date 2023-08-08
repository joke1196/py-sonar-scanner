import os

import subprocess
import threading
from context import Context


class Scanner:
    def scan(self, ctx: Context):
        command = os.path.join(ctx.sonar_scanner_executable_path, 'sonar-scanner')
        scan_args = []
        if scan_args is None:
            scan_args = []
        cmd = [ctx.sonar_scanner_executable_path] + scan_args
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

        def print_output():
            while True:
                output_line = process.stdout.readline()
                if not output_line:
                    break
                decoded_line = output_line.decode('utf-8')
                print(decoded_line, end='', flush=True)

        output_thread = threading.Thread(target=print_output)
        output_thread.start()

        process.wait()
        output_thread.join()

        return process.returncode
