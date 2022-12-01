#!/bin/bash

mkdir -p e_mushaf/static/locales/{en,ar}/LC_MESSAGES
xgettext -d base -o e_mushaf/static/locales/base.pot e_mushaf/cgi-bin/*.py

sed -e "s/CHARSET/utf-8/g" -i e_mushaf/static/locales/base.pot 
[ ! -f  e_mushaf/static/locales/en/LC_MESSAGES/base.po ] && cp e_mushaf/static/locales/base.pot e_mushaf/static/locales/en/LC_MESSAGES/base.po
[ ! -f  e_mushaf/static/locales/ar/LC_MESSAGES/base.po ] && cp e_mushaf/static/locales/base.pot e_mushaf/static/locales/ar/LC_MESSAGES/base.po

msgfmt -o e_mushaf/static/locales/en/LC_MESSAGES/base.mo e_mushaf/static/locales/en/LC_MESSAGES/base
msgfmt -o e_mushaf/static/locales/ar/LC_MESSAGES/base.mo e_mushaf/static/locales/ar/LC_MESSAGES/base
