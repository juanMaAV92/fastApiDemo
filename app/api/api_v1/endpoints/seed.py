

import os
from typing import Any

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app import schemas
from app.db.base_class import Base
from app.db.session import engine


router = APIRouter()


seed_data = {    
    'organization' : [
        {
            'id' : "740ed1fd-3ec1-4135-99d0-1bf9ab947c99",
            "name": "0rganization 1",
            "email": "organization1@email.com",
            "type": "comida rapida",
            "identification_type": "CC",
            "identification": "1111111111",
            "description": "comidas rapidas la numero 1",
            "address": "calle 1 carrera 1",
            "phone": "11111111",
        },{
            'id' : "68fd024d-3e42-42d6-a8d0-431b21cd4a95",
            "name": "0rganization 2",
            "email": "organization2@email.com",
            "type": "comida rapida",
            "identification_type": "NIT",
            "identification": "2222222222",
            "description": "comidas rapidas la numero 2",
            "address": "calle 2 carrera 2",
            "phone": "22222222",
        },{
            'id' : "dc2451d6-4678-492d-bca8-9381e71ee4a0",
            "name": "0rganization 3",
            "email": "organization3@email.com",
            "type": "comida rapida",
            "identification_type": "CC",
            "identification": "3333333333",
            "description": "comidas rapidas la numero 3",
            "address": "calle 3 carrera 3",
            "phone": "33333333",
        },{
            'id' : "006575da-a247-43db-ad44-652e5d2cfefa",
            "name": "0rganization 4",
            "email": "organization4@email.com",
            "type": "comida rapida",
            "identification_type": "CC",
            "identification": "4444444444",
            "description": "comidas rapidas la numero 4",
            "address": "calle 4 carrera 4",
            "phone": "44444444",
        }
    ],
    'headquarter' : [
        {   
            'id' : '2469d6cb-7800-4d36-a6e8-898395beef76',
            "name": "headquarter 1",
            "address": "avenida 1 transversarl 1",
            "phone": "11111111111",
            "email": "headquarter1@email.com",
            "organization_id": '68fd024d-3e42-42d6-a8d0-431b21cd4a95'
        },{
            'id' : '3b1a5dc8-b775-496a-8c75-544c6dc2e404',
            "name": "headquarter 2",
            "address": "avenida 2 transversarl 2",
            "phone": "22222222222",
            "email": "headquarter2@email.com",
            "organization_id": None
        },{
            'id' : '6d2d9750-b5d3-45ce-8dd8-b139d22508ab',
            "name": "headquarter 3",
            "address": "avenida 3 transversarl 3",
            "phone": "33333333333",
            "email": "headquarter3@email.com",
            "organization_id": '68fd024d-3e42-42d6-a8d0-431b21cd4a95'
        },{
            'id' : 'af80a63b-001e-4877-bee8-a3a9ef89872b',
            "name": "headquarter 4",
            "address": "avenida 4 transversarl 4",
            "phone": "44444444444",
            "email": "headquarter4@email.com",
            "organization_id": None
        },{
            'id' : 'bdecf3e2-ab05-44e7-8b3d-c48d0288cf5d',
            "name": "headquarter 5",
            "address": "avenida 5 transversarl 5",
            "phone": "55555555555",
            "email": "headquarter5@email.com",
            "organization_id": 'dc2451d6-4678-492d-bca8-9381e71ee4a0'
        },{
            'id' : '9e6822e4-00b1-4dcf-ab9a-22051da85563',
            "name": "headquarter 6",
            "address": "avenida 6 transversarl 6",
            "phone": "66666666666",
            "email": "headquarter6@email.com",
            "organization_id": None
        }
    ]
}


@router.get('')
async def populate_DB(
    db: Session = Depends(deps.get_db)
) -> Any:
    env = os.getenv("ENV")
    if env != 'development':
        return JSONResponse( status_code= 403, content= 'endpoint available just in development mode' )
    
    Base.metadata.drop_all( bind= engine )
    Base.metadata.create_all( bind= engine )

    for model, rows in seed_data.items():
        match model:
            case 'organization':
                for row in rows:
                    organization = schemas.OrganizationSeed.parse_obj( row )
                    organization = crud.organization.create(db, obj_in=  organization)
            case 'headquarter':
                for row in rows:
                    headquarter = schemas.HeadquarterSeed.parse_obj( row )
                    headquarter = crud.headquarter.create(db, obj_in=  headquarter)

    return {"message": "Seed created"}
