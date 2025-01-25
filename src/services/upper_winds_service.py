from pymongo import MongoClient
from src.config import settings
import re
import json

# Define a regex pattern for valid ICAO codes
ICAO_CODE_PATTERN = re.compile(r"^[A-Z]{4}$")


class UpperWindsService:
    def __init__(self):
        self.client = MongoClient(settings.mongodb_url)

    def get_database(self, icao_code: str):
        return self.client[icao_code]

    def get_upper_winds_data(self, icao_code: str):
        db = self.get_database(icao_code)
        collection = db["upper_winds"]
        data = list(collection.find({}, {"_id": 0}))  # Exclude the MongoDB _id field
        return data

    def get_all_stations(self):
        stations = self.client.list_database_names()
        return [station for station in stations if ICAO_CODE_PATTERN.match(station)]

    def get_all_upper_winds_data(self):
        all_data = []
        for db_name in self.get_all_stations():
            db = self.get_database(db_name)
            collection = db["upper_winds"]
            data = list(
                collection.find({}, {"_id": 0})
            )  # Exclude the MongoDB _id field
            all_data.extend(data)
        return all_data


# Instantiate the service
upper_winds_service = UpperWindsService()
