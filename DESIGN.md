# Store Intelligence System Design

## Overview

This system processes CCTV footage and transforms raw video streams into business-relevant retail analytics.

The solution focuses on practical deployment and engineering simplicity rather than perfect computer vision accuracy.

Pipeline:

Video Input
→ Person Detection (YOLOv8)
→ Multi-Object Tracking
→ Event Generation
→ Event Storage
→ Metrics Computation
→ Dashboard Visualization

---

## Components

### Detection Layer

YOLOv8n is used for person detection.

Reasoning:

* Fast CPU execution
* Minimal setup
* Sufficient accuracy for retail analytics

### Tracking Layer

Ultralytics tracking is used with persistent track IDs.

Generated outputs:

* Track ID
* Bounding Box
* Session State

### Event Layer

Events generated:

* SESSION_STARTED
* DWELL_TIME_UPDATED
* SESSION_ENDED
* PERSON_ENTERED
* PERSON_EXITED

### Storage Layer

SQLite stores all generated events.

Reasoning:

* Lightweight
* No external dependency
* Easy local deployment

### API Layer

FastAPI exposes:

* /events
* /metrics
* /funnel
* /anomalies

### Dashboard Layer

Streamlit dashboard provides:

* KPI metrics
* Funnel visualization
* Event inspection
* Anomaly review

---

## Data Flow

Video
→ Detection
→ Tracking
→ Event Generation
→ SQLite
→ FastAPI
→ Streamlit Dashboard

---

## Assumptions

* CCTV cameras are fixed.
* Store layout changes infrequently.
* Approximate visitor counts are acceptable.
* Business metrics are prioritized over perfect detection accuracy.

---

## Future Improvements

* Staff identification
* Better re-entry handling
* Zone analytics
* Real-time streaming
* Multi-camera fusion
