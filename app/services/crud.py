from app.services.config import ESConfigService, IndexNames
from app.services.utils import ESUtilityService
from typing import Optional
from pydantic import BaseModel


class ESCrudService(object):
    def __init__(self) -> None:
        self.config = ESConfigService()
        self.utils = ESUtilityService()

    def create(self, index: IndexNames, body: BaseModel):
        """
        Method for adding a single new document for the specified index.
        """

        try:
            self.config.connection.index(index=index, body=body)
            return body
        except Exception as ex:
            print("Error during creation: ", ex)

    def read(self, index: IndexNames, q: Optional[str], count: int = 3):
        """
        Method for a basic search functionality for a specific index.
        """

        try:
            result = self.config.connection.search(index=index, q=q, size=count)
            return self.utils.process_response(result)
        except Exception as ex:
            print("Search error: ", ex)

    # TODO: UPDATE METHOD

    def delete_by_query(self, index: IndexNames, query: str):
        """
        Method for deleting a document found through a query for a specific index.
        """

        try:
            self.config.connection.delete_by_query(index=index, body=query)
        except Exception as ex:
            print("Error during deletion: ", ex)
