import cv2

resim = cv2.imread('cicek.png')

cv2.rectangle(resim,(200,70),(320,180),(250,0,0),2)#bu kördinatlara mavi renkte 2 kalınlıkta dörtgen çizer

cv2.imshow('dörtgen',resim)



cv2.waitKey(0)
cv2.destroyAllWindows()