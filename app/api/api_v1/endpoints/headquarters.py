

from typing import Any

from fastapi import APIRouter


router = APIRouter()


@router.get( "" )
def read_headquarters(

) -> Any:
    return []


@router.post( "" )
def create_headquarter(

) -> Any:
    return []


@router.patch( "/{id}" )
def update_headquarter(

) -> Any:
    return []


@router.get( "/{id}" )
def get_headquarter(

) -> Any:
    return []


@router.delete( "/{id}" )
def delete_headquarter(

) -> Any:
    return []