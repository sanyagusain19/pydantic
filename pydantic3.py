from pydantic import BaseModel, Field, AnyUrl, EmailStr, model_validator
from typing import Dict, List, Optional

class Patient(BaseModel):
    name : str 
    age : int
    email : EmailStr
    weight : float
    married : Optional[bool] 
    allergies : Optional[List[str]] = False
    contact_details : Dict[str,str]

    @model_validator(mode = 'after')
    def vaidate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError(' For age greater than 60, there must be an emergency number provided')  
        return model




def insert_data(patient: Patient):
        print(patient.name)
        print(patient.age)
        print(patient.contact_details)
        print(patient.email)
        print('inserted')


patient_info = {
    'name': ' Stefie',
    'age': 30,
    'weight': 45,
    'married' : True,
    'email':'abc@hdfc.com',
    'contact_details': {'phone no.': '67896543'}}


patient1 = Patient(**patient_info)  #** since its dictionary so we need to unpack this
insert_data(patient1)