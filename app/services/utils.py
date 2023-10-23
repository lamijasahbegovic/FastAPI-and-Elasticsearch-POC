from typing import Any
from elastic_transport import ObjectApiResponse


class ESUtilityService(object):
    def process_response(self, response: ObjectApiResponse[Any]):
        hits: list[dict] = response["hits"]["hits"]
        data: list[dict] = []
        count: int = 0

        for hit in hits:
            source_data = hit["_source"]

            count += 1
            data.append(source_data)

        return {"count": count, "data": data}
