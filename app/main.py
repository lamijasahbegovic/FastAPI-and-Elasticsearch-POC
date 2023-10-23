from fastapi import FastAPI
from app.routes import router as movement_router
from app.es_config import ESConfig

app = FastAPI()


@app.on_event("startup")
def startup_events():
    print("Starting up..")
    es_config = ESConfig()
    es_config.create_indexes()


@app.on_event("shutdown")
def shutdown_events():
    print("Shutting down..")


app.include_router(movement_router, tags=["movement"], prefix="/movement")
