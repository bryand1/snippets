#!/bin/bash

# https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/recognize-expanded-volume-linux.html

# To re-size a Linux partition

# 1. Use the lsblk command to list the block devices attached to your instance
lsblk

# 2. Use the df -h command to report the existing disk space usage on the file system
df -h

# 3. Expand the modified partition using growpart (and note the unusual 
#    syntax of separating the device name from the partition number)
#    $ sudo growpart /dev/xvdf 1
sudo growpart /dev/nvme0n1 1

# A look at the lsblk output confirms that the partition /dev/xvdf1
# now fills the available space on the volume /dev/xvdf
lsblk

# To extend a Linux file system

# 1. Use a file system-specific command to resize each file system to the new volume capacity.

# For a Linux ext2, ext3, or ext4 file system, use the following command, substituting the device name to extend:
# sudo resize2fs /dev/xvdf1
sudo resize2fs /dev/nvme0n1p1
