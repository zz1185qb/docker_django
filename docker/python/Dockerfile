# ============================================================
# Dockerfile  Python 3.9 Dockerfile Ver 2021.06.23
# ============================================================
# ベースとなるイメージの指定
FROM python:3.6.6
RUN mkdir /code
WORKDIR /code

# インストールするライブラリを記述したファイル（requirements.txt）をコピー
COPY requirements.txt /code/
# ファイルに記載されたライブラリをインストールするためのコマンド
RUN pip install --upgrade pip
RUN pip install --upgrade setuptls
RUN pip install -r requirements.txt
ADD . /code/
# COPY /apps /code