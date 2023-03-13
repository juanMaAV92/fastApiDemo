
from typing import Generator
from sqlalchemy.orm import Session
import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.db.session import SessionLocal

@pytest.fixture(scope="session")
def db() -> Session:
    yield SessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c