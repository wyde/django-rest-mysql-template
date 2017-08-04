#!/home/drfuser/pyvenv/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import csv
import MySQLdb
from drf.config import *

def help():
    print('  USAGE: valid command list as followed')
    print('  create_demodb_and_demouser ')
    print('  create_table_stations ')
    print('  drop_table_stations ')
    print('  setup')

def root_connect():
    try: 
        r_conn = MySQLdb.connect(host=MYSQL_ROOT_CONFIG['host'],
                                user='root',
                                passwd=MYSQL_ROOT_CONFIG['passwd'],
                                charset=MYSQL_ROOT_CONFIG['charset'])
    except:
        print("Can't Connect Database via root: ", sys.exc_info()[0])
        sys.exit()
    else:
        return r_conn

def create_demodb_and_demouser():
    r_conn = root_connect()
    r_cursor = r_conn.cursor()
    sql = 'CREATE USER IF NOT EXISTS \"' + MYSQL_CONFIG['user'] + '\"@\"' + MYSQL_CONFIG['host'] + '\" IDENTIFIED BY \"' + MYSQL_CONFIG['passwd'] + '\"'
    r_cursor.execute(sql)
    sql = 'CREATE DATABASE IF NOT EXISTS ' + MYSQL_CONFIG['db'] + ' CHARACTER SET ' + MYSQL_CONFIG['charset']
    r_cursor.execute(sql)
    sql = "GRANT ALL PRIVILEGES ON " + MYSQL_CONFIG['db'] + ".* to '" + MYSQL_CONFIG['user'] + "'@'" + MYSQL_CONFIG['host'] + "'"
    r_cursor.execute(sql)
    r_cursor.execute('FLUSH PRIVILEGES')
    r_cursor.close()
    r_conn.close()
    
def dbuser_connect():
    try:
        conn = MySQLdb.connect(host=MYSQL_CONFIG['host'],
                                user=MYSQL_CONFIG['user'],
                                passwd=MYSQL_CONFIG['passwd'],
                                db=MYSQL_CONFIG['db'],
                                charset=MYSQL_CONFIG['charset'])
    except:
        print("Can't Connect Database via " + MYSQL_CONFIG['user'], sys.exc_info()[0])
        sys.exit()
    else:
        return conn

def create_table_stations():
    conn = dbuser_connect()
    cursor = conn.cursor()
    try:
        cursor.execute("""CREATE TABLE IF NOT EXISTS stations (
                    spk INT(5) NOT NULL PRIMARY KEY,
                    name CHAR(10) NOT NULL,
                    sid CHAR(5) NOT NULL,
                    county CHAR(3) NOT NULL,
                    lon FLOAT(7,4) NOT NULL,
                    lat FLOAT(7,4) NOT NULL
                    ) ENGINE=InnoDB""")
    except:
        print("WARNING: Table might already exist")
        cursor.close()
        conn.close()
        sys.exit()
    cursor.close()
    conn.close()
    print("table has been created...")

def drop_table_stations():
    conn = dbuser_connect()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE stations;")
    cursor.close()
    conn.close()
    print("table has been dropped...")

def seidm():
    print("SEIDM ROCKS!!")

def setup():
    create_demodb_and_demouser()
    print("Setup Complete")

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] in ["create_demodb_and_demouser", 
                                            "create_table_stations", 
                                            "drop_table_stations", 
                                            "setup",
                                            "seidm"]:
        f = globals()[sys.argv[1]]
        f()
    else:
        help()
        sys.exit()
