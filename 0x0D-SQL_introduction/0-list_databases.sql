#/bin/bash
# Connect to MySQL server
mysql -hlocalhost -uroot -p"<password>" <<EOF SHOW DATABASES; EOF
