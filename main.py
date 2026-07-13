from fastapi import FastAPI, Path, HTTPException,Query
import json
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import  Annotated,Literal
app = FastAPI()

class Patient(BaseModel):
    id : Annotated[str, Field(..., description="ID of a patient", examples=["P001"])]
    name : Annotated[str, Field(..., description="Name of patient")]
    city : Annotated[str, Field(..., description="city where patient is living")]
    age : Annotated[int, Field(..., gt =0, lt= 120, description="age of patient")]
    gender : Annotated[Literal['male','female','others'], Field(..., description ="gender of patient")]
    height : Annotated[float, Field(..., gt=0, description ="height of patient")]
    weight : Annotated[float, Field(..., gt=0, description="weight of patient")]

    @computed_field
    @property
    def bmi(self)-> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi

    @computed_field
    @property
    def verdict(self)-> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data
def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data, f)

 
@app.get("/")
def hello():
    return {"message":'patient management api'}

@app.get('/about')
def about(): 
    return {'message' : 'fully functional API '}

@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')
def patient_view(patient_id : str = Path(..., description='ID of the patient',examples="P001")):
    #load all data
    v1= load_data()
    if patient_id in v1:
        return v1[patient_id]
    else:
        return HTTPException(status_code=404, detail='Patient not found!')
@app.get('/sort')
def sort_para(sort_by:str=Query(..., description="sort on basis of height, weight, bmi"), order:str = Query('asc', description = 'sort in asc or des order')):
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid field selected  from {valid_fields}")

    orderby = ['asc','desc']
    if order not in orderby:
        raise HTTPException(status_code=400, detail=f"invalid order selected from {orderby}")
    
    sort_order = True if order =='desc' else False
    data = load_data()
    sorted_data = sorted(data.values(), key=lambda x: x.get('sort_by', 0), reverse = sort_order)
    return sorted_data

@app.post('/create')
def create_patient(patient: Patient): #pydantic object 
    
    #load existing data.
    data = load_data()

    #check if the patient already exists?
    if patient.id in data:
        raise HTTPException(status_code=400, detail="patient already exists")
    #new patient added to the database.
    data[patient.id] = patient.model_dump(exclude=['id'])#converting pydantic modelto dic
    #saving file in json:
    save_data(data)
    return JSONResponse(status_code = 201, content={'message':"patient created succesfully"})
