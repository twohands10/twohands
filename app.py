from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi
client = MongoClient('mongodb+srv://test:sparta@cluster0.i565z.mongodb.net/Cluster0?retryWrites=true&w=majority',tlsCAFile=certifi.where())
db = client.dbsparta


@app.route('/')
def detail():
    return render_template("detail.html")

#url이 shop이고, post 방식으로 입력란의 정보들이 DB로 이동
@app.route("/review", methods=["POST"])
def review_post():
    review_receive = request.form['review_give']
    review_list = list(db.review.find({}, {'_id': False}))
    count = len(review_list) + 1

    doc = {
        'num': count,
        'review': review_receive
    }
    db.review.insert_one(doc)
    return jsonify({'msg': '등록 완료!'})

#url이 shop이고, get 방식으로 전체 shoplist를 보여주기
@app.route("/review", methods=["GET"])
def review_get():
    review_list = list(db.review.find({}, {'_id': False}))
    return jsonify({'reviews': review_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)