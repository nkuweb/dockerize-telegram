#!/bin/sh
sudo -s
cat flask_config > \
		/etc/nginx/sites-enabled \
		/etc/nginx/sites-enabled
service nginx restart
