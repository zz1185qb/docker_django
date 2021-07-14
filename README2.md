```
# docker_django : Djangoの開発環境(Nginx + Python + Mysql)
# ----------------------------------------------------------------
# Docker Desktop Mac 3.3.3
# docker-compose version 1.29.1
# Python 3.6.6
# Django 2.2 -> 3.0.7
# Mysql  5.7
# Last Change: 2021/07/13 17:42:43.
# ----------------------------------------------------------------
環境構築にあたり参考にさせていただいたコンテンツ（とてもわかりやすい、感謝）
https://hackerdemy.com/2019/09/09/docker-django/
```
# docker_django 実行方法
```bash
$ git clone https://github.com/zz1185qb/docker_django.git
$ cd docker_django
$ docker-compose up -d --build
$ docker ps
CONTAINER ID   IMAGE               COMMAND                  CREATED              STATUS              PORTS                                         NAMES
631c45fe5298   nginx:1.13             "nginx -g 'daemon of…"   11 minutes ago   Up 11 minutes   80/tcp, 127.0.0.1:8000->8000/tcp      docker_django_nginx_1
b089f139536e   docker_django_python   "uwsgi --socket :800…"   11 minutes ago   Up 11 minutes   8001/tcp                              docker_django_python_1
15785fbd23d3   docker_django_db       "docker-entrypoint.s…"   11 minutes ago   Up 11 minutes   33060/tcp, 127.0.0.1:3307->3306/tcp   docker_django_db_1

## Mysql コンテナに入る
## 検測値ファイルの MySQL リストア 
$ docker exec -it docker_django_db_1 sh

# cd docker-entrypoint-initdb.d
# ls -l

# sh 02_db_create.sh
  : sql dump file リストア中...
# exit

$ Python 3.6.6 Runnig test 
$ docker exec -it docker_django_python_1 sh
# pwd
/code
$ python -V
Python 3.6.6
# ls
test_docker.py  requirements.txt
# python test_docker.py
Attaching to docker_django_python_1
python_1  | Hello World !!! Running on Docker Python
python_1  | [[1 2 3]
python_1  |  [4 5 6]
python_1  |  [7 8 9]]
python_1  | Connected to Docker Python and MySQL
python_1  | Docker Mysql conected : OK

```
tree
```bash
docker-django
.
├── README.md
├── Dockerfile                               
├── docker-compose.yaml                      
├── .env       docker-compose.yaml の環境変数                                                                
├── docker                                   
│     ├── mysql                             
│     │     ├── data                       MySQLの永続化データ
│     │     └── Dockerfile                 
│     ├── nignx                             
│     │     ├── conf
│     │     │     └── app_nginx.conf      Nginxの設定ファイル
│     │     └── uwsgi_params               uwsgi_params
│     ├── python                            
│     │     ├── Dockerfile
│     │     └── requirements.txt
│     └── sql                               データベース関係                          
│            ├── 01_create_db.sql           DBユーザー、データベース作成、権限設定
│            ├── 02_db_create.sh            SQL Dump File をTableにリストアするshell
│            └── 105_quake.sql_ .. 113_quake.sql_  SQL Dump Test File
├── apps                                     
│     ├── test_docker.py                   
│     ├── project1                                                      
│     ├── :
│     └── projectX
├── data  データフォルダー                                
└── static 

```
# コンテナのビルドと立ち上げ
```bash
$ cd (path)/docker_django  Dockerホルダーへ移動

## docker環境の構築
$ docker-compose up -d --build # up -d detach モードで起動, 構築 --build  


## Docker system 状態の確認
$ docker system df
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          3         3         2.072GB   0B (0%)
Containers      3         3         222.3kB   0B (0%)
Local Volumes   37        0         1.028GB   1.028GB (100%)
Build Cache     145       0         6.164GB   6.164GB
## 削除: $ docker stop $(docker ps -q) | docker rm $(docker ps -aq) | docker rmi $(docker images -q)

## Docker プロセスの確認
$ docker ps
CONTAINER ID   IMAGE               COMMAND                  CREATED              STATUS              PORTS                                         NAMES
631c45fe5298   nginx:1.13             "nginx -g 'daemon of…"   11 minutes ago   Up 11 minutes   80/tcp, 127.0.0.1:8000->8000/tcp      docker_django_nginx_1
b089f139536e   docker_django_python   "uwsgi --socket :800…"   11 minutes ago   Up 11 minutes   8001/tcp                              docker_django_python_1
15785fbd23d3   docker_django_db       "docker-entrypoint.s…"   11 minutes ago   Up 11 minutes   33060/tcp, 127.0.0.1:3307->3306/tcp   docker_django_db_1


# Step 1-1 Mysqlコンテナに入る
$ docker exec -it docker_django_db_1 sh
#

## Mysql のデータを確認する
# cd docker-entrypoint-initdb.d
# pwd
/docker-entrypoint-initdb.d
# ls
01_create_db.sql  02_db_create.sh  105_quake_tbl.sql_  108_quake_tbl.sql_  109_quake_tbl.sql_  112_quake_tbl.sql_  113_quake_tbl.sql_
# cat /etc/mysql/conf.d/my.cnf
   :

## 検測値テーブル（105_quake_tbl.sql .. 113_quake_tbl.sql）のリストア
# sh 02_db_create.sh
Mysql table creation Start
mysql: [Warning] Using a password on the command line interface can be insecure.
   :
mysql: [Warning] Using a password on the command line interface can be insecure.
Mysql table creation End

## MYSQL コンテナに入る
## Docker MySQL testdb ユーザー及びパスワードの確認
# mysql -u root -p
password:3#%KA
mysql> use testdb;
mysql> show tables;
+------------------+
| Tables_in_testdb |
+------------------+
| 105_quake        |
| 108_quake        |
| 109_quake        |
| 112_quake        |
| 113_quake        |
+------------------+
5 rows in set (0.00 sec)
mysql > ¥q

## Python コンテナに入る
$ docker ps
CONTAINER ID   IMAGE                  COMMAND                  CREATED             STATUS             PORTS                                                  NAMES
631c45fe5298   nginx:1.13             "nginx -g 'daemon of…"   11 minutes ago   Up 11 minutes   80/tcp, 127.0.0.1:8000->8000/tcp      docker_django_nginx_1
b089f139536e   docker_django_python   "uwsgi --socket :800…"   11 minutes ago   Up 11 minutes   8001/tcp                              docker_django_python_1
15785fbd23d3   docker_django_db       "docker-entrypoint.s…"   11 minutes ago   Up 11 minutes   33060/tcp, 127.0.0.1:3307->3306/tcp   docker_django_db_1


## Docker Python の動作確認
## Python コンテナに入る
$ docker exec -it docker_django_python_1 sh
# pwd
/code
# ls
app  test_docker.py  manage.py
# python test_docker.py


##  Djangoプロジェクトの作成
$ cd /docker_django
$ docker-compose run python django-admin.py startproject app .

## /apps/app/setting.py の変更
## MySQLとの接続設定 /apps/app/setting.py
import pymysql
pymysql.install_as_MySQLdb()

## database 設定をsqliteからMysql用に書き換え
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testdb',
        'USER': 'root',
        'PASSWORD': '3#%KA',
        'HOST': 'db',
        'PORT': '3306',
    }
}

## マイグレーションの実行
## Django 2.1.2 -> 3.1 version UP
$ cd /docker_django
$ docker-compose run python ./manage.py makemigrations
$ docker-compose run python ./manage.py migrate
Operations to perform:
   : 
  Applying sessions.0001_initial... OK
  
## 管理画面にログインユーザー等登録
$ docker-compose run python ./manage.py createsuperuser
Creating docker_django_python_run ... done
Username (leave blank to use 'root'): admin
Email address: admin@icloud.com
Password:admin12345
Password (again):admin12345
Superuser created successfully.

## webブラウザーで動作確認
$ docker-compose up -d
http://localhost:8000/  -> django Opening screen

```
# Django projectの作成
```bash
$ docker-compose exec app django-admin startproject test
※プロジェクト名の変更

## コンテナのリスタート
$ docker-compose down
$ docker-compose up -d

```
# Docker File : docker-compose.yml
```bash
# ============================================================
# docker-compose.yml (Django + MySQL) Ver 2021.06.23
# ============================================================
version: '3'

services:
  nginx: # WEBサーバのコンテナの設定
    image: nginx:1.13 # 使用するコンテナのイメージ名を記述
    ports:
      - "${IP}:8000:8000" # ホストの8000ポートとコンテナの8000ポートを接続します。IPは127.0.0.1を.env指定
    volumes:
      - ./docker/nginx/conf:/etc/nginx/conf.d # nginxの設定ファイルをマウントします。
      - ./docker/nginx/uwsgi_params:/etc/nginx/uwsgi_params # nginxの設定ファイルをマウントします。
      - ./static:/static # 静的ファイルのディレクトリをマウント
    tty: true            # 起動状態を維持
    depends_on:
      - python # アプリケーションサーバが起動してから起動させるため、アプリケーションサーバ用のコンテナとの依存関係を記述します。


  db:                              # DBサーバのコンテナの設定                                            
    build: ./docker/mysql          # ./docker/mysql/Dockerfileを使用してイメージをビルド
    container_name: mysql_db       # Docker Mysql の名称
    command: mysqld --character-set-server=utf8 --collation-server=utf8_unicode_ci
    ports:                         # IPは127.0.0.1を.envで指定
      - "${IP}:3307:3306"          # ホストの3307ポートとコンテナの3306ポートを接続  なお3306はホスト側mysqlのportとする
    environment:                   # 環境変数の設定を行います
      MYSQL_ROOT_PASSWORD: "${MYSQL_ROOT_PASSWORD}"   # パスワード.envに記載（docker-compose.ymlと同じ階層にある）
      TZ: 'Asia/Tokyo'             # タイムゾーンの設定
    volumes:
      - ./docker/mysql/my.cnf:/etc/mysql/conf.d/my.cnf   # mysql設定ファイルをマウント
      - ./docker/mysql/data:/var/lib/mysql               # データベースのデータを永続化するためにホストのボリュームをマウント
      - ./docker/sql:/docker-entrypoint-initdb.d         # データベースの設定ファイルをマウント
    tty: true                      # 起動状態を維持
          
  python:                          # アプリケーションサーバの設定
    build: ./docker/python         # ./docker/python/Dockerfileを使用してイメージをビルド
    container_name: python3
    command: uwsgi --socket :8001 --module app.wsgi --py-autoreload 1 --logto /tmp/mylog.log # コンテナ起動時のコマンド
    # command: python3 app/manage.py runserver 0.0.0.0:8000
    volumes:
      - ./apps:/code               # Django,Python projectコードをマウント
      - ./static:/static           # Django 静的ファイルディレクトリをマウント
      - ./data:/data               # projectデータ用ディレクトリをマウント
    environment:
      - "TZ=Asia/Tokyo"            # コンテナのtimezoneをJSTへ
    expose:
      - "8001"                     # 公開するポートの設定    

    tty: true                      # 起動状態を維持
    depends_on:
      - db                         # DBサーバとの接続の設定
```
# .env 
```bash
IP=127.0.0.1
MYSQL_ROOT_PASSWORD='3#%KA'

```
# MySQL Dockerfile
```bash
# ============================================================
# MySQL 5.7 Dockerfile Ver 2021.05.01
# ============================================================
FROM mysql:5.7
COPY entry/* /docker-entrypoint-initdb.d/
```
# Python Dockerfile
```bash
# ============================================================
# Dockerfile  Python 3.6 Dockerfile Ver 2021.06.23
# ============================================================
FROM python:3.6.6
RUN mkdir /code
WORKDIR /code
COPY /apps/requirements.txt /code
RUN pip install -r requirements.txt
COPY /apps /code

```
# Step 1-1 Mysqlコンテナに入る
```bash
$ docker ps
CONTAINER ID   IMAGE              COMMAND                  CREATED         STATUS          PORTS                                                  NAMES
631c45fe5298   nginx:1.13             "nginx -g 'daemon of…"   11 minutes ago   Up 11 minutes   80/tcp, 127.0.0.1:8000->8000/tcp      docker_django_nginx_1
b089f139536e   docker_django_python   "uwsgi --socket :800…"   11 minutes ago   Up 11 minutes   8001/tcp                              docker_django_python_1
15785fbd23d3   docker_django_db       "docker-entrypoint.s…"   11 minutes ago   Up 11 minutes   33060/tcp, 127.0.0.1:3307->3306/tcp   docker_django_db_1

## mysql コンテナの名称は mysql_db とした（名称は最後のNAMESに記載される）
## Docker mysql のコンテナに入る
$ docker exec -it docker_django_db_1 sh

## Mysql のデータを確認する
# cd docker-entrypoint-initdb.d
# pwd
/docker-entrypoint-initdb.d
# ls
01_create_db.sql  02_db_create.sh  105_quake_tbl.sql_  108_quake_tbl.sql_  109_quake_tbl.sql_  112_quake_tbl.sql_  113_quake_tbl.sql_
# cat /etc/mysql/conf.d/my.cnf
[client]                           # clientセクション: mysqlクライアントツールへの設定
# port=4306
# socket=/tmp/mysql.sock
default-character-set=utf8

[mysqld]                           # mysqldセクション: mysqlサーバーへの設定
# port=4306
# socket=/tmp/mysql.sock
# key_buffer_size=16M
character-set-server=utf8
collation-server=utf8_general_ci
max_allowed_packet=128M

[mysqldump]                        # mysqldumpセクション: バックアップコマンドへの設定
# quick

[mysqld_safe]                      # mysqld_safeセクション: 起動ファイル設定
# log-error=/var/log/mysqld.log

# MYSQL コンテナに入る
# testdb ユーザー及びパスワードの設定
# mysql -u root -p
password:3#%KA
# MYSQLコンテナ作成後、01_create_db.sqlは自動実行されているため
# 「testdb」の作成とユーザー作成実施済み.
# ---- testdb ユーザ作成 & testdb パスワード設定 の確認----
mysql> SELECT user, host FROM mysql.user;
+---------------+-----------+
| user          | host      |
+---------------+-----------+
| root          | %         |
| mysql.session | localhost |
| mysql.sys     | localhost |
| root          | localhost |
| testdb        | localhost |
+---------------+-----------+
5 rows in set (0.00 sec)
mysql > ¥q
Bye

## MYSQLコンテナ作成後、01_create_db.sqlは自動実行されているため
## 「testdb」の各テーブルもリストア済み.テーブルも確認.

# mysql -u testdb -p
Enter password:testdb
mysql> use testdb;
mysql> show tables;
+------------------+
| Tables_in_testdb |
+------------------+
| 105_quake        |
| 108_quake        |
| 109_quake        |
| 112_quake        |
| 113_quake        |
+------------------+
5 rows in set (0.00 sec)
mysql > ¥q

## もし、Docker MYSQLにtableがなければリストア（shellを起動）

# pwd
# cd /docker-entrypoint-initdb.d
# ls
01_create_db.sql  02_db_create.sh  105_quake_tbl.sql_  108_quake_tbl.sql_  109_quake_tbl.sql_  112_quake_tbl.sql_  113_quake_tbl.sql_

# sh 02_db_create.sh
## しばらく時間がかかる...
Mysql table creation Start
mysql: [Warning] Using a password on the command line interface can be insecure.
   :
mysql: [Warning] Using a password on the command line interface can be insecure.
Mysql table creation End

# mysql -u testdb -p
Enter password:testdb
mysql> use testdb;
mysql> show tables;
+------------------+
| Tables_in_testdb |
+------------------+
| 105_quake        |
| 108_quake        |
| 109_quake        |
| 112_quake        |
| 113_quake        |
+------------------+
5 rows in set (0.00 sec)

```
# 参考  MySQL
```bash
## Mysql コンテナに入ったのちに、mysql にログインできなかった場合の確認箇所
# mysql -u root -p
password:3#%KA

ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)

$ cd /docker_django
## docker-compose.yml ディレクトリに .env file が必要
$ echo "MYSQL_ROOT_PASSWORD='3#%KA'" > .env
$ cat .env
MYSQL_ROOT_PASSWORD='3#%KA'

(sql) 01_create_db.sql  コンテナ生成時にtestdbユーザーとtestdbデータベースを作成
# ---- testdb ユーザ作成 & testdb パスワード設定 ----
GRANT ALL ON testdb.* TO testdb@localhost identified by 'testdb';
# ---- testdb 作成 ----
create database testdb;

(shell) 02_db_create.sh
## データベースのリストア
mysql -u testdb -ptestdb testdb < 105_quake_tbl.sql_
 :
mysql -u testdb -ptestdb testdb < 113_quake_tbl.sql_

```
# 参考  Docker削除
```bash
削除前
$ docker system df
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          6         2         2.943GB   1.654GB (56%)
Containers      2         2         5.79kB    0B (0%)
Local Volumes   93        0         8.289GB   8.289GB (100%)
Build Cache     385       0         11.07GB   11.07GB

## 一括削除  https://qiita.com/takuma-jpn/items/455e911d77f8361cf0de
$ docker stop $(docker ps -q) | docker rm $(docker ps -aq) | docker rmi $(docker images -q)

削除後
$ docker system df
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          0         0         0B        0B
Containers      0         0         0B        0B
Local Volumes   93        0         8.289GB   8.289GB (100%)
Build Cache     30        0         841.8MB   841.8MB

```
# 参考  ローカルホストから DockerのMySQLに接続する方法
（https://www.it-swarm-ja.com/ja/mysql/ローカルホストからdocker-mysqlコンテナーに接続しますか？/1056012799/）
```bash
## DBコンテナの/etc/hostsを確認
$ docker exec -it docker_django_db_1 sh
# cat /etc/hosts
127.0.0.1	localhost
 : 
## ターミナルからDockerコンテナのmysqlに接続する
$ mysql -h 127.0.0.1 -P 3306 -u root -p
Enter password:3#%KA
mysql> show databases;
+------------------+
| Tables_in_testdb |
+------------------+
| 105_quake        |
|   :              |
+------------------+
5 rows in set (0.00 sec)
```
おわり


