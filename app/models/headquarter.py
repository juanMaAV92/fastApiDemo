
from typing import TYPE_CHECKING

from sqlalchemy import TIMESTAMP, Column, ForeignKeyConstraint, Integer, PrimaryKeyConstraint, String, UniqueConstraint, text
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .organization import Organization
    

class Headquarter( Base ):
    __tablename__ = 'headquarters'

    id =        Column( Integer, index= True  )
    name =      Column( String, nullable= False)
    address =   Column( String, nullable= False)
    phone =     Column( String, nullable= False)
    email =     Column( String, nullable= False)
    
    organization_id = Column( Integer, nullable=True, default= None ) 

    created_at = Column(TIMESTAMP(  timezone=True),
                                    nullable=False, 
                                    server_default=text("now()"))
    updated_at = Column(TIMESTAMP(  timezone=True),
                                    nullable=False, 
                                    server_default=text("now()"))

    organization = relationship(    "Organization", 
                                    back_populates="headquarter" )
   
    __table_args__ = ( 
        PrimaryKeyConstraint( 'id' ),
        ForeignKeyConstraint( [ 'organization_id' ],[ 'organizations.id' ]),
        UniqueConstraint( 'name' ),
        UniqueConstraint( 'phone' ),
        UniqueConstraint( 'email' ),
    )