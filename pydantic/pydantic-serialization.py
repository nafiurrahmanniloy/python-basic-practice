# export pydantic models as python dict or json

from pydantic import BaseModel

class address(BaseModel):
    road:str
    city: str
    postalcode: str

class patient(BaseModel):
    name: str
    gender: str
    age: int 
    address: address      
    
    
address_dict = {'road': 'Badda','city':'Dhaka', 'postalcode': '2200'}  

# pydantic obj
address1 = address(**address_dict)

patient_dict ={
    'name': 'Niloy',
    'gender': 'Male',
    'age': 22,
    'address': address1
}

patient1 = patient(**patient_dict)


# output in dict 
temp = patient1.model_dump()
print(temp)
print(type(temp))

#output in json 
temp2= patient1.model_dump_json()
print(temp2)
print(type(temp2))

temp3 = patient1.model_dump(include=['name', 'gender']) #only get specific one or two fields
print(temp3)
print(type(temp3))

temp4 = patient1.model_dump(exclude=['name', 'gender']) #only exclude specific one or two fields
print(temp4)
print(type(temp4))

temp5 = patient1.model_dump(exclude={'address': ['state']}) 
print(temp5)
print(type(temp5))