
from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.headquarter import Headquarter
from app.schemas.headquarter import HeadquarterCreate, HeadquarterUpdate


class CRUDHeadquarter(CRUDBase[Headquarter, HeadquarterCreate, HeadquarterUpdate]):
    def create_with_organization(
        self, db: Session, *, obj_in: HeadquarterCreate, organization_id: int
    ) -> Headquarter:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, organization_id=organization_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

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