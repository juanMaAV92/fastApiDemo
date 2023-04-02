
import re
from datetime import datetime
from pydantic import BaseModel, Field, validator
from typing import Optional
from uuid import UUID

# Shared properties
class HeadquarterBase( BaseModel ):
    name: str = Field( min_length=3, max_length=20 )    
    address: str
    phone: str
    email: str
    organization_id: Optional[ UUID ] = None  

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
class HeadquarterCreate( HeadquarterBase ):
    pass


# Properties to receive via API on update
class HeadquarterUpdate( HeadquarterBase ):
    pass


# Properties shared by models stored in DB
class HeadquarterInDBBase( HeadquarterBase ):
    id : UUID
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


# seed population properties 
class HeadquarterSeed( HeadquarterCreate ):
    id : UUID
    pass