from sqlalchemy.orm import Session

from app.events.models import Event


def calculate_metrics(db: Session):

    events = db.query(Event).all()

    session_started = [
        e for e in events
        if e.event_type == "SESSION_STARTED"
    ]

    session_ended = [
        e for e in events
        if e.event_type == "SESSION_ENDED"
    ]

    dwell_events = [
        e.dwell_time
        for e in events
        if e.dwell_time > 0
    ]

    total_visitors = len(session_started)

    active_visitors = max(
        total_visitors - len(session_ended),
        0
    )

    average_dwell_time = 0

    if dwell_events:

        average_dwell_time = (
            sum(dwell_events)
            / len(dwell_events)
        )

    max_dwell_time = 0

    if dwell_events:

        max_dwell_time = max(dwell_events)

    return {
        "total_visitors": total_visitors,
        "active_visitors": active_visitors,
        "sessions_started": len(session_started),
        "sessions_ended": len(session_ended),
        "average_dwell_time": round(
            average_dwell_time,
            2
        ),
        "max_dwell_time": round(
            max_dwell_time,
            2
        ),
        "total_events": len(events)
    }