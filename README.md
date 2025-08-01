# 👋 OpenCV Hand Tracking

**Author:** Supakrit Kongkham
**Student ID:** 650610858
**Faculty of Engineering, Chiang Mai University**
[GitHub Repository](https://github.com/9-Fakrizz/HandTracking_OpenCV.git)

---

## 🧠 Project Overview

This project uses **OpenCV** and **2D vector mathematics** to detect and count raised fingers from a single hand in real time using webcam input.

The program identifies whether each finger is raised or folded and displays the total number of raised fingers.

---

## ✨ Features

* ✅ Detects which specific fingers are raised
* ✅ Counts the number of raised fingers
* ✅ Works with **one hand** at a time

---

## ⚠️ Limitations

* ❌ Only supports **one hand** at a time
* ❌ Cannot detect sideways (edge-on) hands — fingers aligned in depth are not visible
* ❌ Fingers pointing directly at the camera (along z-axis) are not detected accurately

---

## 🧩 Detection Logic

The detection is based on comparing distances between finger landmarks using simple 2D vector comparisons.

### 👍 Thumb Detection

We compare two distances:

* **t1**: Distance from thumb tip `(landmark 4)` to pinky base `(landmark 17)`
* **t0**: Distance from thumb middle joint `(landmark 3)` to pinky base `(landmark 17)`

**Logic:**

* If `t1 < t0`: thumb is folded
* If `t1 > t0`: thumb is extended

### ✋ Other Fingers (Index to Pinky)

We repeat the following for each finger:

* **1**: Distance from fingertip `(8, 12, 16, 20)` to wrist `(landmark 0)`
* **0**: Distance from middle joint `(6, 10, 14, 18)` to wrist `(landmark 0)`

**Logic:**

* If `1 < 0`: finger is folded
* If `1 > 0`: finger is extended

All results are stored in an array, which is displayed along with the total count of raised fingers.

---

## 🧮 Landmark Reference (MediaPipe Hands)

```
Thumb:  [1, 2, 3, 4]
Index:  [5, 6, 7, 8]
Middle: [9, 10, 11, 12]
Ring:   [13, 14, 15, 16]
Pinky:  [17, 18, 19, 20]
Palm:   [0]
```

---

## 📸 Demo

> *Insert GIF or screenshot here of the program in action.*

---

## 🛠️ Requirements

* Python 3.x
* OpenCV
* MediaPipe

Install dependencies:

```bash
pip install opencv-python mediapipe
```

---

## 🚀 Getting Started

Clone the repository and run the script:

```bash
git clone https://github.com/9-Fakrizz/HandTracking_OpenCV.git
cd HandTracking_OpenCV
python hand_tracking.py
```

---
I appreciate your interest!

