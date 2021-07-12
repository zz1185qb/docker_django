# ---- ユーザの確認 ----
# select user, host from mysql.user;
# ---- testdb ユーザ作成 & testdb パスワード設定 ----
GRANT ALL ON testdb.* TO testdb@localhost identified by 'testdb';
create database testdb;

# MySQL 5.7以前パスワード設定 / 変更
# SET PASSWORD FOR 'testdb'@'loaclhost' IDENTIFIED BY 'testdb';


