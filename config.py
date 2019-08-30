#!/usr/bin/env python3

import os


class Config(object):
    def __init__(self):
        self.db_url: str = os.environ["DATABASE_URL"]
        self.twilio_number: str = os.environ["TWILIO_NUMBER"]
        self.account_sid: str = os.environ["ACCOUNT_SID"]
        self.auth_token: str = os.environ["AUTH_TOKEN"]
        self.joe_personal: str = os.environ["JOE_PERSONAL"]
        self.joe_work: str = os.environ["JOE_WORK"]
        self.mary_personal: str = os.environ["MARY_PERSONAL"]
        self.mary_work: str = os.environ["MARY_WORK"]
