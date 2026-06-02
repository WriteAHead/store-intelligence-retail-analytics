# Engineering Decisions and Trade-offs

## Why YOLOv8n?

Alternative:

* Larger YOLO models

Decision:

* YOLOv8n

Reason:
The challenge emphasizes working systems over model complexity. YOLOv8n provides adequate accuracy while running efficiently on CPU hardware.

---

## Why SQLite?

Alternative:

* PostgreSQL
* MySQL

Decision:

* SQLite

Reason:
The project is evaluated locally and does not require distributed infrastructure.

---

## Why Event-Based Architecture?

Alternative:

* Direct metric computation from video

Decision:

* Generate structured events first

Reason:
Events provide traceability and make downstream analytics easier to validate.

---

## Why Tracking Instead of Frame Counting?

Alternative:

* Count detections per frame

Decision:

* Persistent tracking IDs

Reason:
Tracking reduces duplicate counts and enables dwell-time computation.

---

## Entry/Exit Counting Trade-off

Challenge:
Mirror reflections, occlusion, and crowd movement can affect accuracy.

Decision:
Use tracking combined with line-crossing logic.

Reason:
Provides reasonable approximation while keeping implementation simple.

---

## Dashboard Trade-off

Decision:
Streamlit dashboard

Reason:
Fast development, easy review, minimal deployment complexity.

---

## Known Limitations

* Re-entry handling is basic.
* Staff filtering is not implemented.
* Accuracy depends on camera placement.
* Tracking IDs may occasionally reset under heavy occlusion.

---

## Conclusion

The project prioritizes reliability, simplicity, explainability, and end-to-end functionality over model sophistication.
