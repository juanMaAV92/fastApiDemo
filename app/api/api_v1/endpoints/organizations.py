

from typing import Any

from fastapi import APIRouter


router = APIRouter()


@router.get( "" )
def read_organizations(

) -> Any:
    return []


@router.post( "" )
def create_organization(

) -> Any:
    return []


@router.patch( "/{id}" )
def update_organization(

) -> Any:
    return []


@router.get( "/{id}" )
def get_organization(

) -> Any:
    return []


@router.delete( "/{id}" )
def delete_organization(

) -> Any:
    return []