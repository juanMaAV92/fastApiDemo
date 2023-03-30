
from uuid import UUID
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import schemas, models, crud
from app.api import deps

router = APIRouter()


@router.get( "", response_model= List[ schemas.Organization ] )
async def read_organizations(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve organizations.
    """
    organizations = crud.organization.get_multi( db, skip=skip, limit=limit )
    return jsonable_encoder( organizations )


@router.post( "", response_model= schemas.Organization )
async def create_organization(
    organization_in: schemas.OrganizationCreate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Create new organization.
    """
    organization = crud.organization.if_organization( db, obj_in=organization_in )
    if ( organization ):
        raise HTTPException(
            status_code=400, detail="organization already exists in the system"
        )
    organization = crud.organization.create(db, obj_in=organization_in)
    return jsonable_encoder( organization )


@router.patch( "/{id}", response_model= schemas.Organization )
async def update_organization(
    id: UUID,
    organization_in: schemas.OrganizationUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update an organization.
    """
    organization = crud.organization.get( db, id= id)
    if not organization:
        raise HTTPException(
            status_code=404,
            detail="Organization not found",
        )
    organization = crud.organization.update( db, db_obj= organization, obj_in= organization_in)
    return jsonable_encoder( organization )


@router.get( "/{id}", response_model= schemas.Organization )
async def read_organization_by_id(
    id: UUID,
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Get a specific organization by id.
    """
    organization = crud.organization.get( db, id=id)
    if not organization:
        raise HTTPException(
            status_code=404, detail="Organization not found"
        )
    return jsonable_encoder( organization )


@router.delete( "/{id}", response_model= schemas.Organization )
async def delete_organization(
    id: UUID,
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Delete a specific organization by id.
    """
    organization = crud.organization.get( db, id=id)
    if not organization:
        raise HTTPException(
            status_code=404, detail="Organization not found"
        )
    organization = crud.organization.remove( db, id=id)
    return jsonable_encoder( organization )