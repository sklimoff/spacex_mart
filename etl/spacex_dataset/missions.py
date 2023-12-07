from spacex_dataset.base import BaseRequest
from spacex_dataset.models import MissionModel


class MissionsRequest(BaseRequest):
    _query_name: str = 'missions'
    _model: MissionModel = MissionModel
