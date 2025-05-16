from model.Models import Person
from config.mySql import db


def methodPost(person:Person):
        cursors = db.cursor() 
        sql = ("insert into usuario" "(nombre, apellido,email,telefono)" "values(%s,%s,%s,%s)")
        insertData = (person.name,person.lastName,person.email,person.phone)
        cursors.execute(sql,insertData)
        db.commit()
        return {"message":"submit data with exit"}  