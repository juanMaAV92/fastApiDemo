
import os
from functools import lru_cache

from typing import Any, Dict, Optional
from pydantic import BaseSettings, EmailStr, PostgresDsn, validator


class Settings( BaseSettings ):

    API_V_STR :  str
    API_RELOAD : bool

    SERVER_NAME : str
    SERVER_HOST : str
    SERVER_PORT : int

    PROJECT_NAME : str
    PROJECT_DESCRIPTION : str
    PROJECT_VERSION : str
    PROJECT_DOCS_URL : str
    PROJECT_REDOC_URL : str

    POSTGRES_USER : str
    POSTGRES_PASSWORD : str
    POSTGRES_HOST : str
    POSTGRES_PORT : int
    POSTGRES_DB : str
    SQLALCHEMY_DATABASE_URI : Optional[ PostgresDsn ]

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[ str ], values: Dict[ str, Any] ) -> Any:
        if isinstance( v, str ):
            return v

        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER" ),
            password=values.get( "POSTGRES_PASSWORD" ),
            host=values.get( "POSTGRES_HOST" ),
            port=str(values.get( 'POSTGRES_PORT' )),
            path=f"/{values.get( 'POSTGRES_DB' ) or '' }",
        )
    
    FIRST_SUPERUSER : EmailStr
    FIRST_SUPERUSER_PASSWORD : str
    USERS_OPEN_REGISTRATION : bool = False

    class Config :
        separador = os.path.sep
        dir_actual = os.path.dirname(os.path.abspath(__file__))
        dir = separador.join(dir_actual.split(separador)[:-2])
        env_file = dir + '/.env'
        env_file_encoding = 'utf-8'
        case_sensitive = True

@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()