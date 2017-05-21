from flask import Flask, jsonify
from flask import request
import jieba.analyse
from bs4 import BeautifulSoup

app = Flask(__name__)

jieba.set_dictionary('./res/dict.txt.big')
jieba.analyse.set_stop_words('./res/stop_words.txt')
jieba.analyse.set_idf_path('./res/idf.txt.big')


@app.route("/")
def home():
    return "flask"


def clean_content(s):
    return BeautifulSoup(s).text


@app.route("/tags", methods=['POST'])
def tags():
    top = request.form.get('top', '10')
    content = request.form['content']
    content = clean_content(content)
    tags = jieba.analyse.extract_tags(content, topK=int(top))
    return jsonify(tags)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
