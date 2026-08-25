import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

# Load the patient dataset
data = pd.read_csv("Medical_AI_Analysis_Toolkit/data/patients_demo.csv")

# Display the dataset
print("Patient Dataset:")
print(data)

# Convert columns to NumPy arrays
ages = np.array(data["Age"])
heart_rates = np.array(data["Heart_Rate"])
temperatures = np.array(data["Temperature"])

# Calculate statistics
print("\nPatient Statistics:")
print("Average Age:", np.mean(ages))
print("Average Heart Rate:", np.mean(heart_rates))
print("Maximum Heart Rate:", np.max(heart_rates))
print("Minimum Heart Rate:", np.min(heart_rates))
print("Average Temperature:", np.mean(temperatures))

plt.figure(figsize=(8, 5))

plt.plot(
    data["Patient_ID"],
    data["Heart_Rate"],
    marker="o"
)

plt.title("Heart Rate of Patients")
plt.xlabel("Patient ID")
plt.ylabel("Heart Rate (BPM)")

plt.grid(True)
plt.tight_layout()

# Save the graph
plt.savefig(
    "Medical_AI_Analysis_Toolkit/outputs/heart_rate_analysis.png"
)

plt.show()
# -----------------------------
# OpenCV Image Processing
# -----------------------------

image_path = "Medical_AI_Analysis_Toolkit/images/sample.png"

image = cv2.imread(image_path)

if image is None:
    print("\nError: X-ray image could not be loaded.")
else:
    print("\nX-ray image loaded successfully.")

    # Resize
    resized = cv2.resize(image, (224, 224))

    # Convert to grayscale
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    # Gaussian Blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Canny Edge Detection
    edges = cv2.Canny(blurred, 50, 150)

    # Save processed images
    cv2.imwrite(
        "Medical_AI_Analysis_Toolkit/outputs/xray_resized.png",
        resized
    )

    cv2.imwrite(
        "Medical_AI_Analysis_Toolkit/outputs/xray_grayscale.png",
        gray
    )

    cv2.imwrite(
        "Medical_AI_Analysis_Toolkit/outputs/xray_blurred.png",
        blurred
    )

    cv2.imwrite(
        "Medical_AI_Analysis_Toolkit/outputs/xray_edges.png",
        edges
    )

    print("X-ray preprocessing completed successfully.")

    # Display results
    cv2.imshow("Original X-Ray", image)
    cv2.imshow("Grayscale X-Ray", gray)
    cv2.imshow("Canny Edges", edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # -----------------------------
# Generate Analysis Report
# -----------------------------

report_path = "Medical_AI_Analysis_Toolkit/outputs/analysis_report.txt"

with open(report_path, "w") as report:

    report.write("MEDICAL AI ANALYSIS TOOLKIT\n")
    report.write("===========================\n\n")

    report.write("PATIENT DATA ANALYSIS\n")
    report.write("---------------------\n")
    report.write(f"Number of Patients: {len(data)}\n")
    report.write(f"Average Age: {np.mean(ages):.2f}\n")
    report.write(f"Average Heart Rate: {np.mean(heart_rates):.2f} BPM\n")
    report.write(f"Maximum Heart Rate: {np.max(heart_rates)} BPM\n")
    report.write(f"Minimum Heart Rate: {np.min(heart_rates)} BPM\n")
    report.write(f"Average Temperature: {np.mean(temperatures):.2f} °C\n\n")

    report.write("IMAGE PROCESSING\n")
    report.write("----------------\n")
    report.write("Input Image: sample.png\n")
    report.write("Resize: 224 x 224\n")
    report.write("Grayscale Conversion: Applied\n")
    report.write("Gaussian Blur: Applied\n")
    report.write("Canny Edge Detection: Applied\n")

print("\nAnalysis report saved successfully.")

# -----------------------------
# Combined X-Ray Visualization
# -----------------------------

plt.figure(figsize=(12, 8))

# Original image
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original X-Ray")
plt.axis("off")

# Grayscale image
plt.subplot(2, 2, 2)
plt.imshow(gray, cmap="gray")
plt.title("Grayscale")
plt.axis("off")

# Blurred image
plt.subplot(2, 2, 3)
plt.imshow(blurred, cmap="gray")
plt.title("Gaussian Blur")
plt.axis("off")

# Edge image
plt.subplot(2, 2, 4)
plt.imshow(edges, cmap="gray")
plt.title("Canny Edges")
plt.axis("off")

plt.tight_layout()

# Save combined visualization
plt.savefig(
    "Medical_AI_Analysis_Toolkit/outputs/xray_processing_pipeline.png"
)

plt.show()

print("Combined X-ray visualization saved successfully.")