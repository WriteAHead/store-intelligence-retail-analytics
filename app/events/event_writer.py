from app.db.database import SessionLocal
from app.events.models import Event


def save_event(
    event_type,
    track_id,
    timestamp,
    dwell_time=0
):

    db = SessionLocal()

    try:

        event = Event(
            event_id=f"{event_type}_{track_id}_{timestamp}",
            timestamp=str(timestamp),
            camera_id="camera_1",
            track_id=int(track_id),
            event_type=str(event_type),
            event_metadata="generated",
            dwell_time=float(dwell_time)
        )

        db.add(event)

        db.commit()

        print(
            f"SAVED -> {event_type}"
        )

    except Exception as e:

        print(
            f"DB ERROR -> {e}"
        )

    finally:

        db.close()