from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):  #first step is to create a pydentic model(class)
    name: str
    age: int
    weight: float
    married: bool 
    allergies: Optional[List[str]] = None #makes this feild optiona :: Must set default value to None
    contact_details: Dict[ str, str]

def insert_patient_info(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('data inserted')
def update_patient_info(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('data Updated')

patient_info = {'name': 'Niloy', 'age': 30, 'weight': 65.6, 'married':False, 'allergies': ['dust','pollen'],
                'contact_details': {'email': 'nafiur@gmail.com', 'phone': '01722222222'}}  #dictionary 
    
    
patient1 =Patient(**patient_info)  # ** used to unpack dictionary:: This is a pydantic object

insert_patient_info(patient1)
