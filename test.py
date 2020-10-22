#GrabCut algoritm
import numpy as np
#import matplotlib.pyplot as plt
import cv2


filename = "test.png"
im = cv2.imread(filename)

h,w = im.shape[:2]

mask = np.zeros((h,w),dtype='uint8')
rect = cv2.selectROI(im)
tmp1 = np.zeros((1, 13 * 5))
tmp2 = np.zeros((1, 13 * 5))

cv2.grabCut(im,mask,rect,tmp1,tmp2,10,mode=cv2.GC_INIT_WITH_RECT)
mask[mask == cv2.GC_BGD] = 0 #certain background is black
mask[mask == cv2.GC_PR_BGD] = 63 #possible background is dark grey
mask[mask == cv2.GC_FGD] = 255  #foreground is white
mask[mask == cv2.GC_PR_FGD] = 192 #possible foreground is light grey

cv2.imshow('image', im)
cv2.imshow('mask', mask)
cv2.waitKey(delay=5000)
"""
plt.figure()
plt.imshow(mask)
plt.colorbar()
plt.show()
"""