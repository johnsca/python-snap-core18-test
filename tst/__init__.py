import os
import subprocess
from pathlib import Path

import mock  # noqa


def main():
    try:
        snap_bin = Path(os.environ['SNAP']) / 'bin'
        res = subprocess.run([str(snap_bin / 'tst-sub')],
                             stdout=subprocess.PIPE)
        if res.returncode == 0:
            subres = res.stdout.decode("utf8").strip()
        else:
            subres = 'failed'
    except FileNotFoundError:
        subres = 'not found'
    print(f'success! ({subres})')


def sub():
    print('i am subprocess')
