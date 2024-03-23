#!/bin/bash

# Set executable permission for this script
chmod +x "$0"

# Create a virtual environment named ".venv" in the current directory
python3 -m venv .venv

echo "Virtual environment created successfully!"

# Activate the virtual environment (uncomment if desired)

source .venv/bin/activate

echo "Virtual environment activated!"

echo "Running requirements.txt"

pip install -r requirements.txt

echo "**** Your Environment is Ready *****"

