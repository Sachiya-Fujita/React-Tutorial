import json

# Flask などの必要なライブラリをインポートする
from flask import Flask
from flask_cors import CORS
from flask import request, make_response, jsonify

# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)
# CORS (Cross-Origin Resource Sharing)
CORS(app)

# ここからウェブアプリケーション用のルーティングを記述
# index にアクセスしたときの処理
@app.route('/', methods=['GET'])
def show_user():
    response = {'user': {'name': 'index', 'age': 'hoge', 'job': 'web'}}
    return make_response(jsonify(response))

# /user にアクセスしたときの処理
@app.route('/user', methods=['GET'])
def show_user2():
    response = {'user': {'name': 'user', 'age': 'fuga', 'job': 'free'}}
    return make_response(jsonify(response))


if __name__ == '__main__':
    app.run()
