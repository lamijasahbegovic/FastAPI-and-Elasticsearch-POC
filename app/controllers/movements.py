from fastapi import APIRouter, status, Request, Body, Path, Query
from fastapi.encoders import jsonable_encoder
from app.models.movement import MovementModel
from app.services.config import ESConfigService, IndexNames
from app.services.utils import ESUtilityService
from typing import Annotated, Optional
from app.services.crud import ESCrudService
from pydantic import BaseModel

router = APIRouter(prefix="/movement", tags=["movement"])
service = ESCrudService()


@router.get("/", status_code=status.HTTP_200_OK)
def find_art_movements(
    q: Annotated[Optional[str], Query(description="Search input.")] = None,
    count: Annotated[int, Query(description="Maximum number of search results.")] = 3,
):
    return service.read(IndexNames.MOVEMENT, q, count)


@router.post("/", status_code=status.HTTP_201_CREATED)
def add_art_movement(movement: MovementModel = Body(...)):
    mvmnt_doc = jsonable_encoder(movement)
    return service.create(IndexNames.MOVEMENT, mvmnt_doc)


@router.put("/{movement_id}", status_code=status.HTTP_200_OK)
def update_art_movement(
    movement_id: Annotated[str, Path(description="ID of the document to update.")],
    movement=Body(...),
):
    mvmnt_doc = jsonable_encoder(movement)
    return service.update(IndexNames.MOVEMENT, movement_id, mvmnt_doc)


@router.delete("/{movement_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_art_movement(
    movement_id: Annotated[str, Path(description="ID of the document to delete.")]
):
    return service.delete(IndexNames.MOVEMENT, movement_id)
