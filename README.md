# Fast Api Demo

This is an exercise to learn how use FastApi

Run in local

```sh
cd ~/fastApiDemo
bash script/setup_env.sh development
# in deploy change development => production

source .venv/bin/activate
poetry run python app/main.py
```


# Alembic

New revision

```sh
cd ~/fastApiDemo
while read line; do export $line; done < .env
printenv PROJECT_VERSION  
alembic upgrade head
alembic revision --autogenerate -m "some useful message
```

API documentation http://localhost:5000/docs also http://localhost:5000/redoc


# Some interesing links

- [Home page FastApi](https://fastapi.tiangolo.com/)
- [Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/)
- [JSON Schema](https://json-schema.org/)
- [Tipos](https://fastapi.tiangolo.com/python-types/)
- [SQLAlchemy Schema](https://overiq.com/sqlalchemy-101/defining-schema-in-sqlalchemy-core/)