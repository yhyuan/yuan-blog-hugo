---
title: "Create Shell Script Test Bitcoind"
date: 2023-11-09T10:36:00-05:00
tags: ['Bitcoin', 'Shell', 'Automation']
draft: false
---

## Create a Shell script
```
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
```
save it as bitocind-test.sh
```
chmod +x bitocind-test.sh
```

## Shedule it to run every 10 minutes
```
crontab -e
```
add 
```
*/10 * * * * /home/user/bitocind-test.sh
```
save it. 