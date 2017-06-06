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
    top = request.form.get('top', '10')
    content = request.form['content']
    content = clean_content(content)
    tags = jieba.analyse.extract_tags(content, topK=int(top))
    return jsonify(tags)


@app.route("/tags/textrank", methods=['POST'])
def rank_tags():
    top = request.form.get('top', '10')
    content = request.form['content']
    content = clean_content(content)
    tags = []
    for x, y in jieba.analyse.textrank(content, topK=int(top), withWeight=True):
        tags.append(x)
    return jsonify(tags)


if __name__ == "__main__":
    app.run()
