from pymongo import MongoClient
from src.config import settings
import re
import json
from datetime import datetime

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

    def get_upper_winds_data_by_date(self, icao_code: str, date_str: str):
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
            db = self.get_database(icao_code)
            collection = db["upper_winds"]
            # Use regex to match the date part of the datetime field
            regex_pattern = f"^{date.isoformat().split('T')[0]}"
            print(regex_pattern)
            return list(
                collection.find({"datetime": {"$regex": regex_pattern}}, {"_id": 0})
            )
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

    def get_upper_winds_data_by_date_range(
        self, icao_code: str, start_date_str: str, end_date_str: str
    ):
        try:
            # start_date = datetime.strptime(start_date_str, "%Y-%m-%d").isoformat()
            # end_date = (
            #     datetime.strptime(end_date_str, "%Y-%m-%d")
            #     .replace(hour=23, minute=59, second=59, microsecond=999999)
            #     .isoformat()
            # )
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
            start_date_iso = start_date.isoformat() + "T00:00:00.0000"
            end_date_iso = end_date.isoformat() + "T23:59:59.9999"
            print("start_date", start_date_iso, "end_date", end_date_iso)
            db = self.get_database(icao_code)
            collection = db["upper_winds"]
            print(
                list(
                    collection.find(
                        {"datetime": {"$gte": start_date_iso, "$lt": end_date_iso}},
                        {"_id": 0},
                    )
                )
            )
            return list(
                collection.find(
                    {"datetime": {"$gte": start_date_iso, "$lt": end_date_iso}},
                    {"_id": 0},
                )
            )
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")


# Instantiate the service
upper_winds_service = UpperWindsService()
