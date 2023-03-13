

from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas, models, crud
from app.api import deps

router = APIRouter()


@router.get( "", response_model= List[ schemas.Headquarter ] )
def read_headquarters(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve headquarters.
    """
    headquarters = crud.headquarter.get_multi( db, skip=skip, limit=limit )
    return headquarters


@router.post( "", response_model= schemas.Headquarter )
def create_headquarter(
    *,
    db: Session = Depends(deps.get_db),
    headquarter_in: schemas.HeadquarterCreate,
) -> Any:
    """
    Create new headquarter.
    """
    # TODO: check if the headquarter already exists

    headquarter = crud.headquarter.create(db, obj_in=headquarter_in)
    return headquarter


@router.patch( "/{id}", response_model= schemas.Headquarter )
def update_headquarter(

) -> Any:
    # TODO: 
    return []


@router.get( "/{id}", response_model= schemas.Headquarter)
def get_headquarter_by_id(
    id: int,
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Get a specific headquarter by id.
    """
    headquarter = crud.headquarter.get( db, id=id)
    if not headquarter:
        raise HTTPException(
            status_code=404, detail="Headquarter not found"
        )
    return headquarter


@router.delete( "/{id}", response_model= schemas.Headquarter)
def delete_headquarter(
    id: int,
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Delete a specific headquarter by id.
    """
    headquarter = crud.headquarter.get( db, id=id)
    if not headquarter:
        raise HTTPException(
            status_code=404, detail="Headquarter not found"
        )
    headquarter = crud.headquarter.remove( db, id=id)
    return headquarter