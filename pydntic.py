from pydantic import BaseModel, EmailStr, AnyUrl, Field    #can attach metadata using fields
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    #type validation
    name: Annotated[str, Field(max_length = 50, title = ' Name of patient', description = 'Give the name of the patient in less than 50 chars', examples= ['sana','Saniya gusain'])]
    age: int = Field( gt = 0, lt = 60)
    email: EmailStr
    
    # linkedin = Annotated[Optional[AnyUrl], Field(default = None) ]
    married: Annotated[bool, Field(default = None, description='patient married or not', examples=['True','False'])]
    allergies: Annotated[Optional[List[str]], Field(default = None)]   #why not only list:we need to validate each item should be string, thats whyyy
    contact_details: Dict[str,str]


def insert_data(patient: Patient):
        print(patient.name)
        print(patient.age)
        print(patient.allergies)
        print(patient.email)
        print('inserted')


patient_info = {
    'name': ' sana',
    'age': 20,
    'weight': 45,
    'married':False,
    'email':'abc@gmail.com',
    'contact_details':{'phone':'9767852445'}
}

patient1 = Patient(**patient_info)  #** since its dictionary so we need to unpack this
insert_data(patient1)