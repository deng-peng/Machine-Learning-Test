from flask import Flask, jsonify
from flask import request
import jieba.analyse
from bs4 import BeautifulSoup

app = Flask(__name__)

jieba.set_dictionary('/var/www/FlaskApp/FlaskApp/res/dict.txt.big')
jieba.analyse.set_stop_words('/var/www/FlaskApp/FlaskApp/res/stop_words.txt')
jieba.analyse.set_idf_path('/var/www/FlaskApp/FlaskApp/res/idf.txt.big')


@app.route("/")
def home():
    return "flask"


def clean_content(s):
    soup = BeautifulSoup(s, 'html.parser')
    for script in soup(["script", "style"]):
        script.extract()
    return soup.get_text()


@app.route("/tags", methods=['POST'])
def idf_tags():
    req = request.get_json(force=True)
    top = 10
    if 'top' in req:
        top = req['top']
    response = {}
    for key in req['list']:
        content = clean_content(req['list'][key])
        tags = {}
        for x, y in jieba.analyse.extract_tags(content, topK=int(top), withWeight=True):
            tags[x] = y
        response[key] = tags
    return jsonify(response)


@app.route("/tags/textrank", methods=['POST'])
def rank_tags():
    req = request.get_json(force=True)
    top = 10
    if 'top' in req:
        top = req['top']
    response = {}
    for key in req['list']:
        content = clean_content(req['list'][key])
        tags = {}
        for x, y in jieba.analyse.textrank(content, topK=int(top), withWeight=True):
            tags[x] = y
        response[key] = tags
    return jsonify(response)


if __name__ == "__main__":
    app.run()
