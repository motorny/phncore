import sys
import os
import subprocess
import argparse

# expected to be exposed
APP_SCRIPT_NAME = 'core.py'


def get_arguments():
    parser = argparse.ArgumentParser(description='Manager for PHNcore app.')
    parser.add_argument('--start', action='store_true', help='Start a new instance of an app')

    return parser.parse_args()


def start_app():
    # provide a full path to the script (assume that it is exposed to the same directory, as a curent interpreter)
    # a script can not be called without 'python' on Windows, but a call with 'python' prefix only
    # searches for in a current directory
    script_path = os.path.join(os.path.dirname(sys.executable), APP_SCRIPT_NAME)
    pid = subprocess.Popen(['python', script_path],
                           creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP).pid

    return pid


if __name__ == '__main__':
    args = get_arguments()

    if args.start:
        pid = start_app()
        print(pid)
