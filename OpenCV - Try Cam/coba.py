import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture('http://192.168.1.101:8080/video')
wCam, hCam = 640, 480
cap.set(3, wCam)
cap.set(4, hCam)

if not cap.isOpened():
    print("Cannot open video capture")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Cannot read frame")
        break


    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()