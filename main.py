from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob


#---------------------------------------------------------------------------

consumer_key = 'rdwiLwtI7YFIjVgH4g7jlQCS8'
consumer_secret = 'OsNbPNWWvxmgoZrokDdM3lWpsVyyVAiCiuSdsmWVurGfQaW4Tp'

access_token = '1512095320330543106-Frrgfyo6RDm49e1MJ2esgGIiBDwuqZ'
access_token_secret = '2Yq8W71giOaJQnxwyjWHeDGNPAGyfN9OIpkA1mQTig5bk'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#-------------------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    
    t = []
    tweets = api.search(search_tweet, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])
        # t.append(tweet.full_text)

    return jsonify({"success":True,"tweets":t})

app.run()
