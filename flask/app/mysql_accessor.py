import MySQLdb
import env

class MysqlAccessor:

    def __init__(self, hostname, dbname, username, passwdstr):
        '''
        コンストラクタ
        MYSQLへ接続し、カーソルを取得する。
        '''
        self.conn = MySQLdb.connect(
            user = username,
            passwd = passwdstr,
            host = hostname,
            db = dbname
        )
        self.cur = self.conn.cursor()

    def execute_sql(self, sql):
        '''
        任意のSQL文を実行する。
        '''
        self.cur.execute(sql)
        return self.cur.fetchall()

    def end(self):
        '''
        終了処理
        '''
        self.cur.close
        self.conn.close


class UserAccessor:
    '''
    userテーブルへのアクセッサ
    必ずwith句で呼び出して使うこと
    '''

    def __init__(self, hostname):
        '''
        コンストラクタ
        ローカルからの実行とコンテナからの実行に対応するためにhostnameは引数指定
        '''
        self.accessor = MysqlAccessor(
            hostname, 
            env.mysql_db_name, 
            env.mysql_user_name, 
            env.mysql_user_password
        )
    
    def insert(self, id, username, address):
        '''
        データを登録する
        '''
        sql = f'INSERT INTO user VALUES ({id}, "{username}", "{address}")'
        self.accessor.execute_sql(sql)
    
    def search(self, column, value):
        '''
        データを検索する
        '''
        sql = f'SELECT * FROM user WHERE {column} LIKE "%{value}%"'
        return self.accessor.execute_sql(sql)

    def select_all(self):
        '''
        全件取得する
        '''
        sql = 'SELECT * FROM user'
        return self.accessor.execute_sql(sql)
    
    def delete_all(self):
        '''
        全件削除する
        '''
        sql = 'DELETE FROM user'
        self.accessor.execute_sql(sql)

    def __enter__(self):
        '''
        with句で呼び出すために用意
        なにもしない
        '''
        return self
    
    def __exit__(self, ex_type, ex_value, trace):
        '''
        withで呼び出した場合の終了処理
        '''
        self.accessor.conn.commit()
        self.accessor.end()


if __name__ == '__main__':
    pass
