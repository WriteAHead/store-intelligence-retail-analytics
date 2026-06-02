import cv2

from ultralytics import YOLO

VIDEO_PATH = "data/videos/video1.mp4"

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(VIDEO_PATH)

frame_count = 0

while True:

    success, frame = cap.read()

    if not success:
        break

    frame_count += 1

    if frame_count % 5 != 0:
        continue

    results = model(frame, verbose=False)

    person_count = 0

    for box in results[0].boxes:

        cls = int(box.cls[0])

        if cls == 0:

            person_count += 1

            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0]
            )

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

    print("Persons:", person_count)

    cv2.putText(
        frame,
        f"Persons: {person_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    cv2.imshow(
        "Store Intelligence",
        frame
    )

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()