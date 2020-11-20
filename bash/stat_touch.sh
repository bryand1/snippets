#!bin/bash
# Touch the file to reset modified time
# touch [-a | -c | -m] -t [[CC]YY]MMDDhhmm[.SS] filename.txt

stat -c %Y appointment_types.txt
# 1576886400
date --date '@1576886400'
date --date '@1576886400' +'%Y%m%d%H%M.%S'
# 201912210000.00
modified_time=$(stat -c %Y appointment_types.txt)
date --date "@${modified_time}"
# Sat Dec 21 00:00:00 UTC 2019
touch_format=$(date --date "@${modified_time}" +'%Y%m%d%H%M.%S')
echo $touch_format
# 201912210000.00
touch -m -t ${touch_format} appointment_types.txt