import cv2
path = "D:\\open cv\\Picture2.png"
img =cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
cv2.imshow("Img Blur",imgBlur)
cv2.waitKey(0)
