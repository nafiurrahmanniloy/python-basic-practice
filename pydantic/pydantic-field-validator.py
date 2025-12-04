from pydantic import BaseModel,EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

# ------ field_validator is used to validate data on a single field ---
# ------ field_validator works on 2 mode(before and after):: by default it is set to **after** ----
# ------ field_validator is used to do **custom data validation** or any kind of transformation ---
# ------ to user field_validator need to create a method inside the class::**classmethod**---


class Patient(BaseModel):  #first step is to create a pydentic model(class)
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool 
    allergies: Optional[List[str]] = None #makes this feild optiona :: Must set default value to None(step 1)
    contact_details: Dict[ str, str]
  
  #custom data validation using field_validator
    
    @field_validator('email')   # field to apply the validation
    @classmethod
    def email_validator(cls,value):     # gets 2 inputs one is class and the other is the value: email
        valid_domains =['student.aiub.edu','ific.com']
        
        domain_name =value.split('@')[-1]  # splits the data on @ and get the last string.

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain.')
        return value
    
 #transformation using field_validator
    @field_validator('name')
    @classmethod
    
    def name_upper_transform(cls, value):
        return value.upper()
   
   
    @field_validator('age', mode ='after')
    @classmethod
    
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be between 0 to 100')
            
    
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

patient_info = {'name': 'Niloy', 'email':'nafiur@student.aiub.edu','age': '30' , 'weight': 65.6, 'married':False, 'allergies': ['dust','pollen'],
                'contact_details': {'phone': '01722222222'}}  #dictionary 
    
    
patient1 =Patient(**patient_info)  # ** used to unpack dictionary:: This is a pydantic object(step 2)--> validation==> type coercion

insert_patient_info(patient1) #step 3
