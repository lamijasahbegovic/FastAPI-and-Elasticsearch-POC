from fastapi import FastAPI, status
from app.controllers.movements import router as movement_router
from app.services.config import ESConfigService

app = FastAPI()


@app.on_event("startup")
def startup_events():
    print("Starting up..")
    es_config = ESConfigService()
    es_config.create_indexes()


@app.on_event("shutdown")
def shutdown_events():
    print("Shutting down..")


@app.post("/seed", status_code=status.HTTP_201_CREATED)
def add_seed_data():
    es_config = ESConfigService()
    es_config.seed_data()
    return


app.include_router(movement_router)
