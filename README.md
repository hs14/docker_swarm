# docker_swarm

### 概要
Docker Swarmを使ってFlaskとMySQLで簡易的なWeb API環境を構築

### 構築手順
dindコンテナを立てる
```
cd {クローンしたフォルダ}
docker-compose up -d
```
docker container exec -it manager docker swarm init

Swarmクラスタを有効化する
```
docker container exec -it manager docker swarm init

docker container exec -it worker_db docker swarm join ^
--token {上記で表示されたトークン} manager:2377

docker container exec -it worker_ap docker swarm join ^
--token {上記で表示されたトークン} manager:2377

docker container exec -it worker_web docker swarm join ^
--token {上記で表示されたトークン} manager:2377
```

Swarmクラスタの構築の確認、およびコンテナ名の確認
```
docker container exec -it manager docker node ls
docker container ls
```

Visualizerのデプロイ (http://localhost:9000 でアクセスできる)
```
docker container exec -it manager docker stack deploy -c ./stack/visualizer.yml visualizer
```

スタック間通信用のネットワーク作成
```
docker container exec -it manager docker network create --driver=overlay --attachable swarm_api_network
```

Dockerイメージのビルドとregistryへのプッシュ (スタック内でインターネット越しにイメージ取得ができないため)
```
docker build -t webapi/mysql:latest mysql
docker build -t webapi/flask:latest flask
docker build -t webapi/apache:latest apache

docker image tag webapi/mysql:latest localhost:5000/webapi/mysql:latest
docker image tag webapi/flask:latest localhost:5000/webapi/flask:latest
docker image tag webapi/apache:latest localhost:5000/webapi/apache:latest

docker image push localhost:5000/webapi/mysql:latest
docker image push localhost:5000/webapi/flask:latest
docker image push localhost:5000/webapi/apache:latest
```

スタックのデプロイ
```
docker container exec -it manager docker stack deploy -c ./stack/db.yml db
docker container exec -it manager docker stack deploy -c ./stack/ap.yml ap
docker container exec -it manager docker stack deploy -c ./stack/web.yml web
```

スケールアウト
```
docker container exec -it manager docker service scale ap_flask=2
docker container exec -it manager docker service scale web_apache=2
```

クラスタ外からの通信許可
```
docker container exec -it manager docker stack deploy -c ./stack/proxy.yml proxy
```

### API仕様
#### データ登録
以下の形式で、ユーザID、ユーザ名、ユーザの住所の情報を登録できる。
ASCIIのみ対応。
```
curl -X POST http://localhost:8000/user?id={ユーザID}\&username={ユーザ名}\&address={ユーザの住所}
```

#### データ検索
以下の形式で、ユーザ名をキーに、ヒットしたユーザ全員をJSON形式で取得できる。
ユーザ名は曖昧検索で検索される。
```
curl -X GET http://localhost:8000/user?username={検索語}
```
