from sqlalchemy.orm import Session

from app.events.models import Event


def detect_anomalies(db: Session):

    events = db.query(Event).all()

    anomalies = []

    high_dwell = [
        e
        for e in events
        if e.dwell_time > 300
    ]

    for event in high_dwell:

        anomalies.append(
            {
                "type": "HIGH_DWELL_TIME",
                "track_id": event.track_id,
                "dwell_time": event.dwell_time
            }
        )

    if len(events) == 0:

        anomalies.append(
            {
                "type": "NO_ACTIVITY_DETECTED"
            }
        )

    return anomalies