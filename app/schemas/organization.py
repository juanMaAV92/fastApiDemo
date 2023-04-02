
import re
from datetime import datetime
from uuid import UUID
from enum import Enum
from pydantic import BaseModel, Field, validator


class IdentificationType(str, Enum):
    CC = 'CC'
    NIT = 'NIT'
    

# Shared properties
class OrganizationBase( BaseModel ):
    description: str = Field( min_length=3, max_length=50 )    
    address: str
    phone: str
    email: str

    @validator('phone')
    def validate_phone( cls, v ):
        if not bool(re.match(r"^\+[0-9]{10,10}$", v)):
            raise ValueError("invalid phone number format")
        return v

    @validator('email')
    def validate_email( cls, v ):
        if not bool(re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", v)):
            raise ValueError("invalid email format")
        return v
    


# Properties to receive via API on creation
class OrganizationCreate( OrganizationBase ):
    name: str = Field( min_length=3, max_length=20 )
    type: str 
    identification_type: IdentificationType 
    identification: str

   
# Properties to receive via API on update
class OrganizationUpdate( OrganizationBase ):
    pass


# Properties shared by models stored in DB
class OrganizationInDBBase( OrganizationBase ):
    id : UUID
    created_at: datetime
    updated_at: datetime

    class config:
        orm_mode = True



# Additional properties to return via API
class Organization( OrganizationInDBBase ):
    name: str = Field( min_length=3, max_length=20 )
    type: str 
    identification_type: str 
    identification: str
    pass


# Additional properties stored in DB
class OrganizationInDB ( OrganizationInDBBase ):
    pass




# seed population properties 
class OrganizationSeed( OrganizationCreate ):
    id : UUID
    pass