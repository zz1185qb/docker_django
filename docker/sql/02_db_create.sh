#!/bin/sh
#  Mysql table creation
echo "Mysql table creation Start"
mysql -u testdb -ptestdb testdb < 105_quake_tbl.sql_
mysql -u testdb -ptestdb testdb < 108_quake_tbl.sql_
mysql -u testdb -ptestdb testdb < 109_quake_tbl.sql_
mysql -u testdb -ptestdb testdb < 112_quake_tbl.sql_
mysql -u testdb -ptestdb testdb < 113_quake_tbl.sql_
echo "Mysql table creation End"