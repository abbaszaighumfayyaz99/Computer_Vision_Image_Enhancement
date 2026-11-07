
# Image Evaluation using MSE and PSNR

import cv2
import numpy as np
import csv
import os

# Define the four methods and their image folders
method_names = [
    "Degraded Baseline",
    "Contrast Stretching",
    "Histogram Equalization",
    "Gamma Correction"
]

method_folders = [
    "images/degraded",
    "images/contrast_stretched",
    "images/histogram_equalized",
    "images/gamma_corrected"
]

# Store all evaluation results
results = []

# Evaluate all four original photographs
for i in range(1, 5):

    # Load the original reference image
    original = cv2.imread(f"images/original/img_{i}.jpg")

    if original is None:
        print(f"Error: Original image img_{i}.jpg not found.")
        raise FileNotFoundError(f"Missing original image {i}")

    print(f"\nEvaluation for Image {i}")

    # Compare each method with the same original image
    for j in range(4):

        processed = cv2.imread(f"{method_folders[j]}/img_{i}.png")

        if processed is None:
            raise FileNotFoundError(f"Missing image in {method_folders[j]}")

        # Check that original and processed images have the same shape
        if original.shape != processed.shape:
            raise ValueError(f"Image {i}: dimensions do not match.")

        # Convert images to float32 for correct subtraction
        original_float = original.astype(np.float32)
        processed_float = processed.astype(np.float32)

        # Calculate Mean Squared Error (MSE)
        difference = original_float - processed_float
        squared_difference = difference ** 2
        mse = np.mean(squared_difference)

        # Calculate Peak Signal-to-Noise Ratio (PSNR)
        if mse == 0:
            psnr = float("inf")
        else:
            psnr = 10 * np.log10((255 ** 2) / mse)

        # Display the evaluation results
        print(f"{method_names[j]}: MSE = {mse:.4f}, PSNR = {psnr:.4f} dB")

        # Store results for the CSV file
        results.append([f"img_{i}", method_names[j], float(mse), float(psnr)])

# Create the results folder and save metrics to CSV
os.makedirs("results", exist_ok=True)

with open("results/evaluation_metrics.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Image", "Method", "MSE", "PSNR_dB"])
    writer.writerows(results)

print("\nEvaluation completed successfully.")
print("Total comparisons:", len(results))
print("Metrics saved to: results/evaluation_metrics.csv")
