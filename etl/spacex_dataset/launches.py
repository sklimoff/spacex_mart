from spacex_dataset.base import BaseRequest
from spacex_dataset.models import LaunchModel


class LaunchesRequest(BaseRequest):
    _query_name: str = 'launches'
    _model: LaunchModel = LaunchModel
