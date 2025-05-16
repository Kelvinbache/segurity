from pydantic import BaseModel

class Person(BaseModel):
    name:str
    lastName:str
    email:str
    phone:str
