#!/bin/python
import os
import random
cmd = "fdisk /dev/vdb <<EOF\nn\np\n1\n2048\n+500M\nt\n8e\nw\nEOF"
try:
	os.system(cmd)
	os.system('partprobe')
	os.system('pvcreate /dev/vdb1')
	os.system('vgcreate hitesh /dev/vdb1')
	os.system('lvcreate -n subnani -L 190M hitesh')
	os.system('mkfs.xfs /dev/hitesh/subnani')
except Exception as e:
	print("Error!!",e)
os.system('mkdir /hitesh')
cmd = "/dev/hitesh/subnani /hitesh xfs defaults 0 0"
try:
	os.system('echo "%s" >> /etc/fstab'%(cmd))
	os.system('mount -a')
except Exception as e:
	print("error!!",e)
