#/bin/bash
# Connect to MySQL server
mysql -h localhost -uroot -p"root" <<EOF SHOW DATABASES; EOF
