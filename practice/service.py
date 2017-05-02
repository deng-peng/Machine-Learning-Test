from flask import Flask, jsonify
from flask import request
import jieba.analyse

app = Flask(__name__)
jieba.analyse.set_stop_words('../res/stop_words.txt')


@app.route("/")
def home():
    return "flask"


@app.route("/tags", methods=['GET', 'POST'])
def tags():
    content = request.data
    tags = jieba.analyse.extract_tags(content, topK=10)
    return jsonify(tags)


if __name__ == "__main__":
    app.run()
