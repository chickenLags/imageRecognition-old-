import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    grayscaled = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY, 115, 1)
    


    cv2.imshow("video", frame)
    cv2.imshow("vid_gray", grayscaled)
    cv2.imshow("vid_gaus", gaus)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
