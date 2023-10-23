from fastapi import APIRouter, status, Request, Body, Path, Query
from fastapi.encoders import jsonable_encoder
from app.obsolete.models.requests import MovementRequestBody, ArtistRequestBody
from app.es_config import ESConfig, IndexName
from typing import Annotated
import json

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
def add_es_movement(request: Request, movement: MovementRequestBody = Body(...)):
    mvmnt_doc = jsonable_encoder(movement)
    try:
        es_config = ESConfig()
        es_config.connection.index(index="movement", body=mvmnt_doc)
        print("# movement document added")
    except Exception as ex:
        print("# es adding doc: ", ex)


@router.post("/{index_name}", status_code=status.HTTP_201_CREATED)
def add_document(
    index_name: Annotated[
        IndexName, Path(title="The name of the index related to the document")
    ],
    request_body: MovementRequestBody | ArtistRequestBody,
):
    return request_body.model_dump()
