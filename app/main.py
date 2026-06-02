from fastapi import FastAPI
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.database import Base
from app.db.database import engine

from app.db.session import get_db

from app.events.models import Event
from app.events.schemas import EventCreate
from app.events.crud import create_event
from app.events.crud import get_events

from app.metrics.service import calculate_metrics
from app.funnel.service import calculate_funnel
from app.anomaly.service import detect_anomalies

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Store Intelligence API",
    version="1.0.0"
)


@app.get("/")
def root():

    return {
        "message": "Store Intelligence System"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.post("/events")
def add_event(
    event: EventCreate,
    db: Session = Depends(get_db)
):

    created = create_event(
        db,
        event
    )

    return {
        "id": created.id,
        "event_type": created.event_type
    }


@app.get("/events")
def events(
    db: Session = Depends(get_db)
):

    all_events = get_events(db)

    return {
        "count": len(all_events),
        "events": [
            {
                "id": e.id,
                "event_id": e.event_id,
                "event_type": e.event_type,
                "track_id": e.track_id,
                "camera_id": e.camera_id
            }
            for e in all_events
        ]
    }


@app.get("/metrics")
def metrics(
    db: Session = Depends(get_db)
):

    return calculate_metrics(db)


@app.get("/funnel")
def funnel(
    db: Session = Depends(get_db)
):

    return calculate_funnel(db)


@app.get("/anomalies")
def anomalies(
    db: Session = Depends(get_db)
):

    return {
        "anomalies": detect_anomalies(db)
    }