from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float

from app.db.database import Base


class Event(Base):

    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)

    event_id = Column(String, nullable=False)

    timestamp = Column(String, nullable=False)

    camera_id = Column(String, nullable=False)

    track_id = Column(Integer, nullable=False)

    event_type = Column(String, nullable=False)

    event_metadata = Column(String)

    dwell_time = Column(Float, default=0.0)