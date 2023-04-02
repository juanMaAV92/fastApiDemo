
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


class ExceptionsMiddleware( BaseHTTPMiddleware ):
    def __init__( self, app: FastAPI ) -> None:
        super().__init__( app )

    async def dispatch( self, request: Request, call_next ) -> Response or JSONResponse:
        try:
            return await call_next( request )
        except Exception as exc:
            body = await request.body()
            detail = {"errors": exc.errors(), "body": body.decode()}
            return JSONResponse( status_code= 500, content={ 'error': str(exc) } )