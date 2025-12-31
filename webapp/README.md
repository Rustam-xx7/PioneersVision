# PioneersVision Next.js Web Application

This is a Next.js full-stack application for the PioneersVision ASL gesture recognition system.

## Features

- **Modern React Frontend**: Built with Next.js 14 and TypeScript
- **API Routes Backend**: Server-side API routes handle Python subprocess management
- **Real-time Status**: Auto-refresh status checks every 3 seconds
- **Process Management**: Starts/stops the live_gesture_text.py script in the virtual environment

## Getting Started

### 1. Install Dependencies

```bash
cd webapp
npm install
```

### 2. Run the Development Server

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### 3. Production Build

```bash
npm run build
npm start
```

## How It Works

### Backend API (`/api/recognition`)

- **POST /api/recognition** - Start/stop the recognition process
  - `{ "action": "start" }` - Starts live_gesture_text.py
  - `{ "action": "stop" }` - Stops the process
  
- **GET /api/recognition** - Check if recognition is running

### Frontend

- React components with hooks for state management
- Automatic status polling
- Real-time log display
- Responsive UI with modern design

## Project Structure

```
webapp/
├── src/
│   └── app/
│       ├── api/
│       │   └── recognition/
│       │       └── route.ts       # API endpoint
│       ├── layout.tsx             # Root layout
│       ├── page.tsx               # Main page component
│       ├── page.module.css        # Component styles
│       └── globals.css            # Global styles
├── package.json
├── tsconfig.json
└── next.config.js
```

## Requirements

- Node.js 18+ 
- Python 3.11+ with virtual environment (../.venv or ../venv)
- All Python dependencies installed in the virtual environment

## Notes

- The Next.js app looks for the Python virtual environment in the parent directory
- The live_gesture_text.py script runs as a subprocess with inherited stdio
- Process lifecycle is managed by the API route
