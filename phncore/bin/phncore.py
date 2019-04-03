import sys
import os
import subprocess
import argparse

# expected to be exposed
APP_SCRIPT_NAME = 'core.py'

DETACHED_PROCESS = 0x00000008  # present in subprocess module only from python 3.7. Manually defined for compatibility


def get_arguments():
    parser = argparse.ArgumentParser(description='Manager for PHNcore app.')
    parser.add_argument('--start', action='store_true', help='Start a new instance of an app')

    return parser.parse_args()


def start_app():
    # provide a full path to the script (assume that it is exposed to the same directory, as a curent interpreter)
    # a script can not be called without 'python' on Windows, but a call with 'python' prefix only
    # searches for scripts in a current directory
    script_path = os.path.join(os.path.dirname(sys.executable), APP_SCRIPT_NAME)

    creationflags = None
    if os.name == 'nt':
        creationflags = DETACHED_PROCESS

    pid = subprocess.Popen(['python', script_path],
                           creationflags=creationflags).pid

    return pid


if __name__ == '__main__':
    args = get_arguments()

    if args.start:
        pid = start_app()
        print(pid)
