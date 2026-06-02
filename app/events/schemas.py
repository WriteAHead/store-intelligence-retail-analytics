from pydantic import BaseModel


class EventCreate(BaseModel):

    event_id: str

    timestamp: str

    camera_id: str

    track_id: int

    event_type: str

    event_metadata: str = ""

    dwell_time: float = 0.0