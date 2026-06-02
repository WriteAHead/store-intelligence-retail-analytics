from datetime import datetime


active_tracks = {}


def handle_track(
    track_id: int
):

    events = []

    current_time = datetime.now()

    if track_id not in active_tracks:

        active_tracks[track_id] = {
            "start_time": current_time
        }

        events.append(
            {
                "event_type": "SESSION_STARTED",
                "track_id": track_id,
                "timestamp": current_time.isoformat()
            }
        )

    else:

        dwell_time = (
            current_time
            - active_tracks[track_id]["start_time"]
        ).total_seconds()

        events.append(
            {
                "event_type": "DWELL_TIME_UPDATED",
                "track_id": track_id,
                "timestamp": current_time.isoformat(),
                "dwell_time": round(
                    dwell_time,
                    2
                )
            }
        )

    return events


def close_track(
    track_id: int
):

    if track_id not in active_tracks:
        return None

    current_time = datetime.now()

    session = active_tracks[track_id]

    dwell_time = (
        current_time
        - session["start_time"]
    ).total_seconds()

    del active_tracks[track_id]

    return {
        "event_type": "SESSION_ENDED",
        "track_id": track_id,
        "timestamp": current_time.isoformat(),
        "dwell_time": round(
            dwell_time,
            2
        )
    }