from pydantic import BaseModel,EmailStr,model_validator
from typing import List, Dict, Optional


# ---- Model validatior is to validate multiple fields combine(dependent fileds) ----
# ---- if users age is more then 60 then there must be an emergency contact number ----


class Patient(BaseModel):  #first step is to create a pydentic model(class)
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool 
    allergies: Optional[List[str]] = None #makes this feild optiona :: Must set default value to None(step 1)
    contact_details: Dict[ str, str]

    @model_validator(mode='after')
    
    def validate_em_contact(self):
        if self.age > 60 and 'emergency' not in self.contact_details:
            raise ValueError('Patient older then 60 must have an emergency contact')
        return self



def insert_patient_info(patient:Patient):
    print(patient.name)
    print(patient.email)
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

patient_info = {'name': 'Niloy','email':'nafiur@student.aiub.edu', 'age': 61, 'weight': 65.6, 'married':False, 'allergies': ['dust','pollen'],
                'contact_details': {'phone': '01722222222', 'emergency':'0172342348371'}} #dictionary 
    
    
patient1 =Patient(**patient_info)  # ** used to unpack dictionary:: This is a pydantic object(step 2)

insert_patient_info(patient1) #step 3
