#!/bin/bash

# Correct systemic filename error
# rename phillips.pkl -> phillips.pkl
# rename phillips-1.json -> philips-1.json

find . -name "phillips*" | while read f; do mv -v "$f" $(echo "$f" | sed 's/phillips/philips/'); done

