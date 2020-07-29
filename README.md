# Open The Gate

## About

Gated communities are a bit out dated where they only dial one number. This app helps me solve that problem by putting a Twilio API number that the gate key pad dials. This then texts several numbers where we can respond yes or no based on if we are expecting someone or not. 

## Challenges

- Getting the flask server to wait to respond back to the voice call. This was a bit of trial and error. 
- Wife did not like me playing loud annoying sounds if we denied access. (Someone using our code wihtout our knowledge).
- I had this installed on Heroku w/ Heroku Postgres but Twilio has a 15 second timeout on HTTP requests. This would cause a timeout. If you want heroku or install somewhere else then go for it.
- pipenv - this thing when it worked was great but then it just stopped working and sucks.

## The Stack

- Python
- Flask
- Twilio
- Bootstrap 4.1
- Azure Cosmo Mongo DB
- Azure App Service

## Setup in Twilio

- Programmable Messaging > Messaging Services > Create Messaging Service
INBOUND REQUEST CONFIG = <domain-name>/sms/
- Phone Numbers > Manage Numbers > Active Numbers > A Call Comes In > Webhook > <domain-name>/voice/
- Inside [alert.py](https://github.com/josephdrane/OpenTheGate/blob/master/alert.py) you'll need to update w/ twilio API credentials and your contact list for text notifications.

## Want to help make this better?

Start by picking up an [issue](https://github.com/josephdrane/OpenTheGate/issues) and working on resolving or setting up. Thanks in advance!
