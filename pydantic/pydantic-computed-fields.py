from pydantic import BaseModel,EmailStr, computed_field
from typing import List, Dict, Optional


# ----- computed field is a field of pydantic model which value wont be provided by the user
# ----- for example: get weight and height value form user then calculate bmi of the user dynamically
# ----- will be created dynamically and dependent on the other fields of the pydantic model---> then use computed_field


class Patient(BaseModel):  #first step is to create a pydentic model(class)
    name: str
    email: EmailStr
    age: int
    weight: float #kg
    height: float #mtr
    married: bool 
    allergies: Optional[List[str]] = None #makes this feild optiona :: Must set default value to None(step 1)
    contact_details: Dict[ str, str]

    @computed_field # @...---> are called decorator 
    @property
    def calculate_bmi(self) -> float:  #this fun name becomes field name
        bmi= round(self.weight/(self.height**2),2)
        return bmi



def insert_patient_info(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.weight)
    print(f'BMI is: {patient.calculate_bmi}')
    print(patient.allergies)
    print(patient.contact_details)
    print('data inserted')
def update_patient_info(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('data Updated')

patient_info = {'name': 'Niloy','email':'nafiur@student.aiub.edu', 'age': 30, 'weight': 65.6,'height':1.4, 'married':False, 'allergies': ['dust','pollen'],
                'contact_details': {'phone': '01722222222'}}  #dictionary 
    
    
patient1 =Patient(**patient_info)  # ** used to unpack dictionary:: This is a pydantic object(step 2)

insert_patient_info(patient1) #step 3
