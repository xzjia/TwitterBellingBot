import webapp2
import tweepy, time, sys
import datetime
from keys import keys



MAIN_PAGE_HTML = """\
<html>
<head>
<title>Belling Bot</title>
</head>
<body>
<h3>Belling Bot</h3>
<p>This is the home of <a href="https://twitter.com/BellingBot">@BellingBot</a>.
I'm a Twitter 'bot that bells every other hour SHARP.
There's not too much to see here.
Bother to <a href="https://twitter.com/JiaXiaozhou">@JiaXiaozhou</a> if you find it's not working correctly.
</body>
</html>
"""


class BellingBot(webapp2.RequestHandler):

    def generate(self):
        utc = datetime.datetime.now()
        delta = datetime.timedelta(hours=9)
        t = utc + delta
        if t.hour <= 12:
            ringing = "Bang!!! " * t.hour 
        else:
            ringing = "Bang!!! " * (t.hour - 12)

        readable_time = t.strftime('%Y-%m-%d %H:%M')
        saying = "It's now " + readable_time + " in Tokyo."
        return saying + " Here comes the (be) bellingS (careful): " + ringing 

    def tweet(self, status):
        CONSUMER_KEY = keys['consumer_key']
        CONSUMER_SECRET = keys['consumer_secret']
        ACCESS_KEY = keys['access_token']
        ACCESS_SECRET = keys['access_token_secret']

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)
        api.update_status(status)
    
    def get(self):
        status = self.generate()
        # self.tweet(status)
        self.response.write(status)


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)



application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/BellingBot', BellingBot)
], debug=True)





