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

temp = patient1.model_dump   #convert existsing model into dictionary
print(temp)
print(type(temp))
#if need json
temp1 = patient1.model_dump_json
print(temp1)
#if need only address field or name field then
temp2 = patient1.model_dump(include=['name','address'])
#exclude too:
# temp3= patient1.model_dump(exclude=['gender'])
temp3= patient1.model_dump(exclude={'address':['pin']})
print(temp3)
#one more parameter is necessary 'exclude_unset=True': which means it will exclude the default one whose value is not provided.