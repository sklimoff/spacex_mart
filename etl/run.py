from config import config
from models import (LaunchModel, LaunchPublicationModel, MediaTypeModel,
                    MissionModel, MissionPublicationModel, RocketModel,
                    RocketPublicationModel, SpaceXDataMartModel)
from spacex_dataset.launches import LaunchesRequest
from spacex_dataset.missions import MissionsRequest
from spacex_dataset.rockets import RocketsRequest
from sqlalchemy import create_engine, delete, select
from sqlalchemy.orm import Session, sessionmaker


def get_or_create_media_type(*, session: Session, name: str) -> MediaTypeModel:
    stmt = select(MediaTypeModel).where(MediaTypeModel.name == name)
    entity = session.execute(stmt).scalar_one_or_none()
    if entity is None:
        entity = MediaTypeModel(name=name)
        session.add(entity)
        session.flush()
    return entity


def main() -> None:
    engine = create_engine(config.get_postgres_dsn())
    session_factory = sessionmaker(bind=engine)
    with session_factory() as session:
        for item in LaunchesRequest().get_data():
            entity = session.get(LaunchModel, item.id)
            if entity is None:
                name = f'{item.mission_name} ({item.launch_date_utc.strftime("%b %d %Y")})'
                entity = LaunchModel(
                    id=item.id, name=name, details=item.details
                )
                session.add(entity)
                session.flush()
            links_dict = item.links.model_dump()
            fields = [
                'article_link',
                'presskit',
                'reddit_campaign',
                'reddit_launch',
                'reddit_launch',
                'reddit_media',
                'reddit_recovery',
                'wikipedia',
            ]
            for field in fields:
                if links_dict[field] is None:
                    continue
                media_type = get_or_create_media_type(
                    session=session, name=field
                )
                stmt = select(LaunchPublicationModel).where(
                    LaunchPublicationModel.launch == entity
                    and LaunchPublicationModel.media_type == media_type
                    and LaunchPublicationModel.ref == links_dict[field]
                )
                pub = session.execute(stmt).scalar_one_or_none()
                if pub is None:
                    session.add(
                        LaunchPublicationModel(
                            launch=entity,
                            media_type=media_type,
                            ref=links_dict[field],
                        )
                    )
                    session.flush()

        for item in RocketsRequest().get_data():
            entity = session.get(RocketModel, item.id)
            if entity is None:
                entity = RocketModel(
                    id=item.id,
                    name=item.name,
                    description=item.description,
                )

                session.add(entity)
                session.flush()
            if item.wikipedia is None:
                continue
            media_type = get_or_create_media_type(session=session, name=field)
            stmt = select(RocketPublicationModel).where(
                RocketPublicationModel.rocket == entity
                and RocketPublicationModel.media_type == media_type
                and RocketPublicationModel.ref == links_dict[field]
            )
            pub = session.execute(stmt).scalar_one_or_none()
            if pub is None:
                session.add(
                    RocketPublicationModel(
                        rocket=entity,
                        media_type=media_type,
                        ref=item.wikipedia,
                    )
                )
                session.flush()

        for item in MissionsRequest().get_data():
            entity = session.get(MissionModel, item.id)
            if entity is None:
                entity = MissionModel(
                    id=item.id,
                    name=item.name,
                    description=item.description,
                )
                session.add(entity)
                session.flush()
            links_dict = item.model_dump()
            fields = ['twitter', 'website', 'wikipedia']
            for field in fields:
                if links_dict[field] is None:
                    continue
                media_type = get_or_create_media_type(
                    session=session, name=field
                )
                stmt = select(MissionPublicationModel).where(
                    MissionPublicationModel.launch == entity
                    and MissionPublicationModel.media_type == media_type
                    and MissionPublicationModel.ref == links_dict[field]
                )
                pub = session.execute(stmt).scalar_one_or_none()
                if pub is None:
                    session.add(
                        MissionPublicationModel(
                            launch=entity,
                            media_type=media_type,
                            ref=links_dict[field],
                        )
                    )
                    session.flush()

        session.commit()

        session.execute(delete(SpaceXDataMartModel))

        for launch_pub in session.scalars(select(LaunchPublicationModel)):
            session.add(
                SpaceXDataMartModel(
                    type=1,
                    name=launch_pub.launch.name,
                    media_type_name=launch_pub.media_type.name,
                    ref=launch_pub.ref,
                    count=1,
                )
            )

        for mission_pub in session.scalars(select(MissionPublicationModel)):
            session.add(
                SpaceXDataMartModel(
                    type=2,
                    name=mission_pub.mission.name,
                    media_type_name=mission_pub.media_type.name,
                    ref=mission_pub.ref,
                    count=1,
                )
            )

        for rocket_pub in session.scalars(select(RocketPublicationModel)):
            session.add(
                SpaceXDataMartModel(
                    type=3,
                    name=rocket_pub.rocket.name,
                    media_type_name=rocket_pub.media_type.name,
                    ref=rocket_pub.ref,
                    count=1,
                )
            )

        session.commit()


if __name__ == '__main__':
    main()
