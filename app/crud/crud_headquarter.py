
from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.headquarter import Headquarter
from app.schemas.headquarter import HeadquarterCreate, HeadquarterUpdate


class CRUDHeadquarter(CRUDBase[Headquarter, HeadquarterCreate, HeadquarterUpdate]):
    def if_headquarter(
        self, db: Session, *, obj_in: HeadquarterCreate
    ):
        headquarter = db.query( self.model ).filter(or_( Headquarter.name.like( obj_in.name ),
                                                          Headquarter.phone.like( obj_in.phone ),
                                                          Headquarter.email.like( obj_in.email ))).first() 
        
        return headquarter
    
    
    def get_multi_by_organization(
        self, db: Session, *, organization_id: int, skip: int = 0, limit: int = 100
    ) -> List[Headquarter]:
        return (
            db.query(self.model)
            .filter(Headquarter.organization_id == organization_id)
            .offset(skip)
            .limit(limit)
            .all()
        )



headquarter = CRUDHeadquarter( Headquarter )