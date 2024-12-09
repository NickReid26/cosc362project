#!/bin/bash

# Activate the virtual environment
source /path/to/virtual/environment/activate

# Run the Python scripts in the background
python /path/to/simtherm.py &
python /path/to/rgb_control.py &

# Wait to keep the script running
wait
