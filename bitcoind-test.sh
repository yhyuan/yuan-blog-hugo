#!/bin/bash

# Define the name of the process to check
PROCESS_NAME="bitcoind"

# Check if the process is running
if pgrep -x "$PROCESS_NAME" >/dev/null; then
    echo "$PROCESS_NAME is running."
else
    echo "$PROCESS_NAME is not running. Starting $PROCESS_NAME..."
    bitcoind
    # Start the process here, for example:
    # /path/to/bitcoind -options &
    # Replace '/path/to/bitcoind -options &' with the actual command to start bitcoind.
fi
