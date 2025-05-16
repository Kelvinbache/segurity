import mysql.connector as myBase

db = myBase.connect(
    user="root",
    password="iqMICI@GopLHISN!",
    host='localhost',
    port=3306
)

fromData = db.cursor()

myls = fromData.excuse("show databases")

for i in myls:
    print(i)

# finish the connection with the base data


