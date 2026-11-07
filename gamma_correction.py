# Gamma Correction

import cv2
import numpy as np

# Fixed gamma parameter for all images
gamma = 0.7

# Process all four degraded photographs
for i in range(1, 5):
    image = cv2.imread(f"images/degraded/img_{i}.png")
    if image is None:
        print(f"Error: Image img_{i}.png not found.")
    else:
        print(f"Image img_{i}.png loaded successfully.")

        # Convert the image from BGR to Lab color space
        lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        
        # Extract the L (lightness) channel
        L = lab_image[:, :, 0]

        # Convert to float32 and normalize pixel values to [0, 1]
        L_float = L.astype(np.float32)
        L_normalized = L_float / 255.0

        # Apply gamma correction using the power-law transformation
        L_gamma = 255.0 * np.power(L_normalized, gamma)

        # Clip the corrected values and convert to uint8
        L_clipped = np.clip(L_gamma, 0, 255)
        L_uint8 = L_clipped.astype(np.uint8)

        # Replace the lightness channel and convert back to BGR
        enhanced_lab = lab_image.copy()
        enhanced_lab[:, :, 0] = L_uint8
        enhanced_bgr = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)
        
        # Save the gamma-corrected image
        saved_image = cv2.imwrite(f'images/gamma_corrected/img_{i}.png',enhanced_bgr)
        print(f"img_{i} saved successfully: {saved_image}")

        # *************************** Verification results *************************************

        #print("Normalized min:", L_normalized.min())
        #print("Normalized max:", L_normalized.max())
        #print("Data type:", L_normalized.dtype)
        #print("Gamma min:", L_gamma.min())
        #print("Gamma max:", L_gamma.max())
        #print("Gamma data type:", L_gamma.dtype)
        #print("Final L minimum:", L_uint8.min())
        #print("Final L maximum:", L_uint8.max())
        #print("Final L data type:", L_uint8.dtype)
        #rint("Enhanced Lab shape:", enhanced_lab.shape)
        #print("Enhanced Lab dtype:", enhanced_lab.dtype)
        #print("Enhanced BGR shape:", enhanced_bgr.shape)
        #print("Enhanced BGR dtype:", enhanced_bgr.dtype)
        
        
