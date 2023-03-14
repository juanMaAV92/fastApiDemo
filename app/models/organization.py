
from typing import TYPE_CHECKING

from sqlalchemy import TIMESTAMP, Column, Integer, PrimaryKeyConstraint, String, UniqueConstraint, text
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .headquarter import Headquarter


class Organization( Base ):
    __tablename__ = 'organizations'

    id =                    Column( Integer, index= True )
    name =                  Column( String, nullable= False )
    description =           Column( String, nullable= False )
    type =                  Column( String, nullable= False )
    identification_type =   Column( String, nullable= False )
    identification =        Column( String, nullable= False )
    address =               Column( String, nullable= False )
    phone =                 Column( String, nullable= False )
    email =                 Column( String, nullable= False )

    created_at = Column( TIMESTAMP( timezone= True),
                                    nullable= False,
                                    server_default= text( "now()" ))
    updated_at = Column( TIMESTAMP( timezone= True),
                                    nullable= False,
                                    server_default= text( "now()" ))

    headquarter = relationship(    'Headquarter',
                                    back_populates= 'organization')

    __table_args__ = (
        PrimaryKeyConstraint( 'id' ),
        UniqueConstraint( 'name' ),
        UniqueConstraint( 'phone' ),
        UniqueConstraint( 'email' ),
    )