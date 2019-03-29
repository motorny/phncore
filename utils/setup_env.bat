@echo off
rem Script for setting python venv for PHNcore and installing its package in develop mode
rem Author: Nikita Motornyi

echo Usage: Path to the python can be passed as an argument, if python is not in PATH variable

rem Next variables will be local
SETLOCAL

rem Check whether path to a python is passed and set a corresponding variable (do not forget to handle a backslash after the path)
IF "%~1"=="" GOTO NO_PARAMS
set ARG_PY_DIR=%1\
:NO_PARAMS

rem Go to root repository directory
cd .\..\

rem save it
set ROOT_DIR=%CD%

rem Name of created environment
set ENV_NAME=env_core_37
set ENV_DIR= %ROOT_DIR%\env\%ENV_NAME%
echo Setting environment %ENV_NAME%

rem setup env
%ARG_PY_DIR%python -m venv %ENV_DIR%

rem go to env folder and install phncore
cd %ENV_DIR%\Scripts
echo Environment created
echo Installing PHNcore
pip install -e %ROOT_DIR%

echo List of installed packages:
pip list
