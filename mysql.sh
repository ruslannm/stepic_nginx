#!/bin/bash
mysql -uroot -e "CREATE USER 'admin'@'localhost'"
mysql -uroot -e "SET PASSWORD FOR 'admin'@'localhost' = PASSWORD('pass111')"
mysql -uroot -e "CREATE DATABASE firstdb"
mysql -uroot -e "GRANT ALL ON firstdb.* TO 'admin'@'localhost'"

# mysql -uroot -e "CREATE DATABASE stepic_web;"
# mysql -uroot -e "GRANT ALL PRIVILEGES ON stepic_web.* TO 'box'@'localhost' WITH GRANT OPTION;"
