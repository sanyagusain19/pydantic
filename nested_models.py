from pydantic import BaseModel, AnyUrl, EmailStr
from typing import Dict, List

class Address(BaseModel):
    city : str
    state : str
    pin : str


class Patient(BaseModel):
    name : str
    age : int
    gender : str
    address :  Address        #complexx data

address_dict ={
    "city": "YNR",
    'state': 'Haryana',
    'pin' : '135001'

}
address1 = Address(**address_dict)
patient_info ={
    'name':'sana',
    'age': 30,
    'gender':'female',
    'address' : address1
}
patient1 = Patient(**patient_info)
print(patient1.name)
print(patient1.address.state)