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
        TODO: Implement creating documents in a bulk (separate from the seed_data() implementation.)
        """

        try:
            self.config.connection.index(index=index, body=body)
            return body
        except Exception as ex:
            print("Error during creation: ", ex)

    def read(self, index: IndexNames, q: Optional[str], count: int = 3):
        """
        Method for a basic search functionality for a specific index.
        TODO: Implement a more complex search.
        """

        try:
            result = self.config.connection.search(index=index, q=q, size=count)
            return self.utils.process_response(result)
        except Exception as ex:
            print("Search error: ", ex)

    def update(self, index: IndexNames, doc_id: str, update_body: BaseModel):
        """
        Method for updating a document for a specific index by the document ID. The document can be partly or completely updated.
        TODO: Disallow updating certain properties.
        TODO: Implement updating by query.
        """

        try:
            result = self.config.connection.get(index=index, id=doc_id)
            doc_body = result["_source"]

            for key, value in update_body.items():
                doc_body[key] = value

            self.config.connection.update(
                index=index, id=doc_id, body={"doc": doc_body}
            )
            return doc_body
        except Exception as ex:
            print("Error during update: ", ex)

    def delete(self, index: IndexNames, doc_id: str):
        """
        Method for deleting a document for a specific index by the document ID.
        TODO: Implement deleting by query.
        """

        try:
            self.config.connection.delete(index=index, id=doc_id)
            return {}
        except Exception as ex:
            print("Error during deletion: ", ex)
