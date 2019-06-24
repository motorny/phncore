#!/bin/bash
# Script for activating python venv for PHNcore
# Author: Nikita Motornyi

# Name of the environment
__ENV_NAME__PHNCORE=env_core_37

# Deactivate just in case
source deactivate

echo Activating environment $__ENV_NAME__PHNCORE
# activate env
source ./../env/$__ENV_NAME__PHNCORE/bin/activate

# test whether it is activated
echo Success:
python -c "import sys; print(sys.prefix != sys.base_prefix)"


echo For deactivating run "deactivate.bat" at any folder
