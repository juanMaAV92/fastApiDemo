

import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from core.config import settings

print(str(settings.SQLALCHEMY_DATABASE_URI))
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


def run():
    uvicorn.run(    'main:app',
                    host = settings.SERVER_HOST,
                    port = settings.SERVER_PORT,
                    reload = settings.API_RELOAD,
                    log_level = 'debug')


if __name__ == '__main__':
    run()