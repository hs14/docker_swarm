import os

# MYSQL接続情報
mysql_user_name     = os.getenv('MYSQL_USER_NAME', 'root')
mysql_user_password = os.getenv('MYSQL_USER_PASSWORD', 'root') 
mysql_db_name       = os.getenv('MYSQL_DB_NAME', 'default')

# コンテナ情報
mysql_container_name = os.getenv('MYSQL_CONTAINER_NAME', 'default')
