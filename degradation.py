#libraries
import cv2
import numpy as np


#Code to load images
rng = np.random.default_rng(42)

for i in range(1,5):
    image = cv2.imread(f'images/original/img_{i}.jpg')
    if image is None:
        print(f"Error: img_{i} not found.")
    else:
        print(f"img_{i} loaded successfully.")
        #print(image.shape)
        image_float = image.astype(np.float32)
        #print(image_float.dtype)
        
        alpha = 0.5
        low_contrast = alpha * image_float + (1 - alpha) * 128
        print(low_contrast.min(), low_contrast.max())
        
        #print("Original average:", image_float.mean())
        #print("Degraded average:", low_contrast.mean())

        noise = rng.normal(loc=0, scale=5, size=low_contrast.shape)
        noisy_image = low_contrast + noise
        clipped_image = np.clip(noisy_image, 0, 255)
        degraded_image = clipped_image.astype(np.uint8)
        saved_image = cv2.imwrite(f'images/degraded/img_{i}.png', degraded_image)
        
        #print("Noisy image shape:", noisy_image.shape)
        #print("Noisy image min:", noisy_image.min())
        #print("Noisy image max:", noisy_image.max())
        
        print("Data type:", degraded_image.dtype)
        print("Minimum:", degraded_image.min())
        print("Maximum:", degraded_image.max())
        print(f"img_{i} saved successfully: {saved_image}")
