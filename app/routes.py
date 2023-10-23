from fastapi import APIRouter, status, Request, Body, Path, Query
from fastapi.encoders import jsonable_encoder
from app.movement import MovementModel
from app.es_config import ESConfig, IndexName
from typing import Annotated, Optional

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
def get_all_movements(q: Annotated[Optional[str], Query(title="Search input")] = None):
    """
    A basic search query.
    """
    es_config = ESConfig()

    try:
        movements = es_config.connection.search(index=IndexName.MOVEMENT, q=q)
        print("Search results:\n", movements)
    except Exception as ex:
        print("Search error: ", ex)


@router.post("/", status_code=status.HTTP_201_CREATED)
def add_movement(movement: MovementModel = Body(...)):
    """
    Adding a movement document to ES.
    """
    mvmnt_doc = jsonable_encoder(movement)
    try:
        es_config = ESConfig()
        es_config.connection.index(index=IndexName.MOVEMENT, body=mvmnt_doc)
        return movement.model_dump()
    except Exception as ex:
        print("Error adding movement: ", ex)
