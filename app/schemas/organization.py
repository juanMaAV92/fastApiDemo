
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional


# Shared properties
class OrganizationBase( BaseModel ):
    description: str = Field( min_length=3, max_length=50 )    
    address: str
    phone: str
    email: str


# Properties to receive on item creation
class OrganizationCreate( OrganizationBase ):
    name: str = Field( min_length=3, max_length=20 )
    type: str 
    identification_type: str 
    identification: str


# Properties to receive on item update
class OrganizationUpdate( OrganizationBase ):
    pass


# Properties shared by models stored in DB
class OrganizationInDBBase( OrganizationBase ):
    id : int
    created_at: datetime
    updated_at: datetime

    class config:
        orm_mode = True



# Properties to return to client
class Organization( OrganizationInDBBase ):
    pass


# Properties stored in DB
class OrganizationInDB ( OrganizationInDBBase ):
    pass
