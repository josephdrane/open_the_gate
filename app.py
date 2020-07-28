#!/usr/bin/env python3

from config import Config as OpenGateAppConfig
from db.session import Session
from db.cosmos import Cosmos
from flask import Flask, render_template, request
from openthegate.twilio_api import TwilioApi
from time import sleep
from twilio import twiml
from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import VoiceResponse, Gather


app = Flask(__name__)
app.secret_key = "super_secret_key"
opengateapp_config = OpenGateAppConfig()
# db = Session(opengateapp_config)
db = Cosmos(opengateapp_config)


@app.route("/voice/", methods=['GET', 'POST'])
def voice():
    response = VoiceResponse()
    twilio_api = TwilioApi(opengateapp_config)
    twilio_api.confirm_gate_open_request()
    response.redirect('/verify/')
    return str(response)


@app.route('/verify/', methods=['GET', 'POST'])
def verify():
    twilio_api = TwilioApi(opengateapp_config)

    if db.get_response_received() == False:
        response = VoiceResponse()
        response.redirect("/verify/")
        return str(response)

    response = db.get_sms_response()
    if response == "Yes":
        response = VoiceResponse()
        response.play("", digits="ww9")
        twilio_api.gate_opened_notificiation()
        db.reset_response()
        return str(response)

    elif response == "No":
        response = VoiceResponse()
        response.say("Denied")
        db.reset_response()
        return str(response)

    else:
        response = VoiceResponse()
        response.redirect('/verify/')
        return str(response)


@app.route("/sms/", methods=['GET', 'POST'])
def inbound_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    print('Body :', body)
    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body.lower() == "yes":
        db.set_sms_response("Yes")
        db.set_response_received()
        resp.message("Ok, I will let them in for you. :)")


    elif body.lower() == "no":
        db.set_sms_response("No")
        db.set_response_received()
        resp.message("Ok, I will deny access. :)")


    else:
        resp.message("I'm sorry I do not understand. Try Yes or No")

    print("Response String : ", str(resp))
    return str(resp)


@app.route("/")
def homePage():
    return render_template("home.html")


if __name__ == "__main__":
    # THIS IS USED FOR DEVELOPMENT ONLY, PROD USES GUNICORN
    import os
    app.secret_key = "super_secret_key"
    app.debug = True
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
