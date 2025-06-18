import mysql.connector as myBase
from config.config import config_data


db = myBase.connect(
    use_pure=True,
    host='localhost',
    user="root",
    password=config_data["DB"],
    database="segurity"
)

