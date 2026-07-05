from pydantic import BaseModel, Field, AnyUrl, EmailStr, computed_field
from typing import Dict, List, Optional 

class Patient(BaseModel):
    name : str 
    age : int
    email : EmailStr
    weight : float #kg
    height : float #meters
    married : Optional[bool] 
    allergies : Optional[List[str]] = False
    contact_details : Dict[str,str]

# In computed field we don't take that info from user we compute it like: Bmi computed with height and weight
    @computed_field
    @property
    def bmi( self) -> float:
        bmi = round(self.weight / (self.height)**2, 2)
        return bmi

def show_data(patient : Patient):
    print(patient.name)
    print('BMI:', patient.bmi)
    print(patient.age)


patient_info ={
    'name' : 'Jane',
    'age': 34,
    'weight': 58,
    'height' : 1.72,
    'email':'abcd@gmail.com',
    'married' : False,
    'contact_details' : {'Phone':'98765432'}
}
patient3 = Patient(** patient_info)
show_data(patient3)

