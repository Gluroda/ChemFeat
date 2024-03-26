#!/bin/bash

# Check if any command is provided
if [ $# -eq 0 ]; then
    # Start an interactive Python shell
    exec python
else
    # Execute the provided command (assuming it's a Python script)
    exec "$@"
fi

