

from fastapi import APIRouter


from api.api_v1.endpoints import organizations, headquarters


api_router = APIRouter()

api_router.include_router( organizations.router, prefix= "/organizations", tags=[ "organizations" ])
api_router.include_router( headquarters.router, prefix= "/headquarters", tags=[ "headquarters" ])