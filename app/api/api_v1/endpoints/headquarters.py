
from uuid import UUID
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import schemas, models, crud
from app.api import deps

router = APIRouter()


@router.get( "", response_model= List[ schemas.Headquarter ] )
async def read_headquarters(
    skip: int = 0,
    limit: int = 100,
    organization_id: int = None,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve headquarters.
    """
    if organization_id:
        headquarters = crud.headquarter.get_multi_by_organization( db, organization_id=organization_id, skip=skip, limit=limit  )
    else:
        headquarters = crud.headquarter.get_multi( db, skip=skip, limit=limit )
    return jsonable_encoder( headquarters )


@router.post( "", response_model= schemas.Headquarter )
async def create_headquarter(
    headquarter_in: schemas.HeadquarterCreate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Create new headquarter.
    """
    headquarter = crud.headquarter.if_headquarter( db, obj_in=headquarter_in )
    if ( headquarter ):
        raise HTTPException(
            status_code=400, detail="headquarter already exists in the system"
        )
    headquarter = crud.headquarter.create(db, obj_in=headquarter_in)
    return jsonable_encoder( headquarter )


@router.patch( "/{id}", response_model= schemas.Headquarter )
async def update_headquarter(
    id: UUID,
    headquarter_in: schemas.HeadquarterUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update an headquarter.
    """
    headquarter = crud.headquarter.get( db, id= id)
    if not headquarter:
        raise HTTPException(
            status_code=404,
            detail="Headquarter not found",
        )
    # TODO: raise Exception if organization_id is not valid

    headquarter = crud.headquarter.update( db, db_obj= headquarter, obj_in= headquarter_in)
    return jsonable_encoder( headquarter )


@router.get( "/{id}", response_model= schemas.Headquarter)
async def get_headquarter_by_id(
    id: UUID,
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
    return jsonable_encoder( headquarter )



@router.delete( "/{id}", response_model= schemas.Headquarter)
async def delete_headquarter(
    id: UUID,
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
    return jsonable_encoder( headquarter )