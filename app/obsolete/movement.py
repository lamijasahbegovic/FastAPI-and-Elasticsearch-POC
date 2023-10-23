from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from app.models.movement import Movement, MovementUpdate

router = APIRouter()


@router.post(
    "/",
    response_description="Create a new art movement",
    status_code=status.HTTP_201_CREATED,
    response_model=Movement,
)
def create_movement(request: Request, movement: Movement = Body(...)):
    Movement = jsonable_encoder(movement)
    new_movement = request.app.database["movements"].insert_one(Movement)
    created_movement = request.app.database["movements"].find_one(
        {"_id": new_movement.inserted_id}
    )

    return created_movement


@router.get(
    "/", response_description="Get all movements", response_model=List[Movement]
)
def get_movements(request: Request):
    movements = list(request.app.database["movements"].find(limit=100))
    return movements


@router.get(
    "/{id}", response_description="Get a single movement by id", response_model=Movement
)
def find_movement(id: str, request: Request):
    if (
        movement := request.app.database["movements"].find_one({"_id": id})
    ) is not None:
        return movement

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Movement with ID {id} not found"
    )


@router.put("/{id}", response_description="Update a movement", response_model=Movement)
def update_movement(id: str, request: Request, movement: MovementUpdate = Body(...)):
    movement = {k: v for k, v in movement.model_dump().items() if v is not None}

    if len(movement) >= 1:
        update_result = request.app.database["movements"].update_one(
            {"_id": id}, {"$set": movement}
        )

        if update_result.modified_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Movement with ID {id} not found",
            )

    if (
        existing_movement := request.app.database["movements"].find_one({"_id": id})
    ) is not None:
        return existing_movement

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Movement with ID {id} not found"
    )


@router.delete("/{id}", response_description="Delete a movement")
def delete_movement(id: str, request: Request, response: Response):
    delete_result = request.app.database["movements"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Movement with ID {id} not found"
    )
