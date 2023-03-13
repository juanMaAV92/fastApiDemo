

from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas, models, crud
from app.api import deps

router = APIRouter()


@router.get( "", response_model= List[ schemas.Organization ] )
def read_organizations(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve organizations.
    """
    organizations = crud.organization.get_multi( db, skip=skip, limit=limit )
    return organizations


@router.post( "", response_model= schemas.Organization )
def create_organization(
    *,
    db: Session = Depends(deps.get_db),
    organization_in: schemas.OrganizationCreate,
) -> Any:
    """
    Create new organization.
    """
    # TODO: check if the organization already exists

    organization = crud.organization.create(db, obj_in=organization_in)
    return organization


@router.patch( "/{id}", response_model= schemas.Organization )
def update_organization(

) -> Any:
    # TODO: 
    return []


@router.get( "/{id}", response_model= schemas.Organization )
def get_organization_by_id(
    id: int,
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
    return organization


@router.delete( "/{id}", response_model= schemas.Organization )
def delete_organization(
    id: int,
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
    return organization