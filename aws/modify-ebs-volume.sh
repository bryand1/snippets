#!/bin/bash

# https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cli-modify.html

aws ec2 modify-volume --region us-east-1 --volume-id vol-11111111111111111 --size 200 --volume-type io1 --iops 10000
