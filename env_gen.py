"""
 eqchangepy Program environment.

     環境設定用 .env ファイルを作成する

 $ python ./env_gen.py

 docker-compose.yml
 python:
    volumes:
      - ./apps:/code               # Django,Python projectコードをマウント
      - ./static:/static           # Django 静的ファイルディレクトリをマウント
      - ./data:/data               # projectデータ用ディレクトリをマウント

 Last Change: 2021/07/13 18:42:43.
"""
import environ
import os
import pwd
import subprocess

# Docker = True     # Docker Environmental setting
Docker = False


# userdir = pwd.getpwuid(os.getuid())[0]

if Docker:
    basedir = '/src'
    env_file = '/src/.env'
    host_name = 'mysql_db'
    root_pass = 'XXXXX'   # <- mysql user のパスワードはそれぞれの設定値を入力する.
    mysql_pass= 'testdb'
else:
    basedir = environ.Path(__file__) - 1
    env_file = str(basedir.path(".env"))
    host_name = 'localhost'
    root_pass = 'XXXXX'    # <- mysql user のパスワードはそれぞれの設定値を入力する.
    mysql_pass = 'XXXXX'   # <- mysql user のパスワードはそれぞれの設定値を入力する.

# External database
# Mysql   DATABASE_URL=mysql+mysqldb://root:3#%KA@localhost/testdb?charset=utf8
# Postsql
EDB_CONFIG = """
# External Database Setting
DATABASE_URL=mysql+mysqldb://root:%s@%s/testdb?charset=utf8
MYSQL_ENGINE=mysql+mysqldb
MYSQL_USER=root
MYSQL_HOST=localhost
MYSQL_PASSWORD=%s
MYSQL_DBNAME=testdb
MYSQL_PORT=3306
""".strip() % (
    root_pass,
    host_name,
    mysql_pass,
)

# /Users/%s/Document/volcano/csv/earthquake/man
if Docker:
    # projectデータ用ディレクトリ
    docdir = '/data'
else :
    docdir = '/Users/{}/Documents'.format(pwd.getpwuid(os.getuid())[0])

DATA_PATH = """
# CSV file storage directory
MAN_STOK_DIR=%s/volcano/csv/earthquake/man
ETOS_STOK_DIR=%s/volcano/csv/earthquake/etos
VOIS_STOK_DIR=%s/volcano/csv/earthquake/vois
# Working directory
WORK_DIR=%s/work  
""".strip() % (
    docdir,
    docdir,
    docdir,
    docdir,
)

PROG_PATH = """
# Project directory
PROG_DIR=%s/quake
INI_DIR=%s/quake/ini
AWK_DIR=%s/quake/awk
# Data directory and temp directory
DATA_DIR=%s/quake/data
TMP_DIR=%s/quake/tmp
# Tests Unit directory
TESTS_INI_DIR=%s/quake/tests
""".strip() % (
    basedir,
    basedir,
    basedir,
    basedir,
    basedir,
    basedir,
)

# testdir = environ.Path(__file__) - 1
SQL_PATH = """
# SQL Dump file
MAKO_TEMPLATE_DIR=%s/makosql/templates/quake
SQL_DATA_DIR=%s/work
SQL_DUMP_DIR=%s/work/quake
# Docker Environmental Setting : %s
""".strip() % (
    basedir,
    docdir,
    docdir,
    Docker,
)

# Writing our configuration file to '.env'
CONFIG_STRING = "{}\n{}\n{}\n{}\n".format(EDB_CONFIG, DATA_PATH, PROG_PATH, SQL_PATH)

with open(".env", "w") as configfile:
    configfile.write(CONFIG_STRING)

print('#########################################')
subprocess.run(["cat", ".env"])
print("# .env file :",env_file)
print('#########################################')
