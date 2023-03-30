

import os
from alembic.migration import MigrationContext
from alembic.script import ScriptDirectory
from alembic.config import Config
from fastapi import HTTPException

from app.db.session import engine as TypEngine

def is_last( engine: TypEngine ):
    separador = os.path.sep
    dir_actual = os.path.dirname(os.path.abspath(__file__))
    dir = separador.join(dir_actual.split(separador)[:-2])
    
    with engine.connect() as connection:
        context = MigrationContext.configure(connection)
        current_version = context.get_current_revision()

        config = Config()
        config.set_main_option("script_location", dir+'/alembic')
        script_dir = ScriptDirectory.from_config(config)
        heads = script_dir.get_heads()
        latest_version = heads[0]
    
    if current_version != latest_version:
        raise HTTPException(status_code=500, detail="The database is not in the latest version")
    return {"version": current_version}
