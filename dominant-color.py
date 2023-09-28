import cv2
import numpy as np

image = cv2.imread('45848-cusat-students.jpg') # load image
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # BGR to RGB mode , bgr is opencv default
pixels = image_rgb.reshape(-1, 3) # reshape to 1-d pixal
dominant_color = np.uint8(np.mean(pixels, axis=0)) # dominant color
print("Dominant Color (RGB):", dominant_color)

# display color swatch
dominant_color_swatch = np.full((100, 100, 3), dominant_color, dtype=np.uint8)
cv2.imshow('Dominant Color', dominant_color_swatch)
cv2.waitKey(10000) # 10000 millisecs n close
cv2.destroyAllWindows()

## todo - make module

