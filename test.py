#GrabCut algoritm
import numpy as np
#import matplotlib.pyplot as plt
import cv2


filename = "grabCut_test.png"
im = cv2.imread(filename)

h,w = im.shape[:2]

mask = np.zeros((h,w),dtype='uint8')
rect = cv2.selectROI(im)
tmp1 = np.zeros((1, 13 * 5))
tmp2 = np.zeros((1, 13 * 5))

cv2.grabCut(im,mask,rect,tmp1,tmp2,10,mode=cv2.GC_INIT_WITH_RECT)
cv2.imshow('image', im)
cv2.imshow('mask', mask)
"""
plt.figure()
plt.imshow(mask)
plt.colorbar()
plt.show()
"""