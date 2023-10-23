from fastapi import FastAPI
from elasticsearch import Elasticsearch, helpers
from app.mappings.movement import movement_mapping
from app.constants import IndexNames
from app.settings import settings

import json
import os.path

app = FastAPI()

INDEX_NAMES = [enum.value for enum in IndexNames]

INDEX_MAPPINGS = {
    "movement": movement_mapping,
}


class ESConfigService(object):
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
            print("Creating indexes failed: ", ex)

    def seed_data(self):
        print("Adding test data..")
        try:
            for index_name in INDEX_NAMES:
                index_exists = self.connection.indices.exists(index=index_name)
                if index_exists:
                    dir = os.path.dirname(os.path.realpath(__file__))
                    filename = os.path.join(dir, f"seed/{index_name}s.json")
                    with open(filename, "r") as file:
                        docs = json.load(file)
                        helpers.bulk(self.connection, docs, index=index_name)
                        print(f"Test data for index {index_name} added.")
        except Exception as ex:
            print("Adding test data failed: ", ex)
