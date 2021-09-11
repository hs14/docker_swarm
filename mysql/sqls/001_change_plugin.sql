-- 以下のエラー対策として、rootユーザの認証プラグインを変更する
-- 'Plugin caching_sha2_password could not be loaded: /usr/lib/x86_64-linux-gnu/mariadb19/plugin/caching_sha2_password.so: cannot open shared object file: No such file or directory'

ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'root';
