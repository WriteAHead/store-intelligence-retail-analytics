import cv2

from ultralytics import YOLO


VIDEO_PATH = "data/videos/video1.mp4"
OUTPUT_PATH = "data/output/tracked_output.mp4"

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(VIDEO_PATH)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")

writer = cv2.VideoWriter(
    OUTPUT_PATH,
    fourcc,
    fps,
    (width, height)
)

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

    annotated_frame = results[0].plot()

    writer.write(annotated_frame)

    cv2.imshow(
        "Tracking",
        annotated_frame
    )

    if cv2.waitKey(1) == 27:
        break

cap.release()
writer.release()

cv2.destroyAllWindows()

print("Video saved to:", OUTPUT_PATH)