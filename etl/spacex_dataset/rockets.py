from spacex_dataset.base import BaseRequest
from spacex_dataset.models import RocketModel


class RocketsRequest(BaseRequest):
    _query_name: str = 'rockets'
    _model: RocketModel = RocketModel
