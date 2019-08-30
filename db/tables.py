#!/usr/bin/env python3

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TextVerification(Base):
    __tablename__ = 'text_verification'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    sms_response = Column(String(50), nullable=True)
    response_received = Column(String(50), nullable=True)
