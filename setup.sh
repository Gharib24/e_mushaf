#!/bin/bash

[[ $(id -u) -ne 0 ]] && echo "Please run as root" && exit 0

domain="rocbird.org"
subdomain="quran"

DocumentRoot=/var/www/${subdomain}.${domain}

if [[ "$1" == "install" ]]; then

	mkdir -p ${DocumentRoot}
	
	cp -rf e_mushaf/* ${DocumentRoot}/
	sed -e "s/SERVERNAME/${subdomain}.${domain}/g" -e\
	       "s/SERVERALIAS/${subdomain}.${domain}/g" -e\
	       "s|DOCUMENTROOT|$DocumentRoot|g" vhost.conf>\
	       /etc/httpd/conf.d/${subdomain}.${domain}.conf
	       
	chcon -R -t httpd_sys_script_exec_t ${DocumentRoot}/cgi-bin
#	setsebool -P httpd_enable_cgi 1
	chmod 755  -R ${DocumentRoot}/cgi-bin
	
	systemctl restart httpd.service
elif [[ "$1" == "remove" ]]; then
	rm -rf $DocumentRoot
	rm -f /etc/httpd/conf.d/${subdomain}.${domain}.conf
	systemctl restart httpd.service
else
	echo "sudo $0 install"
	echo "sudo $0 remove"
fi










