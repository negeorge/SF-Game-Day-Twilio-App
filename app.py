from flask import Flask, request, redirect
import twilio.twiml
import os
app = Flask(__name__)
 
@app.route("/")
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
 
    resp = twilio.twiml.Response()
    resp.sms("Hi From Nisha's app")
    return str(resp)
 
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)