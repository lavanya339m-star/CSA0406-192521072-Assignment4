#!/bin/sh
set -eu
(cd Task02 && gcc -std=c11 -Wall -Wextra allocation.c -o allocation && ./allocation)
(cd Task04 && gcc -std=c11 -Wall -Wextra disk_scheduling.c -o disk_scheduling && ./disk_scheduling)
(cd Task06 && python3 streaming_model.py)
