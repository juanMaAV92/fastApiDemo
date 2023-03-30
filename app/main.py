# -----------------------------------------------------------
# demonstrates how to use FastApi
#
# (C) 2023 juanMaAV92, Cali, Colombia
# Released under GNU Public License (GPL)
# email juanmanuel.armero@gmail.com
# -----------------------------------------------------------

import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.api.api_v1.api import api_router
from app.core.config import settings
from app.db.session import engine
from app.db.base_class import Base
import app.db.revision as revision


Base.metadata.create_all( bind= engine )
revision.is_last( engine )

app = FastAPI(
    title = settings.PROJECT_NAME, 
    description = settings.PROJECT_DESCRIPTION,
    version = settings.PROJECT_VERSION,
    
    docs_url = settings.PROJECT_DOCS_URL,
    redoc_url = settings.PROJECT_REDOC_URL,    
    openapi_url = f"{settings.API_V_STR}/openapi.json"
)


@app.get( f'/health', tags=[ 'health' ] )
async def health():
    return JSONResponse(    status_code = 200,
                            content = [] )


app.include_router( api_router, prefix= settings.API_V_STR )



def run():
    uvicorn.run(    'main:app',
                    host = settings.SERVER_HOST,
                    port = settings.SERVER_PORT,
                    reload = settings.API_RELOAD,
                    log_level = 'debug')


if __name__ == '__main__':
    run()