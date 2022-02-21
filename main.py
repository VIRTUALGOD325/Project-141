from flask import Flask,jsonify,request
from storage import all_articles,liked_articles,did_not_read,not_liked_articles

app = Flask(__name__)

@app.route('/get-article')
def get_movies():
    data = {
        "title":all_articles[0][19],
        "poster_link":all_articles[0][27],
        "release_date":all_articles[0][13] or ' N/A ',
        "duration":all_articles[0][15],
        "rating":all_articles[0][20],
        "overall_rating":all_articles[0][9] 
    }
    return jsonify({
        "data":data, 
        "status":"sucess"
    },200)

@app.route('/liked-article',methods=['POST'])
def liked_articles(): 
    movie = all_articles[0]
    liked_articles.append(movie)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    },200)

@app.route('/unliked-article', methods=['POST'])
def unliked_articles():
    article = all_articles[0]
    not_liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status":"success"
    },200)

@app.route('/did-not-read',methods=['POST'])
def did_not_read(): 
    article = all_articles[0]
    did_not_read.append(article)
    all_articles.pop(0)
    return jsonify({
        "status":"success"
    },200) 
