import cv2

from ultralytics import YOLO

from app.events.event_generator import handle_track
from app.events.event_writer import save_event


VIDEO_PATH = "data/videos/video1.mp4"

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(VIDEO_PATH)

while True:

    success, frame = cap.read()

    if not success:
        break

    results = model.track(
        frame,
        persist=True,
        classes=[0],
        conf=0.25,
        iou=0.5,
        verbose=False
    )

    if results[0].boxes.id is not None:

        track_ids = (
            results[0]
            .boxes
            .id
            .cpu()
            .numpy()
            .astype(int)
        )

        for track_id in track_ids:

            track_id = int(track_id)

            events = handle_track(track_id)

            for event in events:

                print(event)

                save_event(
                    event_type=event["event_type"],
                    track_id=track_id,
                    timestamp=event["timestamp"],
                    dwell_time=event.get(
                        "dwell_time",
                        0
                    )
                )

    annotated = results[0].plot()

    cv2.imshow(
        "Event Generator",
        annotated
    )

    if cv2.waitKey(1) == 27:
        break

cap.release()

cv2.destroyAllWindows()