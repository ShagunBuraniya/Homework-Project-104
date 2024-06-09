import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,  
           "sun",
           (20, 300),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )

cv2.imshow("output",img)

cv2.imwrite("solarsystemwithname.jpg",img)

cv2.waitKey(0)