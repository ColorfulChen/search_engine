from flask import Flask, render_template, request, jsonify
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
GOOGLE_API_KEY = os.getenv("GOOGLE_API")
CX = os.getenv("CX")

badwords = ["天安门","台湾","新疆","Taiwan","Xinhua"]  # 你可以自行扩展

def contains_badword(text):
    if not text:
        return False
    for word in badwords:
        if word in text:
            return True
    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('q', '')
    start = request.args.get('start', 1, type=int)
    if not query:
        return jsonify({'items': []})
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_API_KEY,
        "cx": CX,
        "q": query,
        "start": start
    }
    response = requests.get(url, params=params)
    results = response.json()
    items = results.get("items", [])
    # 过滤违禁词，标记含违禁词的条目
    for item in items:
        flagged = False
        for field in (item.get("title"), item.get("snippet")):
            if contains_badword(field):
                flagged = True
                break
        item["flagged"] = flagged
    return jsonify(items)

if __name__ == "__main__":
    app.run(debug=True)
