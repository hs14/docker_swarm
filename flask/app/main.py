import json
from flask import Flask, request
from mysql_accessor import UserAccessor
import env

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return 'Hello World!'


@app.route('/user', methods=["GET"])
def search():
    try:
        # パラメータの取得
        username_val = request.args.get('username')

        # 値を取得して返却
        vals = []
        with UserAccessor(env.mysql_container_name) as accessor:
            rows = accessor.search('username', username_val)
            for row in rows:
                dict = {}
                dict['id'] = row[0]
                dict['username'] = row[1]
                dict['address'] = row[2]
                vals.append(dict)

        encode_json_data = json.dumps(vals)
        return encode_json_data

    except Exception as e:
        error_message = 'type: ' + str(type(e)) + '\n' \
                          + 'args: ' + str(e.args) + '\n'
        return error_message


@app.route('/user', methods=["POST"])
def register():
    try:
        # パラメータの取得
        id_val       = request.args.get('id')
        username_val = request.args.get('username')
        address_val  = request.args.get('address')

        # 値を取得して返却
        with UserAccessor(env.mysql_container_name) as accessor:
            accessor.insert(id_val, username_val, address_val)
            return "success"

    except Exception as e:
        error_message = 'type: ' + str(type(e)) + '\n' \
                          + 'args: ' + str(e.args) + '\n'
        return error_message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
