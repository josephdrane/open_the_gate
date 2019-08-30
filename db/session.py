#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.tables import TextVerification
from sqlalchemy import update
from config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.tables import Base


class Session(object):
    def __init__(self, config: Config):
        self.engine = create_engine(config.db_url)
        self.DBSession = sessionmaker(bind=self.engine)
        self.session = self.DBSession()
        Base.metadata.create_all(self.engine)
        Base.metadata.bind = self.engine
        self.__db_setup()

    def __add_or_update_record(self, record):
        self.session.add(record)
        self.session.commit()
        self.session.refresh(record)

    def __db_setup(self):
        db = TextVerification(sms_response="None", response_received="False")
        self.__add_or_update_record(db)

    def get_response_received(self) -> bool:
        db = self.session.query(TextVerification).filter_by(id=1).one()
        return db.response_received

    def get_sms_response(self) -> str:
        db = self.session.query(TextVerification).filter_by(id=1).one()
        return db.sms_response

    def set_response_received(self):
        db = self.session.query(TextVerification).filter_by(id=1).one()
        db.response_received="True"
        self.__add_or_update_record(db)

    def set_sms_response(self, yes_or_no):
        db = self.session.query(TextVerification).filter_by(id=1).one()
        db.sms_response=yes_or_no
        self.__add_or_update_record(db)

    def reset_response(self):
        db = self.session.query(TextVerification).filter_by(id=1).one()
        db.sms_response="None"
        db.response_received="False"
        self.__add_or_update_record(db)
