import cv2

img = cv2.imread('PRO-C116-project-image-main-main\solar-system.jpg')
cv2.imshow('output',img)
cv2.waitKey(0)

cv2.putText(img,'Sun',(90,100),cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,255),4)
cv2.putText(img,'Mercury',(100,250),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2)
cv2.putText(img,'Venus',(200,190),cv2.FONT_HERSHEY_SIMPLEX,0.6 ,(255,255,255),2)
cv2.putText(img,'Earth',(300,270),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2)
cv2.putText(img,'Mars',(370,180),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2)
cv2.putText(img,'Jupiter',(430,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)
cv2.putText(img,'Saturn',(700,130),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)
cv2.putText(img,'Uranus',(900,150),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)
cv2.putText(img,'Neptune',(1140,150),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)


cv2.imwrite('Solar_systemwithname.jpg',img)