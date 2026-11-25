#!/bin/sh
set -eu
echo "Filesystem containing current directory:"
df -T .
echo "\nInode usage:"
df -i .
echo "\nFile metadata:"
stat .
echo "\nInode number:"
ls -id .
echo "\nMount details:"
findmnt -T .
echo "\nIf this is ext2/3/4 and device access is permitted, run:"
echo "sudo tune2fs -l /dev/<device> | grep -E 'Block size|Free blocks|Inode count'"
