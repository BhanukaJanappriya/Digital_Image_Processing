import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread(r'images/breast_digital_Xray.tif',0)

transformed_image = np.where(img<128,img,255)

transformed_image = np.array(transformed_image,dtype=np.uint8)

plt.subplot(1,2,1)
plt.title('Original image')
plt.axis('off')
plt.imshow(img,cmap='gray')

plt.subplot(1,2,2)
plt.title('Transformed Image')
plt.axis('off')
plt.imshow(transformed_image,cmap='gray')

plt.show()