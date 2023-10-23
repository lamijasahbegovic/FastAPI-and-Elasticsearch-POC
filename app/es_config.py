from fastapi import FastAPI
from elasticsearch import Elasticsearch
from app.movement import mapping as movement_mapping
from enum import Enum

from app.settings import settings

app = FastAPI()


class IndexName(str, Enum):
    MOVEMENT = "movement"


INDEX_NAMES = [enum.value for enum in IndexName]

INDEX_MAPPINGS = {
    "movement": movement_mapping,
}

# INDEX_SETTINGS = {...} # TODO: INVESTIGATE OPTIONS AND IMPLEMENT SOME


class ESConfig(object):
    def __init__(self) -> None:
        self.connection = Elasticsearch(settings.ES_HOST)

    def create_indexes(self):
        print("Creating indexes..")
        try:
            for index_name in INDEX_NAMES:
                index_exists = self.connection.indices.exists(index=index_name)
                if not index_exists:
                    self.connection.indices.create(
                        index=index_name, mappings=INDEX_MAPPINGS[index_name]
                    )
                    print(f"Index {index_name} created.")
        except Exception as ex:
            print("Creating indexes caused an error: ", ex)
