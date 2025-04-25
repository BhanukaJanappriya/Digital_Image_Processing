import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read the original image
img = cv2.imread(r'images/cover.jpg')
cover_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# --- 1. Crop only the painting area ---
# (Your crop is okay if your visual checking says so.)
cropped_img = img[1270:2500, 432:2022]  # [Y1:Y2, X1:X2]

# --- 2. Perform Contrast Stretching on the painting only ---
r_min = np.min(cropped_img)
r_max = np.max(cropped_img)

contrast_enhanced = ((cropped_img - r_min) * (255 / (r_max - r_min))).astype(np.uint8)
contrast_enhanced_rgb = cv2.cvtColor(contrast_enhanced, cv2.COLOR_BGR2RGB)

# --- 3. Replace the enhanced painting back into the cover ---
# Create a copy of the cover first
enhanced_cover = cover_rgb.copy()
enhanced_cover[1270:2500, 432:2022] = contrast_enhanced_rgb


plt.subplot(1,3,1)
plt.imshow(cover_rgb)
plt.title('Magazine Cover')
plt.axis('off')

# Cropped original painting
plt.subplot(1,3,2)
plt.imshow(cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB))
plt.title('Painting')
plt.axis('off')

# Magazine cover with contrast-enhanced painting
plt.subplot(1,3,3)
plt.imshow(enhanced_cover)
plt.title('Magazine cover\nwith the original painting replaced by the contrast enhanced painting', fontsize=10)
plt.axis('off')

plt.tight_layout()
plt.show()
