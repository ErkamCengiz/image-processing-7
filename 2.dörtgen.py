import cv2
import numpy as np

resim = np.zeros((400,400,3),dtype='uint8')#400 400 piksel 0 lardan oluşan matrisel şekil oluşturuyoruz
cv2.rectangle(resim,(0,0),(400,200),(0,255,255),3)

cv2.imshow('siyah',resim)


cv2.waitKey(0)
cv2.destroyAllWindows()