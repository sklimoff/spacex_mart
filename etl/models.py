from uuid import uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    ...


class MediaTypeModel(Base):
    __tablename__ = 'media_type'

    id: Mapped[str] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(unique=True)


class RocketModel(Base):
    __tablename__ = 'rocket'

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]


class RocketPublicationModel(Base):
    __tablename__ = 'rocket_publication'

    id: Mapped[str] = mapped_column(primary_key=True, default=uuid4)
    rocket_id: Mapped[str] = mapped_column(
        ForeignKey('rocket.id', ondelete='CASCADE')
    )
    rocket: Mapped['RocketModel'] = relationship()
    media_type_id: Mapped[str] = mapped_column(
        ForeignKey('media_type.id', ondelete='CASCADE')
    )
    media_type: Mapped['MediaTypeModel'] = relationship()
    ref: Mapped[str]


class MissionModel(Base):
    __tablename__ = 'mission'

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]


class MissionPublicationModel(Base):
    __tablename__ = 'mission_publication'

    id: Mapped[str] = mapped_column(primary_key=True, default=uuid4)
    mission_id: Mapped[str] = mapped_column(
        ForeignKey('mission.id', ondelete='CASCADE')
    )
    mission: Mapped['MissionModel'] = relationship()
    media_type_id: Mapped[str] = mapped_column(
        ForeignKey('media_type.id', ondelete='CASCADE')
    )
    media_type: Mapped['MediaTypeModel'] = relationship()
    ref: Mapped[str]


class LaunchModel(Base):
    __tablename__ = 'launch'

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]
    details: Mapped[str | None]


class LaunchPublicationModel(Base):
    __tablename__ = 'launch_publication'

    id: Mapped[str] = mapped_column(primary_key=True, default=uuid4)
    launch_id: Mapped[str] = mapped_column(
        ForeignKey('launch.id', ondelete='CASCADE')
    )
    launch: Mapped['LaunchModel'] = relationship()
    media_type_id: Mapped[str] = mapped_column(
        ForeignKey('media_type.id', ondelete='CASCADE')
    )
    media_type: Mapped['MediaTypeModel'] = relationship()
    ref: Mapped[str]


class SpaceXDataMartModel(Base):
    __tablename__ = 'data_mart'

    id: Mapped[str] = mapped_column(primary_key=True, default=uuid4)
    type: Mapped[int]
    name: Mapped[str]
    media_type_name: Mapped[str]
    ref: Mapped[str]
    count: Mapped[int]
