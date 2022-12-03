#!/bin/bash
hostname=quran.rocbird.org
user=myuser
rsync -av --exclude '*.pyc'  --exclude '__pycache__' --delete -e ssh ./* $user@$hostname:/home/$user/e_mushaf