## 以下は参考、そのうちに整理
$ git remote -v
origin	vois@volmac02:git/docker_django.git (fetch)
origin	vois@volmac02:git/docker_django.git (push)

$ cat .git/config
[remote "origin"]
	url = vois@volmac02:git/docker_django.git
	fetch = +refs/heads/*:refs/remotes/origin/*

$ git remote set-url --add --push origin vois@volmac02:git/docker_django.git
## 一時的に github を 追加
$ git remote set-url --add --push origin https://github.com/zz1185qb/docker_django.git

$ cat .git/config
[remote "origin"]
	url = vois@volmac02:git/docker_django.git
	fetch = +refs/heads/*:refs/remotes/origin/*
	pushurl = vois@volmac02:git/docker_django.git
	pushurl = https://github.com/zz1185qb/docker_django.git


$ git remote -v
origin	vois@volmac02:git/docker_django.git (fetch)
origin	vois@volmac02:git/docker_django.git (push)
origin	https://github.com/zz1185qb/docker_django.git (push)

test test
test test
$ cat config 
[remote "origin"]
	url = vois@volmac02:git/eqchangepy.git
	fetch = +refs/heads/*:refs/remotes/origin/*

$ git remote -v
origin	vois@volmac02:git/eqchangepy.git (fetch)
origin	vois@volmac02:git/eqchangepy.git (push)

$ git remote set-url --add --push origin vois@volmac02:git/eqchangpy.git
$ git remote set-url --add --push origin https://github.com/zz1185qb/eqchangpy.git

$ git remote -v
origin	vois@volmac02:git/eqchangepy.git (fetch)
origin	vois@volmac02:git/eqchangpy.git (push)
origin	https://github.com/zz1185qb/eqchangpy.git (push)

[remote "origin"]
	url = vois@volmac02:git/eqchangepy.git
	fetch = +refs/heads/*:refs/remotes/origin/*
	pushurl = vois@volmac02:git/eqchangpy.git
	pushurl = https://github.com/zz1185qb/eqchangpy.git
