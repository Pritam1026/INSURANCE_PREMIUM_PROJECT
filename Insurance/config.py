import pymongo
import pandas as pd
import numpy as np
import json
import os
import sys
from dataclasses import dataclass
from dotenv import load_dotenv
load_dotenv()

@dataclass
class EnvironmentVariable:
    mongo_db_url=os.getenv("MONGO_DB_URL")

env_variable=EnvironmentVariable()
mongo_client=pymongo.MongoClient(env_variable.mongo_db_url)

TARGET_COLUMN='expenses'