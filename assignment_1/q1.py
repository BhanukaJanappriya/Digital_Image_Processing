import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread(r'images/cover.jpg')
cover_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cropped_img = img[1270:2500, 432:2022]
cropped_rgb = cv2.cvtColor(cropped_img,cv2.COLOR_BGR2RGB)

def equalizeHistColorHSV(cropped_img):
    H, S, V = cv2.split(cv2.cvtColor(cropped_img,cv2.COLOR_BGR2HSV))
    eqV = cv2.equalizeHist(V)
    eqImg = cv2.cvtColor(cv2.merge([H, S, eqV]),cv2.COLOR_HSV2RGB)
    return eqImg

painting_enhanced = equalizeHistColorHSV(cropped_img)

enhanced_cover = cover_rgb.copy()
enhanced_cover[1270:2500, 432:2022] = painting_enhanced

plt.figure(figsize=(16, 6))

plt.subplot(1, 3, 1)
plt.imshow(cover_rgb)
plt.title('Magazine Cover')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(cropped_rgb)
plt.title('Painting')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(enhanced_cover)
plt.title('Magazine cover with the original painting \nreplaced by the contrast enhanced painting')
plt.axis('off')

plt.show()
