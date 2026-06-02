# Store Intelligence System

**Author:** Subham Upadhya
**Email:** [upadhyaysubham325@gmail.com](mailto:upadhyaysubham325@gmail.com)

---

# Overview

Store Intelligence is an end-to-end retail analytics platform built from CCTV footage.

The system detects people using YOLOv8, tracks their movement across video frames, generates structured events, stores those events in SQLite, exposes analytics through FastAPI endpoints, and visualizes business insights using a Streamlit dashboard.

The goal is to transform raw CCTV footage into actionable store analytics such as visitor counts, dwell time, funnel metrics, and anomaly detection.

---

# Reviewer Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start Backend API

```bash
python -m uvicorn app.main:app --reload
```

Open Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

### 3. Start Dashboard

```bash
streamlit run dashboard/app.py
```

Open Dashboard:

```text
http://localhost:8501
```

### 4. Run Automated Tests

```bash
pytest -q
```

Expected Output:

```text
6 passed
```

### 5. Run Docker Version

```bash
docker compose up --build
```

---

# System Architecture

```text
Video Input
    |
    v
YOLOv8 Person Detection
    |
    v
Multi-Object Tracking
    |
    v
Event Generation
    |
    v
SQLite Database
    |
    v
FastAPI Analytics APIs
    |
    v
Streamlit Dashboard
```

---

# Features

### Computer Vision

* YOLOv8 Person Detection
* Multi-Object Tracking
* Visitor Session Tracking
* Entry/Exit Event Detection

### Event Processing

* Session Started Events
* Session Ended Events
* Dwell Time Updates
* Structured Event Storage

### Analytics

* Total Visitors
* Active Visitors
* Average Dwell Time
* Maximum Dwell Time
* Visitor Funnel Analytics
* Anomaly Detection

### Platform

* FastAPI Backend
* SQLite Storage
* Streamlit Dashboard
* Docker Support
* Automated Testing

---

# Project Structure

```text
store-intelligence
│
├── app
│   ├── anomaly
│   ├── cv
│   ├── db
│   ├── events
│   ├── funnel
│   ├── metrics
│   └── main.py
│
├── dashboard
│   └── app.py
│
├── data
│   ├── database
│   ├── output
│   └── videos
│
├── tests
│
├── README.md
├── DESIGN.md
├── CHOICES.md
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── requirements-docker.txt
└── pytest.ini
```

---

# API Endpoints

## Health Check

```http
GET /health
```

Returns service health status.

---

## Events

```http
GET /events
```

Returns stored events.

```http
POST /events
```

Creates a new event.

---

## Metrics

```http
GET /metrics
```

Returns business metrics including:

* Total Visitors
* Active Visitors
* Average Dwell Time
* Maximum Dwell Time
* Total Events

---

## Funnel

```http
GET /funnel
```

Returns visitor funnel metrics.

---

## Anomalies

```http
GET /anomalies
```

Returns detected anomalies.

---

# Running the Detection Pipeline

### YOLO Validation

```bash
python app/cv/yolo_check.py
```

### Tracking Pipeline

```bash
python app/cv/tracker_test.py
```

### Event Pipeline

```bash
python -m app.cv.event_test
```

---

# Dashboard Features

The Streamlit dashboard provides:

* Processed CCTV Video
* Visitor Metrics
* Funnel Analytics
* Event Viewer
* Anomaly Monitor

Dashboard URL:

```text
http://localhost:8501
```

---

# Technology Stack

* Python
* FastAPI
* Streamlit
* SQLite
* SQLAlchemy
* OpenCV
* YOLOv8 (Ultralytics)
* Pandas
* NumPy
* Pytest
* Docker

---

# Automated Testing

Run:

```bash
pytest -q
```

Expected Result:

```text
6 passed
```

Covered Endpoints:

* Root
* Health
* Metrics
* Funnel
* Anomalies
* Events

---

# Docker Support

Build and Run:

```bash
docker compose up --build
```

API Documentation:

```text
http://localhost:8000/docs
```

Dashboard:

```text
http://localhost:8501
```

---

# Business Metrics Generated

The platform generates:

* Total Visitors
* Active Visitors
* Average Dwell Time
* Maximum Dwell Time
* Visitor Funnel Metrics
* Event Counts
* Anomaly Signals

---

# Known Limitations

* Staff filtering is not implemented
* Re-entry handling is basic
* Tracking may reset under heavy occlusion
* Accuracy depends on camera quality and placement
* Multi-camera fusion is not implemented
* Real-time streaming is not implemented

---

# Future Improvements

* Staff Identification
* Multi-Camera Fusion
* Zone Analytics
* Conversion Analytics
* Real-Time Processing
* Advanced Anomaly Detection
* Customer Journey Analytics

---

# Submission Notes

This project prioritizes building a complete end-to-end store intelligence pipeline over maximizing detection accuracy.

The focus areas are:

* Detection Pipeline
* Event Generation
* Business Analytics
* API Design
* System Architecture
* Reproducibility
* Docker Deployment
* Engineering Trade-offs

---

Built by **Subham Upadhya**
Email: **[upadhyaysubham325@gmail.com](mailto:upadhyaysubham325@gmail.com)**
