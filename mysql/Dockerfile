FROM mysql:8

# ポート3306
EXPOSE 3306

# 設定ファイルをコピー
ADD ./my.cnf /etc/mysql/conf.d/my.cnf

# MySQLの起動
CMD ["mysqld"]
