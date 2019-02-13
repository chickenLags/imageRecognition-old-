# in this file video and webcam will be used.
import cv2

    # this captures the video from the "first" webcam encountered. 
cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    # this shows the feed of the webcam in color and in gray scale.
    #
    # if there is a frame then you get a true and the img back.
    # a gray feed is created by converting the frame to gray. 
    # it shows it and waits for a key if that key is q then break
    # and close/stop the connection to the webcam and then closes
    # the windows.
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame) #this saves the flow of images in DIVX format
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release() #releases the saving of image (closes file)
cv2.destroyAllWindows()


