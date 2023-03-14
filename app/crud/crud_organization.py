

from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.organization import Organization
from app.schemas.organization import OrganizationCreate, OrganizationUpdate


class CRUDOrganization(CRUDBase[Organization, OrganizationCreate, OrganizationUpdate]):
    def if_organization(
        self, db: Session, *, obj_in: OrganizationCreate
    ):
        # TODO: create and check key ( identification_type, identification )

        organization = db.query( self.model ).filter(or_( Organization.name.like( obj_in.name ),
                                                          Organization.phone.like( obj_in.phone ),
                                                          Organization.email.like( obj_in.email ))).first() 
        
        return organization

organization = CRUDOrganization( Organization ) 