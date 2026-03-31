# Identifying Friend Or Foe - Face Detection System

## Overview

This project implements a face detection system using Python and OpenCV. It simulates an automated sentry gun capable of distinguishing between humans and potential threats based on visual input.

The system processes a sequence of images, detects faces, and validates detections using eye recognition to reduce false positives. Based on the result, it decides whether to trigger or disable the firing mechanism.

## Objectives

- Detect human faces in images using classical computer vision techniques
- Reduce false positives by verifying the presence of eyes
- Simulate a decision-making system based on visual input
- Provide audio feedback corresponding to system decisions

## Technologies

- Python 3

## Project Structure

Put at the end

## Installation

1. Clone the repository:

   git clone https://github.com/titou4n/IdentifyingFriendOrFoe.git
   cd sentry-gun

2. Install dependencies:

   run "check_requirement.txt"

3. On Windows, if pyttsx3 raises errors:

   pip install pypiwin32

## Usage

Run the main script:

   python sentry.py

Ensure that:
- The Haar cascade files are correctly installed with OpenCV
- The image folder is accessible
- Audio files are present in the root directory

## Methodology

### Face Detection

The system uses OpenCV's Haar Cascade Classifier:

- haarcascade_frontalface_default.xml

A sliding window scans the image at multiple scales to detect facial patterns.

### Eye Detection

To improve reliability, detected face regions are further analyzed using:

- haarcascade_eye.xml

The presence of at least one eye confirms a valid human detection.

### Decision Logic

- If a face with eyes is detected: the system disables the weapon
- Otherwise: the system triggers the firing mechanism

## Limitations

- Sensitive to face orientation and lighting conditions
- Limited robustness compared to deep learning approaches
- Possible false positives in complex backgrounds

## Possible Improvements

- Real-time video processing
- Integration of deep learning-based detectors (e.g., CNNs)
- Improved filtering and tracking mechanisms
- Multi-object classification (e.g., animals, masks, occlusions)

## Academic Context

This project was developed as part of an academic assignment in computer science at EPITA. It illustrates fundamental concepts in computer vision, including feature extraction, classification, and real-time decision systems.

## License

This project is intended for educational purposes only.