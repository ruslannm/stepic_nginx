#sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf 
#sudo rm /etc/nginx/sites-enabled/default 
#sudo /etc/init.d/nginx restart 
#sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test 
# sudo gunicorn -c /home/box/web/etc/gunicorn.conf ask.wsgi -D

#!/bin/bash

if [ -f /etc/nginx/sites-enabled/default ]; then
  sudo rm /etc/nginx/sites-enabled/default
fi

# Nginx
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

# Gunicorn
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
