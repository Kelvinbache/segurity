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
                 
