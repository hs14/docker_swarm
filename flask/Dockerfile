FROM python:3.6

# ポート8000
EXPOSE 8000

# 読み込むライブラリのリストをコピー
ADD ./requirements.txt /var/piplib/requirements.txt
ADD ./app /var/app

# ライブラリのインストール
RUN pip install -r /var/piplib/requirements.txt

# アプリの実行
CMD ["python", "/var/app/main.py"]
