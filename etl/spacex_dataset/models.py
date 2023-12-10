from datetime import datetime

from pydantic import BaseModel


class RocketModel(BaseModel):
    id: str
    name: str
    description: str
    wikipedia: str


class MissionModel(RocketModel):
    id: str
    name: str
    description: str
    twitter: str
    website: str
    wikipedia: str


class LaunchLinksModel(BaseModel):
    article_link: str | None
    presskit: str | None
    reddit_campaign: str | None
    reddit_launch: str | None
    reddit_media: str | None
    reddit_recovery: str | None
    video_link: str | None
    wikipedia: str | None


class LaunchModel(BaseModel):
    id: str
    details: str | None
    launch_date_local: datetime
    launch_date_utc: datetime
    links: LaunchLinksModel
    mission_name: str | None
