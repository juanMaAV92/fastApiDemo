
from datetime import datetime
from pydantic import BaseModel, Field
from uuid import UUID

# Shared properties
class OrganizationBase( BaseModel ):
    description: str = Field( min_length=3, max_length=50 )    
    address: str
    phone: str
    email: str


# Properties to receive via API on creation
class OrganizationCreate( OrganizationBase ):
    name: str = Field( min_length=3, max_length=20 )
    type: str 
    identification_type: str 
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