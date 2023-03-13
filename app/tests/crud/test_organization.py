

from sqlalchemy.orm import Session

from app import crud
from app.db.session import SessionLocal
from app.tests.utils.organization import create_random_organization

def test_create_organization( ) -> None:
    db = SessionLocal()
    organization_in = create_random_organization()
    organization = crud.organization.create( db, obj_in= organization_in )
    assert organization.email == organization_in.email
    assert organization.identification_type == organization_in.identification_type