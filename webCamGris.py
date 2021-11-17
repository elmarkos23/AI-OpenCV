import cv2 


cv2.namedWindow("laWebCam")
laWebCam = cv2.VideoCapture(0);

while True:
    next, frame = cv2.laWebCam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gauss = cv2.GaussianBlur(gray, (7,7), 1.5, 1.5)
    can = cv2.Canny(gauss, 0, 30, 3)

    cv2.imshow("laWebCam", can)
    if cv2.waitKey(50) >= 0:
        break;
