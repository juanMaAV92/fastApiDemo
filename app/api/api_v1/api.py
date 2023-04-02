

from fastapi import APIRouter


from app.api.api_v1.endpoints import organizations, headquarters, seed

api_router = APIRouter()

api_router.include_router( organizations.router, prefix= "/organizations", tags=[ "organizations" ])
api_router.include_router( headquarters.router, prefix= "/headquarters", tags=[ "headquarters" ])
api_router.include_router( seed.router, prefix= "/seed", tags=[ "seed" ])