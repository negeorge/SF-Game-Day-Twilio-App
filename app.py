import os
import json
import datetime

from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)
app.debug = True

schedule = json.load(open('giants2012schedule.json'))
@app.route("/")
def game_schedule():
    """Respond to incoming sms with if there is a game."""
    resp = twilio.twiml.Response()
    todays_date = datetime.datetime.now().strftime("X%m/X%d/%Y")
    todays_date = todays_date.replace('X0','X').replace('X', '')
    
    for game in schedule['games']:
        if todays_date == game['date']:
            resp.sms("Giants Game Today! :-) %s %s %s - by http://inish.org" % (game['time'], game['opponent'], game['location']))
            return str(resp)
			
    resp.sms("No Giants Game Today :-( - by http://inish.org")
    return str(resp)
 
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)