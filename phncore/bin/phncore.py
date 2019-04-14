import sys
import os
import subprocess
import argparse
import time
import json

# expected to be exposed
APP_SCRIPT_NAME = 'core.py'
DEFAULT_PORT = 8200


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

def make_instance_record(pid, info):
    instances_dir = os.path.join(sys.prefix, 'tmp', 'instances')
    os.makedirs(instances_dir, exist_ok=True)

    cur_timestamp = int(time.time())

    instance_filename = '{0}_{1}.txt'.format(cur_timestamp, pid)
    with open(os.path.join(instances_dir,instance_filename),'w') as f:
        json.dump(info,f)


def get_arguments():
    parser = argparse.ArgumentParser(description='Manager for PHNcore app.')
    parser.add_argument('--start', action='store_true', help='Start a new instance of an app')
    parser.add_argument('--stop', action='store_true', help='Stop the most recent instance')

    return parser.parse_args()


def start_app():

    # provide a full path to the script (assume that it is exposed to the same directory, as a current interpreter)
    # a script can not be called without 'python' on Windows, but a call with 'python' prefix only
    # searches for scripts in a current directory
    script_path = os.path.join(os.path.dirname(sys.executable), APP_SCRIPT_NAME)

    pid = start_daemon(['python', script_path])
    make_instance_record(pid, {'port': DEFAULT_PORT})
    return pid


if __name__ == '__main__':
    args = get_arguments()

    if args.start:
        pid = start_app()
        print(pid)

