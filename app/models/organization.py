
from typing import TYPE_CHECKING
import uuid

from sqlalchemy import TIMESTAMP, Column, Integer, PrimaryKeyConstraint, String, UniqueConstraint, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Enum as sqlEnum

from app.db.base_class import Base
from app.schemas.organization import IdentificationType

if TYPE_CHECKING:
    from .headquarter import Headquarter


class Organization( Base ):
    __tablename__ = 'organizations'

    id =                    Column( UUID( as_uuid= True ), default= uuid.uuid4 )
    name =                  Column( String, nullable= False )
    description =           Column( String, nullable= False )
    type =                  Column( String, nullable= False )
    identification_type =   Column( sqlEnum(IdentificationType), nullable= False )
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
        UniqueConstraint('identification_type', 'identification', name='uniq_Identification' ),
        UniqueConstraint( 'name' ),
        UniqueConstraint( 'phone' ),
        UniqueConstraint( 'email' ),
    )