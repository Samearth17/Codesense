#!/bin/bash

# Update existing packages
sudo apt-get update
# Install pip3
sudo apt-get install python3-pip
# Install the necessary packages
pip3 install jupyter notebook
# Install virtual environment
pip3 install virtualenv
# Create a virtual environment in the current directory
virtualenv notebook-env
# Activate the virtual environment
source notebook-env/bin/activate
# Upgrade pip and jupyter inside the virtual environment
pip3 install --upgrade pip jupyter
# Make jupyter launchable from inside the virtual environment
python3 -m ipykernel install --user

# To exit from the virtual environment
deactivate