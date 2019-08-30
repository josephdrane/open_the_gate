#!/usr/bin/env python3

from twilio.rest import Client
from config import Config
from openthegate.recipients import Recipients
from typing import Dict


class TwilioApi(object):
    """Share API and Recipient Data"""

    def __init__(self, config: Config):
        self.twilio_num: str = config.twilio_number
        self.account_sid: str = config.account_sid
        self.auth_token: str = config.auth_token
        self.client: Client = Client(self.account_sid, self.auth_token)
        self.get_recipients: Recipients = Recipients(config)
        self.recipients: Dict = self.get_recipients.recipients

    def gate_opened_notificiation(self) -> None:
        message = "OpenTheGate : Opened"
        self.__send_to_all_recipients(message)

    def confirm_gate_open_request(self) -> None:
        message = ("Open The Gate Request :\n"
                   "Reply Yes, to Open The Gate\n"
                   "Reply No, to Deny Request\n")
        self.__send_to_all_recipients(message)

    def __send_to_all_recipients(self, sms_message: str) -> None:
        for recipient in self.recipients:
            self.client.messages.create(body=sms_message,
                                        from_=self.twilio_num,
                                        to=self.recipients[recipient])
