@echo off
rem Script for setting python venv for PHNcore and installing its package in develop mode

rem Next variables will be local
SETLOCAL

rem Name of created environment

rem Go to root repository directory
cd .\..\

rem save it
set ROOT_DIR=%CD%

set ENV_NAME=env_core_37
set ENV_DIR= %ROOT_DIR%\env\%ENV_NAME%
echo Setting environment %ENV_NAME%

rem setup env
python -m venv %ENV_DIR%

rem go to env folder and install phncore
cd %ENV_DIR%\Scripts
echo Environment created
echo Installing PHNcore
pip install -e %ROOT_DIR%

echo List of installed packages:
pip list
pause
