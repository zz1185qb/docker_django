# Docker 開発環境の構築
```bash
# docker_django : DjangoのDocker開発環境(Nginx + Python + MySQL) 
# GitHub アップロードのテスト
# ----------------------------------------------------------------
# 動作環境
# Docker Desktop Mac 3.3.3
# docker-compose version 1.29.1
# Python 3.6.6
# Django 3.0.7
# Mysql  5.7
# Last Change: 2021/07/13 02:42:43.
# ----------------------------------------------------------------
$ git clone https://github.com/zz1185qb/docker_django.git
$ cd docker_django
$ docker-compose up -d --build
$ docker ps
CONTAINER ID   IMAGE                  COMMAND                  CREATED       STATUS       PORTS                                                  NAMES
9f360eb46e65   nginx:1.13             "nginx -g 'daemon of…"   2 hours ago   Up 2 hours   80/tcp, 0.0.0.0:8000->8000/tcp, :::8000->8000/tcp      docker_django_nginx_1
47032c46a434   docker_django_python   "uwsgi --socket :800…"   2 hours ago   Up 2 hours   8001/tcp                                               docker_django_python_1
c72336718a3d   docker_django_db       "docker-entrypoint.s…"   2 hours ago   Up 2 hours   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   docker_django_db_1

Docker開発環境の構築完了。
その後、設定ディレクトリにProjectやDataを配置。

★★★ 上記のDocker環境の構築にあたり参考にさせていただいたコンテンツ ★★★
https://hackerdemy.com/2019/09/09/docker-django/


```
おわり






