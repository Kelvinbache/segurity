from config.mySql import db

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

def validate_transaction(data_transaction:dict):
    
     sql = ("insert into transaccion" "(tipo_transaccion, fecha_hora , monto , cuenta_id, dispositivo_id)" "values(%s,%s,%s,%s,%s)")
     
     sql_update_account=("update cuenta set saldo = %s where id_cuenta = %s")
     
     insert = (data_transaction.typeTransaction, data_transaction.date_hour, data_transaction.moto, data_transaction.id_account,data_transaction.id_device ) 
     
     insert_update = (data_transaction.moto, data_transaction.id_account) 


     try:
       
        cursors.execute(sql,insert)
        cursors.execute(sql_update_account,insert_update)

        db.commit()  # error here
        
        return "operation performed successfully"

     except db.Error as e:
          return db.rollback()         
      
