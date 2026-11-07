import cv2
import numpy as np

# Load and enhance the four degraded images
for i in range(1, 5):
    image = cv2.imread(f'images/degraded/img_{i}.png')
    if image is None:
        print(f"Error: img_{i} not found.")
    else:
        print(f"img_{i} loaded successfully.")
        print(image.shape)
        
        # Convert BGR image to Lab color space
        lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        print("Lab shape:", lab_image.shape)
        print("Lab data type:", lab_image.dtype)
        
        # Extract L (lightness) channel
        L = lab_image[:, :, 0]
        print("L shape:", L.shape)
        
        # Calculate 2nd and 98th percentiles
        p2 = np.percentile(L, 2)
        p98 = np.percentile(L, 98)

        # Convert L channel to float32
        L_float = L.astype(np.float32)
        
        # Apply contrast stretching only if the range is valid
        if p98 > p2:
            L_stretched = ((L_float - p2)/ (p98 - p2)) * 255
            L_clipped = np.clip(L_stretched, 0, 255)
            L_uint8 = L_clipped.astype(np.uint8)
        else:
            # Avoid division by zero
            # Keep the original L channel unchanged
            L_uint8 = L.astype(np.uint8)
        
        # Reconstruct the Lab image
        enhanced_lab = lab_image.copy()
        enhanced_lab[:, :, 0] = L_uint8

        # Convert Lab back to BGR
        enhanced_bgr = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)
        
        # Save enhanced image
        saved_image = cv2.imwrite(f'images/contrast_stretched/img_{i}.png', enhanced_bgr)
        
        print("P2:", p2)
        print("P98:", p98)
        print("Stretched min:", L_stretched.min())
        print("Stretched max:", L_stretched.max())
        print("Clipped min:", L_clipped.min())
        print("Clipped max:", L_clipped.max())
        print("Enhanced Lab shape:", enhanced_lab.shape)
        print("Enhanced Lab dtype:", enhanced_lab.dtype)
        print("Enhanced BGR shape:", enhanced_bgr.shape)
        print("Enhanced BGR dtype:", enhanced_bgr.dtype)
        print(f"img_{i} saved successfully: {saved_image}")


