from config.mySql import db

# from fastapi import Header, Request

# from typing import Annotated

import mysql.connector 

cursors = db.cursor() 
  
def validateUser(user:str):
       # intenta pasar todo por el mismo controlador     
       sql = ("select id, nombre, password from usuario") # select and have condition
         
        # Driver error  
       cursors.execute(sql)

       mys = cursors.fetchall()
       result = list(filter(lambda data_base: data_base[1] == user.name and data_base[2] == user.password, mys)) #------> create the model of person and send
               
       if result:
             for data in result: 
                 return data
       else:
          return None


# Aqui esta pidiendo las cuentas de los cliente, osea para ver su saldo
# Recuperar la redireccion
def sql_get_amount_currents(data:str):
      print(data) 
   #   Tomar el saldo verificar que pueda transferir
   #   Luego pasar los datos verificar que este existan
   #   Pasar el id para evitar la selecion desde aqui  

   #  sql_get_amount_current=("select saldo from cuenta where  usuario_id = %s ") 

   #  insert=(id_user[0])

   #  cursors.execute(sql_get_amount_current, (insert,))

   #  mys=cursors.fetchone() #-------> aqui estamos recibiendo todos lo elementos de la base de datos

   #  print(mys[0])
           

# def verify_the_amount(amount:int):
#     if amount < 0:
#        return True
#     else:
#       return False       


# Luego aqui estamos diciendo que valide dicha transaccion 
def validate_transaction(data_transaction:dict):
     
     sql = ("insert into transaccion" "(tipo_transaccion, fecha_hora , monto , cuenta_id, dispositivo_id)" "values(%s,%s,%s,%s,%s)")
     
     sql_update_account=("update cuenta set saldo = %s where id_cuenta = %s")


     insert = (data_transaction.typeTransaction, data_transaction.date_hour, data_transaction.moto, data_transaction.id_account,data_transaction.id_device ) 

   #   update the amount in the account 
     insert_update = (data_transaction.moto, data_transaction.id_account) #----> aqui que actualize las cuenta pero me falta otra
    
     try:
     
        cursors.execute(sql,insert)
        cursors.execute(sql_update_account,insert_update)
      
        db.commit()
        
        return "operation performed successfully"

     except mysql.connector.Error as error:
          return error
      

# Solucion y sus pasos:
# 1) Hacer una comparacin entre los datos de entrada y salida
# 2) verificar el saldo de la cuenta antes de transferir 
# 3) poner que la hora se ponga sola, sin necesidad de ponerla manual
# 4) usar los datos del cliente
