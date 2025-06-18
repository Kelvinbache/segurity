import os 
from dotenv import load_dotenv

load_dotenv()


config_data={
    "DB": os.environ.get("KEY_DB"),
    "TOKEN":os.environ.get("KEY_TOKEN")
}



