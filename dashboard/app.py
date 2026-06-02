```python
import os
import requests
import streamlit as st
import pandas as pd

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

st.warning(
    """
    **The processed CCTV video is being downloaded from cloud storage.**

    **Please be patient for a few minutes.**

    Download time depends on:
    - Internet speed
    - Streamlit Cloud server load
    - Video size

    Once the download completes, the video player will automatically appear below.
    """
)

FILE_ID = "1q51nhQ3J80MAr7cOcva66ZTAUMghabIB"

VIDEO_URL = (
    f"https://drive.google.com/uc?export=download&id={FILE_ID}"
)

VIDEO_PATH = "tracked_output_web.mp4"

if not os.path.exists(VIDEO_PATH):

    try:

        st.info(
            "Downloading processed CCTV video..."
        )

        response = requests.get(
            VIDEO_URL,
            stream=True,
            timeout=600
        )

        total_size = int(
            response.headers.get(
                "content-length",
                0
            )
        )

        progress_bar = st.progress(0)

        status_text = st.empty()

        downloaded = 0

        with open(VIDEO_PATH, "wb") as file:

            for chunk in response.iter_content(
                chunk_size=1024 * 1024
            ):

                if chunk:

                    file.write(chunk)

                    downloaded += len(chunk)

                    if total_size > 0:

                        percentage = int(
                            downloaded * 100 / total_size
                        )

                        progress_bar.progress(
                            min(
                                percentage,
                                100
                            )
                        )

                        status_text.text(
                            f"Download Progress: {percentage}%"
                        )

        progress_bar.empty()

        status_text.empty()

        st.success(
            "Video downloaded successfully."
        )

    except Exception as e:

        st.error(
            f"Video download failed: {e}"
        )

if os.path.exists(VIDEO_PATH):

    st.video(VIDEO_PATH)

else:

    st.warning(
        "Video is not available yet."
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
    funnel_df.set_index("Stage")
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
```
