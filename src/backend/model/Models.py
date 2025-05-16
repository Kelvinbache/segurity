from pydantic import BaseModel

class Person(BaseModel):
    id:int
    name:str
    lastName:str
    phone:str
