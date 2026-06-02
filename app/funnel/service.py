from sqlalchemy.orm import Session

from app.events.models import Event


def calculate_funnel(db: Session):

    events = db.query(Event).all()

    sessions_started = len(
        [
            e
            for e in events
            if e.event_type == "SESSION_STARTED"
        ]
    )

    dwell_30 = len(
        [
            e
            for e in events
            if e.dwell_time >= 30
        ]
    )

    dwell_60 = len(
        [
            e
            for e in events
            if e.dwell_time >= 60
        ]
    )

    dwell_120 = len(
        [
            e
            for e in events
            if e.dwell_time >= 120
        ]
    )

    return {
        "sessions_started": sessions_started,
        "stay_30_seconds": dwell_30,
        "stay_60_seconds": dwell_60,
        "stay_120_seconds": dwell_120
    }