#!/bin/bash
# Script for setting python venv for PHNcore and installing its package in develop mode
# Author: Nikita Motornyi

echo Usage: Path to the python can be passed as an argument. Using python binary from first arg, or fall back to default python3

# Check whether path to a python is passed. use python binary from arg, or fall back to default python3
if [ "$1" != "" ]; then
    PYTHON_PATH="$1"
else
    PYTHON_PATH="python3"
fi


# Go to root repository directory
cd ./../

# save it
ROOT_DIR=$(pwd)

# Name of created environment
ENV_NAME=env_core_37
ENV_DIR=$ROOT_DIR/env/$ENV_NAME

# setup env
$PYTHON_PATH -m venv $ENV_DIR

echo Environment created

echo Installing PHNcore
$ENV_DIR/bin/pip3 install -e $ROOT_DIR  # use pip3 from directly from environment

echo List of installed packages:
$ENV_DIR/bin/pip3 list
$ENV_DIR/bin/pip3 -V
