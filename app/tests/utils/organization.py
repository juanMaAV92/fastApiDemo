
from sqlalchemy.orm import Session

from app.models.organization import Organization
from app.schemas.organization import OrganizationCreate
from app import crud
from app.tests.utils.utils import random_email, random_identification_type, random_lower_string, random_phone

def create_random_organization() -> Organization:
    name = random_lower_string( 8 )
    type = random_lower_string( 4 )
    identification_type = random_identification_type()
    identification = random_lower_string( 10 )
    description = random_lower_string()
    address = random_lower_string( 15 )
    phone = random_phone()
    email = random_email()
    organization_in = OrganizationCreate(
        name = name,
        type = type,
        identification_type = identification_type,
        identification = identification,
        description = description,
        address = address,
        phone = phone,
        email = email
    )    
    return organization_in