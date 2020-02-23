# -*- coding: utf-8 -*-

import re

cfg = "config_example.cfg"

mylines = []

with open(cfg) as o_cfg:

	for line in o_cfg:
		mylines.append(line.rstrip('\n'))
	
index = mylines.index("interface FastEthernet4")

while True:
	if mylines[index] == "!":
		break
	print(mylines[index])
	index += 1





# find = номер строки
# while True:
# 	print строка +1
# 	break if find = "!"