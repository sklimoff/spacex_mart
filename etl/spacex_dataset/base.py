from abc import ABC, abstractmethod

import requests
from graphql_query import Query, Operation, Field
from pydantic import BaseModel


class BaseRequest(ABC):
    _query_name: str
    _model: BaseModel
    _url: str = 'https://spacex-production.up.railway.app/'

    @classmethod
    def _get_fields_list(cls, model: BaseModel) -> list[str | Field]:
        fields = []
        for field_name, field_info in model.model_fields.items():
            print(field_info)
            if isinstance(field_info.annotation, type) and issubclass(field_info.annotation, BaseModel):
                fields.append(Field(name=field_name, fields=cls._get_fields_list(field_info.annotation)))
            else:
                fields.append(field_name)
        return fields

    def get_data(self) -> list[BaseModel]:
        query = Query(name=self._query_name, fields=self._get_fields_list(self._model))
        print(query.render())
        operation = Operation(queries=[query])
        response = requests.post(url=self._url, json={'query': operation.render()})
        data = response.json()['data']
        for item in data[self._query_name]:
            yield self._model(**item)
