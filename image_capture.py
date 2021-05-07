import numpy as np
import cv2
import time
cam = cv2.VideoCapture(0)


cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC for stop
        print("Escape hit, closing...")
        break
    #time.sleep(3)
    img_name = "pic_{}.png".format(img_counter)
       
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))

    img_counter += 1
    if img_counter == 120:
    	break
cam.release()

cv2.destroyAllWindows()
