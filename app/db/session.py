

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import Settings


engine = create_engine( Settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping= True )
SessionLocal = sessionmaker( autocommit= False, autoflush= False, bind= engine )