# Computer Vision — Homework 1: Image Enhancement

**University:** University of Verona  
**Course:** Computer Vision (2026/2027)  
**Student:** Abbas Zaighum Fayyaz
**Matricola:** VR555433

## 1. Introduction

The aim of this assignment is to compare different image enhancement techniques and understand how they affect photographs with low contrast, shadows, and uneven lighting.

I selected four photographs taken during my visit to Venice, Italy. To make the comparison consistent, I first reduced the contrast of each image and added a small amount of Gaussian noise.

I then tested three image enhancement methods:

1. Linear contrast stretching
2. Histogram equalization
3. Gamma correction

The degraded images without enhancement were also included as a baseline.

Finally, I compared the results with the original photographs using MSE, PSNR, and side-by-side visual comparisons.

## 2. Images Used

The experiment uses four color photographs taken by me in Venice.

| Image | Description |
|---|---|
| `img_1.jpg` | Gondolas near the waterfront, with a cloudy sky and dark foreground |
| `img_2.jpg` | A church interior with uneven lighting and darker architectural details |
| `img_3.jpg` | A view of the Grand Canal under cloudy conditions |
| `img_4.jpg` | A narrow canal with sunlight and shadows between buildings |

The images are stored in `images/original/`.

**Source:** Personal photographs taken in Venice, Italy.  
**Copyright:** Retained by the author.  
**License:** The source code is released under the MIT license (see `LICENSE`). The photographs are not covered by it.
**Usage:** The photographs are included in this repository for reviewing and reproducing this educational experiment. No license for reuse of the photographs is granted.

The original photographs are used as references when calculating MSE and PSNR. In real-world situations, a clean reference image may not be available.

## 3. Synthetic Image Degradation

**Script:** `degradation.py`

To create a controlled experiment, I reduced the contrast of each original photograph using:

\[
I_{low}=0.5I_{original}+0.5(128)
\]

I then added Gaussian noise.

The parameters were:

- Contrast factor: `alpha = 0.5`
- Reference intensity: `128`
- Gaussian noise mean: `0`
- Gaussian noise standard deviation: `5`
- Random seed: `42`

The same settings were used for all four photographs. A fixed random seed was used so the degradation could be reproduced.

The degraded images are saved in `images/degraded/`.

## 4. Image Enhancement Methods

### 4.1 Linear Contrast Stretching

**Script:** `enhancement.py`

Contrast stretching increases the difference between darker and brighter intensity values.

I used the 2nd and 98th percentiles to determine the stretching range. Values outside the valid range were clipped.

The operation was applied to the lightness (L) channel in the Lab color space instead of processing the three color channels separately. This helps reduce unwanted color changes, although some differences may still occur.

**Output folder:** `images/contrast_stretched/`

### 4.2 Histogram Equalization

**Script:** `histogram_equalization.py`

Histogram equalization redistributes intensity values to increase image contrast.

I converted each degraded photograph to Lab color space and used OpenCV's `equalizeHist()` function on the L channel.

This method can reveal details in some areas, but it can also make noise more visible and produce stronger contrast than desired.

**Output folder:** `images/histogram_equalized/`

### 4.3 Gamma Correction

**Script:** `gamma_correction.py`

Gamma correction changes brightness using a power-law transformation.

I normalized the Lab lightness channel, applied a fixed gamma value of `0.7`, and converted the result back to an 8-bit image.

With gamma below 1, the transformation generally increases brightness.

**Output folder:** `images/gamma_corrected/`

## 5. Evaluation

**Script:** `evaluation.py`

I evaluated the degraded baseline and three enhancement methods against the original photographs.

Two metrics were used:

- **Mean Squared Error (MSE):** Measures the average squared difference between the processed image and the original. Lower values indicate better numerical similarity.
- **Peak Signal-to-Noise Ratio (PSNR):** Measures reconstruction fidelity in decibels. Higher values indicate better numerical similarity.

The experiment contains four photographs and four comparison approaches, resulting in **16 evaluations**.

The metrics are saved in:

`results/evaluation_metrics.csv`

I also used `comparison.py` to generate four figures, each showing the original photograph, degraded image, and three enhanced results.

The figures are saved in:

`results/figures/`

## 6. Software Requirements

The experiment was developed using the following versions:

| Software | Version |
|---|---|
| Python | 3.13.5 |
| NumPy | 2.5.4 |
| OpenCV (`opencv-python`) | 5.0.0.93 |
| Matplotlib | 3.11.2 |

### Installation

Python 3.13.5 should be installed before setting up the project.

From the project folder, a virtual environment can be created using:

```bash
python3.13 -m venv .venv
```

On macOS or Linux, activate it using:

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

The project uses OpenCV, NumPy, and Matplotlib. No deep-learning libraries are required.

## 7. Running the Experiment

The complete experiment can be run with a single command from the project folder:

```bash
python main.py
```

The `main.py` script executes the following files in order:

1. `degradation.py` — Creates the degraded images.
2. `enhancement.py` — Applies contrast stretching.
3. `histogram_equalization.py` — Applies histogram equalization.
4. `gamma_correction.py` — Applies gamma correction.
5. `evaluation.py` — Calculates MSE and PSNR and saves the CSV file.
6. `comparison.py` — Generates the comparison figures.

The original images remain unchanged. The generated images, evaluation metrics, and figures are saved in their respective folders.

## 8. Project Folder Structure

```text
CV_Assignment_One/
├── main.py
├── degradation.py
├── enhancement.py
├── histogram_equalization.py
├── gamma_correction.py
├── evaluation.py
├── comparison.py
├── requirements.txt
├── README.md
├── images/
│   ├── original/
│   ├── degraded/
│   ├── contrast_stretched/
│   ├── histogram_equalized/
│   └── gamma_corrected/
└── results/
    ├── evaluation_metrics.csv
    └── figures/
        ├── comparison_img_1.png
        ├── comparison_img_2.png
        ├── comparison_img_3.png
        └── comparison_img_4.png
```

The original photographs are JPEG files, while the degraded and enhanced images are saved as PNG files.

## 9. Observations

After comparing the results, I found that **contrast stretching produced the lowest MSE and highest PSNR for all four photographs**.

For example, in Image 1, PSNR increased from 16.89 dB for the degraded baseline to 26.11 dB after contrast stretching.

Histogram equalization produced stronger contrast in several regions, but also made noise more noticeable. This was particularly visible in the sky of Image 3, where PSNR decreased from 16.69 dB for the degraded baseline to 13.35 dB after equalization.

Gamma correction generally brightened the photographs, but the results were not consistently closer to the original images. For Image 3, gamma correction slightly improved PSNR compared with the degraded baseline.

These observations show that increasing contrast or brightness does not always improve numerical image fidelity. Visual appearance and evaluation metrics both need to be considered.

## 10. Scope and Limitations

This experiment compares three classical enhancement techniques using four real photographs with different lighting conditions.

I used fixed parameters to keep the comparisons consistent. The results describe how the methods performed on these particular photographs, rather than claiming that one technique is always better for every image.

The synthetic degradation provides known original images for quantitative evaluation, but real-world images do not always have an available reference.

This assignment uses classical image-processing techniques only. No deep-learning or pretrained models were used.
