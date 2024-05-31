import cv2

cap = cv2.VideoCapture("nvarguscamerasrc \
    !video/x-raw(memory:NVMM), width=640, height=480, format=NV12, framerate=30/1\
    !nvvidconv flip-method=0 ! videoconvert ! video/x-raw, format=BGR ! appsink")

while True:
    sucess, img = cap.read()
    cv2.imshow("capture", img)
    k = cv2.waitKey(1)
    if k == 27:
        cv2.destroyAllWindows()
        break
    elif k == ord("s"):
        cv2.imwrite("video.jpg", img)
        cv2.destroyAllWindows()
        break
cap.release()
