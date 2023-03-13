
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional


# Shared properties
class HeadquarterBase( BaseModel ):
    name: str = Field( min_length=3, max_length=20 )    
    address: str
    phone: str
    email: str
    organization_id: Optional[ int ] = None  


# Properties to receive via API on creation
class HeadquarterCreate( HeadquarterBase ):
    pass


# Properties to receive via API on update
class HeadquarterUpdate( HeadquarterBase ):
    pass


# Properties shared by models stored in DB
class HeadquarterInDBBase( HeadquarterBase ):
    id : int
    created_at: datetime
    updated_at: datetime

    class config:
        orm_mode = True



# Additional properties to return via API
class Headquarter( HeadquarterInDBBase ):
    pass


# Additional properties stored in DB
class HeadquarterInDB ( HeadquarterInDBBase ):
    pass
