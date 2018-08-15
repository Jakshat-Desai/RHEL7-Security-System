#!/usr/bin/python2

import commands

while commands.getstatusoutput("ping -c 1 smtp.gmail.com")[0]!=0:
	pass
