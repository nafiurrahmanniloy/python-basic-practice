from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

# --- Field is a special type to validate data (custom data validation) :: works as constraint ----
# --- Field function is also used to attatch {metadata} as well.--->to attatch metadata have to use combination of: [Field and Annotated] ------
# --- Field function is also used to set default values ----


class Patient(BaseModel):  #first step is to create a pydentic model(class)
    name: Annotated[str ,Field(max_length=50, title='name of the patient', description='Patient name cant be more then 50 chars.', examples=['Niloy','Nafiur'])]
    email: EmailStr #email validation ---> using custom data type
    linkedin: AnyUrl #url or link validation
    age: int = Field(gt=0, lt= 100)
    weight: Annotated[float , Field(gt=0, strict=True)]  # strict--> does not allow pydantic to convert string to int automatically.
    married: Annotated[bool,Field(default=None, description='Is the patient is married or not')]
    allergies: Annotated[Optional[List[str]], Field(max_length=5, default=None)] #makes this feild optiona :: Must set default value to None(step 1)
    contact_details: Dict[ str, str]

def insert_patient_info(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(f'user linkedIn url is: {patient.linkedin}')
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

patient_info = {'name': 'Niloy','email':'nafiur@gmail.com','linkedin': 'https://www.linkedin.com/in/nafiur-rahman-niloy/','age': 30, 'weight': 65.6, 'married':False, 'allergies': ['dust','pollen'],
                'contact_details': { 'phone': '01722222222'}}  #dictionary 
    
    
patient1 =Patient(**patient_info)  # ** used to unpack dictionary:: This is a pydantic object(step 2)

insert_patient_info(patient1) #step 3
