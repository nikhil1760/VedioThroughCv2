import cv2
cap=cv2.VideoCapture("Code Phat Gaya  A Software Engineers frustration over production bugs  BC Sutta Parody1080p.mp4")

while True:
    status,photo=cap.read()
    photo=cv2.resize(photo,(1000,1000))
    photo[0:200,0:200]=photo[100:300,400:600]
    cv2.imshow("photo",photo)
    if cv2.waitKey(1)==13:
        break
cv2.destroyAllWindows()