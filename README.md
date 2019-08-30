# Open The Gage

**WHY?**
Automate opening the gate in my community.
The front gate has a keypad that will dial a phone number.
Whoever answers that phone can open the gate by pressing 9.
Usually this process is annoying because we miss the calls usually.
So we automate just opening it for whomever will dial it.

## The Stack

- Python 3.7.2
- Flask
- twilio
- Bootstrap 4.1


## How to run locally

You won't be able to test receiving a call but you can send a text running local.

1. git clone this repo (recommend forking and modifying for your needs)
2. Install [Python3](https://www.python.org/downloads/)
3. Install [pipenv](https://pipenv.readthedocs.io/en/latest/) (I use this for virtual environments)
```
pip3 install pipenv
```
4. Setup a virtual environment for Python 3
```
pipenv install --three
```
5. Install all dependencies from [Pipfile](https://github.com/josephdrane/OpenTheGate/blob/master/Pipfile)
```
pipenv sync
```
6. Activate the virtual environment
```
pipenv shell
```
7. Run the app:
```
python3 app.py
```
8. Test the app by going to [local host port 8000](http://localhost:8000).

## Deploy onto Heroku

Currently setup for deployment onto [Heroku](https://heroku.com).
That's what the [Procfile](https://github.com/josephdrane/OpenTheGate/blob/master/Procfile) is for.

## Setup in Twilio

Basically you'll need to get an account and a number that supports voice and sms.
Inside [alert.py](https://github.com/josephdrane/OpenTheGate/blob/master/alert.py) you'll need to update w/ twilio API credentials and your contact list for text notifications.
You'll then need to deploy to heroku and tell twilio the URL to reach our heroku server.

## Want to help make this better?

Start by picking up an [issue](https://github.com/josephdrane/OpenTheGate/issues) and working on resolving or setting up. Thanks in advance!
