import cv2
from src.lane_detection import detect_lanes
from src.damage_detection import detect_damage

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = detect_lanes(frame)
    frame = detect_damage(frame)

    cv2.imshow("Smart AI Car Vision", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
