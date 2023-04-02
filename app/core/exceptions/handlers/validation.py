

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError


async def validation_exception_handler(request: Request, exc: RequestValidationError):    
    errors = jsonable_encoder({"detail": exc.errors()})
    return JSONResponse(status_code = 400,
                        content = errors)

