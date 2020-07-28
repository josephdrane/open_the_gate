from bson.objectid import ObjectId
from config import Config
from pymongo import MongoClient

class Cosmos:
    state_id = ObjectId('5f20975e5e6eadfcabc29dc5')
    query = {"_id": state_id}
    default_state = {
        "sms_response": "None", 
        "response_received": False
    }

    def __init__(self, config: Config) -> None:
        self.client = MongoClient(config.mongo_db_uri)
        self.open_the_gate_db = self.client.open_the_gate
        self.db = self.open_the_gate_db.open_the_gate

    def get_response_received(self) -> bool:
        db = self.db.find_one(self.query)
        return db["response_received"]

    def get_sms_response(self) -> str:
        db = self.db.find_one(self.query)
        return db["sms_response"]

    def set_response_received(self):
        set_response_received = { "$set": { "response_received": True } }
        self.db.update_one(self.query, set_response_received)

    def set_sms_response(self, yes_or_no):
        set_sms_response = { "$set": { "sms_response": "Yes" } }
        self.db.update_one(self.query, set_sms_response)

    def reset_response(self):
        reset_response = { "$set": 
            { "sms_response": "None", "response_received": False } 
        }
        self.db.update_one(self.query, reset_response)