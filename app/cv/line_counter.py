import cv2

from ultralytics import YOLO


VIDEO_PATH = "data/videos/entry_gate.mp4"

LINE_X = 980

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(VIDEO_PATH)

track_history = {}

entered_tracks = set()
exited_tracks = set()

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

    cv2.line(
        frame,
        (LINE_X, 0),
        (LINE_X, frame.shape[0]),
        (0, 0, 255),
        3
    )

    if results[0].boxes.id is not None:

        boxes = results[0].boxes.xyxy.cpu().numpy()
        track_ids = results[0].boxes.id.cpu().numpy().astype(int)

        for box, track_id in zip(boxes, track_ids):

            x1, y1, x2, y2 = box

            center_x = int((x1 + x2) / 2)

            if track_id not in track_history:
                track_history[track_id] = center_x
                continue

            previous_x = track_history[track_id]

            # Outside -> Inside
            if previous_x > LINE_X and center_x < LINE_X:

                if track_id not in entered_tracks:

                    entered_tracks.add(track_id)

                    print(
                        f"PERSON_ENTERED | Track {track_id}"
                    )

            # Inside -> Outside
            if previous_x < LINE_X and center_x > LINE_X:

                if track_id not in exited_tracks:

                    exited_tracks.add(track_id)

                    print(
                        f"PERSON_EXITED | Track {track_id}"
                    )

            track_history[track_id] = center_x

    annotated_frame = results[0].plot()

    cv2.line(
        annotated_frame,
        (LINE_X, 0),
        (LINE_X, annotated_frame.shape[0]),
        (0, 0, 255),
        3
    )

    cv2.imshow(
        "Line Counter",
        annotated_frame
    )

    if cv2.waitKey(1) == 27:
        break

cap.release()

cv2.destroyAllWindows()