
import cv2

# Apply equalization to the Lab lightness channel

for i in range(1, 5):

    # Load degraded image
    image = cv2.imread(f'images/degraded/img_{i}.png')

    if image is None:
        print(f"Error: img_{i}.png not found.")
    else:
        print(f"img_{i}.png loaded successfully.")

        # Convert BGR to Lab
        lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

        # Extract L channel
        L = lab_image[:, :, 0]

        # Apply histogram equalization
        L_equalized = cv2.equalizeHist(L)

        # Create a copy and replace the L channel
        enhanced_lab = lab_image.copy()
        enhanced_lab[:, :, 0] = L_equalized

        # Convert back to BGR
        enhanced_bgr = cv2.cvtColor(enhanced_lab,cv2.COLOR_LAB2BGR)

        # Save enhanced image
        saved = cv2.imwrite(f'images/histogram_equalized/img_{i}.png',enhanced_bgr)
        print(f"img_{i} saved successfully: {saved}")
        print("Image shape:", enhanced_bgr.shape)
        print("Image dtype:", enhanced_bgr.dtype)
