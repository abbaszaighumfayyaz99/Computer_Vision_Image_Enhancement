
# Step 9: Visual Comparison of Image Enhancement Methods

import cv2
import matplotlib.pyplot as plt
import os

# Create a folder for saving comparison figures
os.makedirs("results/figures", exist_ok=True)

# Process all four photographs
for i in range(1, 5):

    # Load original, degraded, and enhanced images
    original = cv2.imread(f"images/original/img_{i}.jpg")
    degraded = cv2.imread(f"images/degraded/img_{i}.png")
    stretched = cv2.imread(f"images/contrast_stretched/img_{i}.png")
    equalized = cv2.imread(f"images/histogram_equalized/img_{i}.png")
    gamma = cv2.imread(f"images/gamma_corrected/img_{i}.png")

    # Check that all five images loaded correctly
    if any(image is None for image in
           [original, degraded, stretched, equalized, gamma]):
        raise FileNotFoundError(f"Missing image for img_{i}")

    # Convert images from BGR to RGB for correct display
    original_rgb = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
    degraded_rgb = cv2.cvtColor(degraded, cv2.COLOR_BGR2RGB)
    stretched_rgb = cv2.cvtColor(stretched, cv2.COLOR_BGR2RGB)
    equalized_rgb = cv2.cvtColor(equalized, cv2.COLOR_BGR2RGB)
    gamma_rgb = cv2.cvtColor(gamma, cv2.COLOR_BGR2RGB)

    # Create one figure with five image panels
    fig, axes = plt.subplots(1, 5, figsize=(20, 5))

    # Display all five images with their method names
    images = [
        original_rgb,
        degraded_rgb,
        stretched_rgb,
        equalized_rgb,
        gamma_rgb
    ]

    titles = [
        "Original",
        "Degraded",
        "Contrast Stretching",
        "Histogram Equalization",
        "Gamma Correction"
    ]

    for j in range(5):
        axes[j].imshow(images[j])
        axes[j].set_title(titles[j])
        axes[j].axis("off")

    # Adjust layout and save the comparison figure
    plt.tight_layout()
    plt.savefig(f"results/figures/comparison_img_{i}.png", dpi=200)
    plt.close(fig)

    print(f"Comparison figure for Image {i} saved successfully.")
    
print("\nAll four comparison figures generated successfully.")
