#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Define the virtual environment directory
VENV_DIR="venv"

# Check if virtual environment directory exists
if [ ! -d "$VENV_DIR" ]; then
  # Create virtual environment
  python3 -m venv $VENV_DIR
fi

# Activate virtual environment
source $VENV_DIR/bin/activate

# Run the browser test
pytest -s tests/test_ocula_resources.py

# Run the API test
pytest -s tests/test_weather_api.py

# Deactivate virtual environment
deactivate
