import { NextResponse } from 'next/server';
import { spawn } from 'child_process';
import path from 'path';
import fs from 'fs';

// Store the active process
let activeProcess = null;

function findPythonExecutable() {
  const baseDir = path.resolve(process.cwd(), '..');
  
  const candidates = [
    path.join(baseDir, '.venv', 'Scripts', 'python.exe'),
    path.join(baseDir, 'venv', 'Scripts', 'python.exe'),
    'python',
  ];

  for (const candidate of candidates) {
    if (candidate === 'python') return candidate;
    if (fs.existsSync(candidate)) return candidate;
  }

  return 'python';
}

export async function POST(request) {
  const { action } = await request.json();

  if (action === 'start') {
    if (activeProcess && !activeProcess.killed) {
      return NextResponse.json(
        { success: false, message: 'Recognition is already running' },
        { status: 400 }
      );
    }

    const baseDir = path.resolve(process.cwd(), '..');
    const scriptPath = path.join(baseDir, 'live_gesture_text.py');

    if (!fs.existsSync(scriptPath)) {
      return NextResponse.json(
        { success: false, message: `Script not found: ${scriptPath}` },
        { status: 404 }
      );
    }

    const pythonExec = findPythonExecutable();

    try {
      activeProcess = spawn(pythonExec, [scriptPath], {
        cwd: baseDir,
        stdio: 'inherit',
      });

      activeProcess.on('exit', (code) => {
        console.log(`Process exited with code ${code}`);
        activeProcess = null;
      });

      activeProcess.on('error', (error) => {
        console.error('Process error:', error);
        activeProcess = null;
      });

      return NextResponse.json({
        success: true,
        message: `Started live_gesture_text.py using ${pythonExec}`,
      });
    } catch (error) {
      return NextResponse.json(
        { success: false, message: `Failed to start: ${error}` },
        { status: 500 }
      );
    }
  }

  if (action === 'stop') {
    if (!activeProcess || activeProcess.killed) {
      return NextResponse.json(
        { success: false, message: 'Recognition is not running' },
        { status: 400 }
      );
    }

    activeProcess.kill('SIGTERM');
    
    // Force kill after 5 seconds if not terminated
    setTimeout(() => {
      if (activeProcess && !activeProcess.killed) {
        activeProcess.kill('SIGKILL');
      }
    }, 5000);

    activeProcess = null;

    return NextResponse.json({
      success: true,
      message: 'Stopped live recognition',
    });
  }

  return NextResponse.json(
    { success: false, message: 'Invalid action' },
    { status: 400 }
  );
}

export async function GET() {
  const isRunning = activeProcess && !activeProcess.killed;
  return NextResponse.json({ isRunning });
}
