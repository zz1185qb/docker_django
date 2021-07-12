#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy
import mysql.connector as mysql

# host = "docker_django_db_1"                # docker-composeで定義されたMySQLのサービス名
conn = mysql.connect(
    host="docker_django_db_1",
    user="root",
    passwd="3#%KA",
    port=3306,
    database="testdb"
)

def main():
    str = 'Hello World !!!'
    ary = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print('{} Running on Docker Python'.format(str))
    print(ary)

    conn.ping(reconnect=True)
    print('Connected to Docker Python and MySQL')
    if conn.is_connected():
        print('Docker Mysql conected : OK')
    else:
        print('Docker Mysql Not conected')


#------------------- main() -------------------------------
if __name__ == "__main__":
   main()
#------------------- main end -----------------------------