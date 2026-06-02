import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Store Intelligence Dashboard",
    layout="wide"
)

st.title("Store Intelligence Dashboard")

st.caption(
    "Built by Subham Upadhya | upadhyaysubham325@gmail.com"
)

st.divider()

# ==================================================
# VIDEO SECTION
# ==================================================

st.subheader("Processed CCTV Feed")

VIDEO_PATH = "tracked_output_web.mp4"

if os.path.exists(VIDEO_PATH):

    video_file = open(
        VIDEO_PATH,
        "rb"
    )

    video_bytes = video_file.read()

    st.video(video_bytes)

else:

    st.error(
        f"Video not found: {VIDEO_PATH}"
    )

st.divider()

# ==================================================
# METRICS
# ==================================================

st.subheader("Business Metrics")

metrics = {
    "total_visitors": 93,
    "active_visitors": 0,
    "average_dwell_time": 300,
    "total_events": 186
}

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Visitors",
        metrics["total_visitors"]
    )

with col2:
    st.metric(
        "Active Visitors",
        metrics["active_visitors"]
    )

with col3:
    st.metric(
        "Average Dwell Time",
        metrics["average_dwell_time"]
    )

with col4:
    st.metric(
        "Total Events",
        metrics["total_events"]
    )

st.divider()

# ==================================================
# FUNNEL
# ==================================================

st.subheader("Visitor Funnel")

funnel_df = pd.DataFrame(
    {
        "Stage": [
            "Sessions",
            "30 Seconds",
            "60 Seconds",
            "120 Seconds"
        ],
        "Count": [
            1,
            16,
            1,
            1
        ]
    }
)

st.bar_chart(
    funnel_df,
    x="Stage",
    y="Count"
)

st.divider()

# ==================================================
# EVENTS
# ==================================================

st.subheader("Recent Events")

events_df = pd.DataFrame(
    [
        {
            "event_type": "PERSON_ENTERED",
            "track_id": 1,
            "camera_id": "cam_1"
        },
        {
            "event_type": "PERSON_EXITED",
            "track_id": 1,
            "camera_id": "cam_1"
        }
    ]
)

st.dataframe(
    events_df,
    use_container_width=True
)

st.divider()

# ==================================================
# ANOMALIES
# ==================================================

st.subheader("Anomaly Monitor")

st.success(
    "No anomalies detected"
)

st.divider()

st.caption(
    "Store Intelligence Platform | YOLOv8 | Tracking | Event Analytics"
)
