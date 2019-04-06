import sys
import os
import subprocess
import argparse

# expected to be exposed
APP_SCRIPT_NAME = 'core.py'


def start_daemon(args):

    DETACHED_PROCESS = 0x00000008  # present in subprocess module from python 3.7. Manually defined for compatibility

    creationflags = 0
    start_new_sess = False
    if os.name == 'nt':
        creationflags = DETACHED_PROCESS
    elif os.name == 'posix':
        start_new_sess = True

    pid = subprocess.Popen(args, creationflags=creationflags, start_new_session=start_new_sess,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).pid
    return pid


def get_arguments():
    parser = argparse.ArgumentParser(description='Manager for PHNcore app.')
    parser.add_argument('--start', action='store_true', help='Start a new instance of an app')

    return parser.parse_args()


def start_app():

    # provide a full path to the script (assume that it is exposed to the same directory, as a current interpreter)
    # a script can not be called without 'python' on Windows, but a call with 'python' prefix only
    # searches for scripts in a current directory
    script_path = os.path.join(os.path.dirname(sys.executable), APP_SCRIPT_NAME)

    pid = start_daemon(['python', script_path])
    return pid


if __name__ == '__main__':
    args = get_arguments()

    if args.start:
        pid = start_app()
        print(pid)

