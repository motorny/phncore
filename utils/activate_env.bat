@echo off
rem Script for activating python venv for PHNcore
rem Author: Nikita Motornyi

rem Name of the environment
rem Can not use 'SETLOCAL' so using complex variable name
set __ENV_NAME__PHNCORE=env_core_37

rem Deactivate just in case
call deactivate.bat

echo Activating environment %ENV_NAME%
rem activate env
call .\..\env\%__ENV_NAME__PHNCORE%\Scripts\activate.bat

rem test whether it is activated
echo Success:
python -c "import sys; print(sys.prefix != sys.base_prefix)"

rem delete variable
set "__ENV_NAME__PHNCORE="

echo For deactivating run "deactivate.bat" at any folder
