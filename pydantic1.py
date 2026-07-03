from pydantic import BaseModel, EmailStr, AnyUrl, Field , field_validator   #can attach metadata using fields
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    #type validation
    name: str
    weight: float
    age: int = Field( gt = 0, lt = 60)
    email: EmailStr
    linkedin_url: AnyUrl

    @field_validator('email', mode='after')
    @classmethod
    def email_validator(cls, value):
          valid_domains=['hdfc.com', 'icici.com']
          domain_name= value.split('@')[-1]
          if domain_name not in valid_domains:
                raise ValueError('not a valid domain')
          else:
                return value
          
    @field_validator('name')
    @classmethod
    def name_validator(cls, value):
          return value.upper()
    
    @field_validator('age', mode= 'before')
    @classmethod
    def age_validate(cls, value):
          
          if value>0 and value<60:
                return value
          else:
                raise ValueError('age should be between 0 and 60')
                    

def insert_data(patient: Patient):
        print(patient.name)
        print(patient.age)
        
        print(patient.email)
        print('inserted')


patient_info = {
    'name': ' sana',
    'age': 20,
    'weight': 45,
    'email':'abc@hdfc.com',
    'linkedin_url': 'https://linkedin.com'
    }


patient1 = Patient(**patient_info)  #** since its dictionary so we need to unpack this
insert_data(patient1)