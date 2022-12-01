#!/bin/bash
cat e_mushaf/cgi-bin/*.py | sed '/^\s*#/d;/^\s*$/d' | wc -l

