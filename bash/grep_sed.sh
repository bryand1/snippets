#!/bin/bash

# Replace AWS keys
aws_access_key_id=NEW_ACCESS_KEY_ID
aws_secret_access_key=NEW_SECRET_ACCESS_KEY
old_id=ID_TO_REPLACE
old_key=KEY_TO_REPLACE

grep -rl ${old_id} | while read f; do sed "s\\${old_id}\\${aws_access_key_id}\\; s\\${old_key}\\${aws_secret_access_key}\\" -i "${f}"; done

