import mysql.connector as myBase

db = myBase.connect(
    use_pure=True,
    host='localhost',
    user="root",
    password="iqMICI@GopLHISN!",
    database="segurity"
)


# export 


# sql = ("insert into usuario" "(nombre, apellido,email,telefono)" "values(%s,%s,%s,%s)")
# insertData = ('kelvin','abache','kelvinabache@gamil.com','041265654564')

# cursors.execute(sql,insertData)

# # split method
# cursors.execute("select * from usuario")
# mySql = cursors.fetchall()

# db.commit()

# cursors.close()
# db.close()

# for i in mySql:
#     print(i)

# finish the connection with the base data


