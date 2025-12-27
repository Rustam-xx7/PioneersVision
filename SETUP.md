# PioneersVision - ASL Gesture Recognition Setup Guide

## Project Overview
Real-time American Sign Language (ASL) gesture recognition using computer vision and machine learning.

## Prerequisites
- **Python 3.11.x** (Required - do not use Python 3.12+ due to TensorFlow compatibility)
- Webcam
- Windows OS (or Linux/Mac with appropriate TensorFlow package)

## Quick Start

### 1. Clone/Download the Project
```bash
cd d:\CODING\PioneersVision
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
.\venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Note:** If you encounter NumPy build issues, you may need to:
- Use Python 3.11 (not 3.12+)
- Install Visual C++ Build Tools for Windows
- Or install packages individually with `--only-binary :all:` flag

### 5. Run the Application
```bash
python live_gesture_text.py
```

## Current Working Versions (Verified Dec 27, 2025)
- Python: 3.11.9
- opencv-python: 4.12.0.88
- mediapipe: 0.10.5
- numpy: 1.26.4 (CRITICAL: Must be >=1.25.0 and <2.0)
- tensorflow-intel: 2.12.0 (Windows)
- scikit-learn: 1.8.0
- joblib: 1.5.3

## Key Compatibility Notes

### NumPy Version is CRITICAL
The project requires NumPy 1.26.x because:
- ✅ NumPy >=1.25.0: Required for `numpy.exceptions` module
- ✅ NumPy <2.0: Required for TensorFlow 2.12.0 and MediaPipe 0.10.5 compatibility
- ❌ NumPy 1.23.x: Missing `numpy.exceptions` module
- ❌ NumPy 2.x: Breaks TensorFlow and MediaPipe

### TensorFlow
- Windows: Uses `tensorflow-intel` package
- Linux/Mac: Uses `tensorflow` package
- Version 2.12.0 is the sweet spot for Python 3.11

## Usage

1. **Run the application:**
   ```bash
   python live_gesture_text.py
   ```

2. **Camera window will open** showing live feed

3. **Make ASL gestures** with your hand in front of the camera

4. **Recognized text** will appear on screen and save to `recognized_text.txt`

5. **Press ESC** to exit

## Project Structure
```
PioneersVision/
├── live_gesture_text.py    # Main application
├── training.py             # Model training script
├── testing.py              # Testing utilities
├── requirements.txt        # Python dependencies
├── SETUP.md               # This file
├── README.md              # Project description
└── model/
    └── asl_model.pkl      # Trained ML model
```

## Troubleshooting

### "ModuleNotFoundError: No module named 'numpy.exceptions'"
- **Solution:** Upgrade NumPy to 1.25.0 or higher: `pip install "numpy>=1.26.0,<2.0"`

### "_ARRAY_API not found" or NumPy 2.x compatibility errors
- **Solution:** Downgrade NumPy to 1.26.x: `pip install "numpy>=1.26.0,<2.0"`

### Camera not opening
- Check if webcam is connected and not in use by another application
- Verify camera permissions in Windows settings

### "Can't open file" errors
- Make sure you're in the correct directory: `cd d:\CODING\PioneersVision`
- Use full path when running: `python d:\CODING\PioneersVision\live_gesture_text.py`

## Development

### Training New Models
```bash
python training.py
```

### Testing
```bash
python testing.py
```

## License
MIT

## Contributors
PioneersVision Team

---
Last Updated: December 27, 2025
