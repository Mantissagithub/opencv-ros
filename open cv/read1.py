import cv2 as cv

# Open the webcam
capture = cv.VideoCapture(0)

# Check if the webcam was opened successfully
while True:
    isTrue, frame = capture.read()
    cv.imshow('Webcam', frame)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

# Release the webcam and close all windows
capture.release()
cv.destroyAllWindows()