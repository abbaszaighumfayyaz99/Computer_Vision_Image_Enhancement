
# Main Program: Complete Image Enhancement Pipeline

import subprocess
import sys

# Run all image processing stages in the correct order
scripts = [
    "degradation.py",
    "enhancement.py",
    "histogram_equalization.py",
    "gamma_correction.py",
    "evaluation.py",
    "comparison.py"
]

# Execute each script one by one
for script in scripts:
    print(f"\nRunning {script}...", flush=True)
    subprocess.run([sys.executable, script], check=True)

print("\nAll image processing and evaluation stages completed successfully.")
