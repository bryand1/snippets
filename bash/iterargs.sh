#!/bin/bash
#
# Iterate through command-line arguments
#
# $ bash iterargs.sh 1 2 3
# >> 1
#    2
#    3

for arg in "$@"; do
    echo $arg;
    # Do something with arg
done

