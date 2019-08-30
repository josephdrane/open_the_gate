#!/usr/bin/env python3

from config import Config


class Recipients(object):
    """Recipients"""

    def __init__(self, config: Config):
        self.recipients = {
            "Joe's Personal": config.joe_personal,
            "Joe's Work": config.joe_work,
            "Mary's Personal": config.mary_personal,
            # "Mary's Work": config.mary_work
        }
