from sqlalchemy.orm import Session

from app.events.models import Event
from app.events.schemas import EventCreate


def create_event(
    db: Session,
    event: EventCreate
):

    db_event = Event(
        event_id=event.event_id,
        timestamp=event.timestamp,
        camera_id=event.camera_id,
        track_id=event.track_id,
        event_type=event.event_type,
        event_metadata=event.event_metadata,
        dwell_time=event.dwell_time
    )

    db.add(db_event)

    db.commit()

    db.refresh(db_event)

    return db_event


def get_events(
    db: Session
):

    return db.query(Event).all()