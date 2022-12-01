#!/usr/bin/python

import os
for l in ('home.py', "index.py", "quran.py", "info.py"):
	symlink = os.path.lexists('e_mushaf/cgi-bin/' + l)
	if not symlink:
		os.symlink("e_mushaf.py",'e_mushaf/cgi-bin/' + l)
	else:
		print('e_mushaf/cgi-bin/' + l)
