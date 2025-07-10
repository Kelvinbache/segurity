from config.mySql import db

from fastapi import Cookie, HTTPException

from typing import Annotated

from datetime import (datetime,timezone,timedelta)

import mysql.connector 

cursors = db.cursor() 
  

def validateUser(user:str):

    #    sql = ("select id, nombre, password from usuario")
       sql_two = ("select * from usuario a inner join cuenta b on a.id = b.usuario_id")
         
    #    cursors.execute(sql)
       cursors.execute(sql_two)

       mys = cursors.fetchall()
       result = list(filter(lambda data_base: data_base[1] == user.name and data_base[2] == user.password, mys)) #A partir de aqui debemos hacer una condicion que nos valide el usuario
                      
       if result:
             for data in result: 
                 return data
       else:
          return None


#Buscar la buenta del cliente
def sql_get_amount_currents(user:Annotated[str | None, Cookie()] = None):

      if user is None:
         raise HTTPException(status_code=404, detail="cookie not found")
         
      else:
         
          sql_get_amount_current=("select saldo from cuenta where id_cuenta = %s ") # deberiamos hacer una sola consuta  
          cursors.execute(sql_get_amount_current, (user,))
          mys=cursors.fetchone()
         
          return {"amount":mys[0], "user":user}
           
# Algunas cosas que ahi que cambiar:
# Ajustar la hora para nuestro pais
# !Ajustar que la cookies se envien por todo el programa, para evitar que solo se usen en una ruta
# El dispositovo esta de mas, porque eso debemos hacerlo aparte solo centrate en la parte de vericar los datos

#Funcion donde podamos pasar los datos de donde vamos a enviar el dinero, y vericar si existe 
def verify_the_customer(data_customer:str):

    id_user=0

    sql=("select * from data_user a inner join cuenta b on a.usuario_id = b.usuario_id")
    
    cursors.execute(sql)
    
    mys=cursors.fetchall()
    
    result = list(filter(lambda data_base: data_base[3] == data_customer.dni or data_base[4] == data_customer.phone, mys))
     
    for data in result:
        id_user = data[7]
    
    return id_user

def method_transaction(data_transaction:dict, customer:dict):
          
     id_account = verify_the_customer(data_transaction)

     if data_transaction.moto > customer["amount"]:
         raise HTTPException(status_code=400, detail="insufficient funds")
     else:     

          date_time_of_day = datetime.now(timezone.utc) + timedelta(minutes=15)

          sql = ("insert into transaccion" "(tipo_transaccion, fecha_hora, monto, cuenta_id, dispositivo_id)" "values(%s,%s,%s,%s,%s)")

          sql_update_account=("update cuenta set saldo = %s where id_cuenta = %s")
         
          insert = (data_transaction.typeTransaction, date_time_of_day, data_transaction.moto, id_account, data_transaction.id_device) 

          insert_update = (data_transaction.moto, id_account)
          
          money= customer["amount"] - data_transaction.moto
          
          updating_the_losing_account=(money,customer["user"])

          try:
     
              cursors.execute(sql,insert)
              cursors.execute(sql_update_account,insert_update)
              cursors.execute(sql_update_account,updating_the_losing_account)
      
              db.commit()
        
              return "operation performed successfully"

          except mysql.connector.Error as error:        
                 return error
      


# Objentivos para hoy:
# Agregar el metodo de pago movil, (Dni, telefono, banco, monto) #!----> Importante aclarar que debemos cabiar la base de datos para hacer todo
