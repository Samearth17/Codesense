#!/bin/bash

# Download latest version of Python
curl -O https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tgz

# Extract the tgz file
tar -xzf Python-3.8.5.tgz

# Move into the Python directory
cd Python-3.8.5

# Run the configure script
./configure

# Compile and install
make
make install