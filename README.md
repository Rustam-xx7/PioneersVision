# PioneersVision - Complete Setup & Deployment Guide

## 📋 Table of Contents
1. [Project Overview](#project-overview)
2. [Prerequisites](#prerequisites)
3. [Backend Setup (Python)](#backend-setup-python)
4. [Frontend Setup (Next.js)](#frontend-setup-nextjs)
5. [Running the Complete Application](#running-the-complete-application)
6. [Troubleshooting](#troubleshooting)
7. [Project Structure](#project-structure)

---

## 🎯 Project Overview

**PioneersVision** is a real-time **American Sign Language (ASL) Gesture Recognition** system that combines:
- **Backend:** Python-based gesture recognition using computer vision (OpenCV, MediaPipe, TensorFlow)
- **Frontend:** Next.js web application for real-time visualization and text-to-speech integration
- **Features:** Live gesture detection, translation, speech synthesis, and user preferences management

---

## ✅ Prerequisites

Before starting, ensure you have:

### System Requirements
- **Python 3.11.x** (CRITICAL: Do NOT use Python 3.12+ - TensorFlow compatibility issue)
- **Node.js 18+** (for Next.js frontend)
- **npm** or **yarn** (package manager for Node.js)
- **Webcam** (for gesture detection)
- **Windows 10/11, macOS, or Linux**
- **Visual C++ Build Tools** (Windows only - for NumPy compilation)
- **Git** (for cloning the repository)

### Verify Installations
```bash
python --version          # Should be 3.11.x
node --version           # Should be 18+
npm --version            # Should be 8+
git --version            # Verify Git is installed
```

---

## 🐍 Backend Setup (Python)

### Step 1: Clone the Repository
```bash
# Navigate to your desired location
cd your-project-directory

# Clone the repository
git clone https://github.com/your-username/PioneersVision.git
cd PioneersVision
```

### Step 2: Create Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` at the beginning of your terminal line.

### Step 3: Upgrade pip
```bash
# Ensure pip is up to date
python -m pip install --upgrade pip setuptools wheel
```

### Step 4: Install Python Dependencies

```bash
# Install all required packages
pip install -r requirements.txt
```

**If you encounter NumPy/Build issues:**
```bash
# Option 1: Install with binary packages only
pip install --only-binary :all: -r requirements.txt

# Option 2: Install packages individually
pip install numpy==1.26.4 --only-binary :all:
pip install opencv-python==4.12.0.88
pip install mediapipe==0.10.5
pip install tensorflow-intel==2.12.0
pip install scikit-learn==1.8.0
pip install joblib==1.5.3
```

### Step 5: Verify Backend Installation

```bash
# Test Python imports
python -c "import cv2; import mediapipe; import tensorflow; print('✓ All imports successful')"
```

---

## 🌐 Frontend Setup (Next.js)

### Step 1: Navigate to webapp Directory
```bash
cd webapp
```

### Step 2: Install Node Dependencies
```bash
# Using npm (recommended)
npm install

# OR using yarn
yarn install
```

### Step 3: Configure Environment Variables

Create a `.env.local` file in the `webapp/` directory:
```bash
# webapp/.env.local
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_WS_URL=ws://localhost:8000/ws
```

### Step 4: Build the Frontend (Optional)
```bash 
# For production build
npm run build

# For development, skip this - it runs in dev mode
```

---

## 🚀 Running the Complete Application

### Terminal 1: Backend (Python ASL Recognition)

```powershell
# Navigate to project root
cd PioneersVision

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Run the backend gesture recognition
python live_gesture_text.py
```

**Expected Output:**
```
Loading model from: .../model/asl_model.pkl
👉 Press ESC to exit
[INFO] Model loaded successfully
[INFO] Camera initialized
```

### Terminal 2: Frontend (Next.js Web Interface)

```powershell
# Navigate to webapp directory
cd webapp

# Run development server
npm run dev
```

**Expected Output:**
```
> dev
> next dev

  ▲ Next.js 14.2.18
  - Local:        http://localhost:3000
  - Environments: .env.local
```

### Step 3: Access the Application

1. **Open your browser** and navigate to:
   ```
   http://localhost:3000
   ```

2. **Grant webcam permissions** when prompted

3. **Perform ASL gestures** in front of your webcam

4. **View recognized text** on the web page

5. **Listen to speech synthesis** of recognized text

---

## ⚙️ Configuration & Settings

### User Preferences (`user_preferences.json`)
Customize your experience by editing this file:
```json
{
  "language": "en",
  "speech_enabled": true,
  "gesture_confidence": 0.7,
  "auto_clear_text": false,
  "text_history_limit": 50
}
```

### Speech Settings
- Modify `func_root/speech/preferences.py` for voice, speed, and language options
- Choose between Azure Cognitive Services or offline TTS

### Model Settings
- Gesture confidence threshold: Adjust in `live_gesture_text.py` (line ~26)
- Default: `min_detection_confidence=0.6`

---

## 🔧 Troubleshooting

### 1. **Python Version Mismatch**
```
Error: tensorflow-intel requires Python 3.9, 3.10, or 3.11
```
**Solution:** Use Python 3.11.x
```bash
python --version  # Check your version
# If not 3.11, install Python 3.11 and update your PATH
```

### 2. **NumPy Compatibility Issues**
```
Error: numpy 2.x breaks TensorFlow
```
**Solution:** Downgrade NumPy to 1.26.4
```bash
pip uninstall numpy -y
pip install numpy==1.26.4 --only-binary :all:
```

### 3. **Webcam Not Detected**
```
Error: Cannot open camera (cv2.VideoCapture returns None)
```
**Solution:**
- Check if another application is using the webcam
- Try camera index `1` or `2` in `live_gesture_text.py` (line ~40)
- Restart VS Code/Terminal with admin privileges
- Check Windows Settings > Privacy > Camera permissions

### 4. **Node.js/npm Not Found**
```
Error: 'npm' is not recognized
```
**Solution:**
- Download and install Node.js from https://nodejs.org/
- Restart your terminal
- Verify: `node --version`

### 5. **Port 3000 Already in Use**
```
Error: Port 3000 is already in use
```
**Solution:**
```bash
# Use a different port
npm run dev -- -p 3001
# Then access: http://localhost:3001
```

### 6. **Module Import Errors**
```
Error: No module named 'mediapipe' / 'tensorflow'
```
**Solution:**
```bash
# Ensure virtual environment is activated
# Windows:
.\venv\Scripts\Activate.ps1
# Then reinstall:
pip install -r requirements.txt
```

### 7. **Permission Denied (Linux/macOS)**
```
Permission denied: ./venv/bin/activate
```
**Solution:**
```bash
chmod +x venv/bin/activate
source venv/bin/activate
```

---

## 📦 Dependencies & Versions

### Critical Versions (Verified Dec 27, 2025)

**Python Backend:**
- Python: **3.11.9**
- TensorFlow: **2.12.0** (tensorflow-intel for Windows)
- MediaPipe: **0.10.5**
- NumPy: **1.26.4** (CRITICAL: 1.25.0 ≤ version < 2.0)
- OpenCV: **4.12.0.88**
- scikit-learn: **1.8.0**
- joblib: **1.5.3**

**Frontend:**
- Node.js: **18+**
- Next.js: **14.2.18**
- React: **18.3.1**
- TailwindCSS: **3.4.1**

---

## 📁 Project Structure
```
PioneersVision/
├── 📄 live_gesture_text.py      # Main gesture recognition app (RUN THIS)
├── 📄 main.py                    # Flask/FastAPI backend (optional)
├── 📄 training.py                # Model training script
├── 📄 testing.py                 # Testing utilities
├── 📄 requirements.txt            # Python dependencies
├── 📄 SETUP.md                    # This file
├── 📄 README.md                   # Project overview
├── 📄 user_preferences.json       # User settings
├── 📁 func_root/                  # Backend modules
│   ├── 📁 speech/                 # Text-to-speech engine
│   ├── 📁 translation/            # Language translation
│   ├── 📁 utils/                  # Utilities (logging, validation)
│   └── 📁 tests/                  # Unit tests
├── 📁 model/                      # ML models (large files)
│   └── asl_model.pkl              # Trained gesture recognition model
└── 📁 webapp/                     # Next.js frontend
    ├── package.json               # Node.js dependencies
    ├── next.config.js             # Next.js configuration
    ├── 📁 src/
    │   └── 📁 app/
    │       ├── page.js            # Home page
    │       ├── layout.js          # App layout
    │       └── 📁 api/            # API routes
    └── 📁 public/                 # Static assets
```

---

## 🎓 Quick Commands Reference

```bash
# Virtual environment
python -m venv venv                    # Create venv
.\venv\Scripts\Activate.ps1            # Activate (Windows)
source venv/bin/activate               # Activate (macOS/Linux)
deactivate                             # Deactivate venv

# Backend
python live_gesture_text.py            # Run main app
python training.py                     # Train new model
python testing.py                      # Run tests
python -m pytest func_root/tests/      # Run unit tests

# Frontend
npm install                            # Install dependencies
npm run dev                            # Start dev server
npm run build                          # Build for production
npm run start                          # Start production server
npm run lint                           # Run ESLint

# Git (after cloning)
git status                             # Check changes
git add .                              # Stage changes
git commit -m "message"                # Commit
git push origin main                   # Push to GitHub
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:
```bash
# .env
FLASK_ENV=development
DEBUG=True
MODEL_PATH=./model/asl_model.pkl
LOG_LEVEL=INFO

# For Azure Speech Services (optional)
AZURE_SPEECH_KEY=your-api-key
AZURE_SPEECH_REGION=eastus
```

---

## 📝 Common Issues Checklist

- [ ] Python version is 3.11.x
- [ ] Virtual environment is created and activated
- [ ] pip is upgraded: `python -m pip install --upgrade pip`
- [ ] requirements.txt installed successfully
- [ ] No port conflicts (3000, 8000)
- [ ] Webcam permissions granted
- [ ] Node.js and npm are installed
- [ ] webapp/.env.local is created with correct URLs

---

## 🆘 Still Having Issues?

1. **Check logs** in terminal output
2. **Run in debug mode** - See console output for errors
3. **Recreate virtual environment**:
   ```bash
   rmdir /s venv  # Windows
   rm -rf venv    # macOS/Linux
   python -m venv venv
   pip install -r requirements.txt
   ```
4. **Clear npm cache** (if frontend issues):
   ```bash
   npm cache clean --force
   rm -rf node_modules package-lock.json
   npm install
   ```
5. **Check GitHub Issues** - Search for your error message
6. **Review logs** in `logs/` directory if they exist

---

## 📚 Additional Resources

- [MediaPipe Documentation](https://developers.google.com/mediapipe)
- [TensorFlow Setup Guide](https://www.tensorflow.org/install)
- [Next.js Documentation](https://nextjs.org/docs)
- [OpenCV Tutorials](https://docs.opencv.org/master/d9/df8/tutorial_root.html)

---

## ✨ Next Steps After Setup

1. ✅ Complete backend & frontend setup (this guide)
2. Train/load gesture model
3. Customize user preferences
4. Set up Azure Speech Services (optional)
5. Deploy to production

---

**Last Updated:** December 31, 2025
**Status:** Ready for Production
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
