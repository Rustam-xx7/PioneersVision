import { NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';

export async function GET() {
  try {
    const baseDir = path.resolve(process.cwd(), '..');
    const filePath = path.join(baseDir, 'recognized_text.txt');

    if (!fs.existsSync(filePath)) {
      return NextResponse.json(
        { text: '', message: 'No recognized text yet' }
      );
    }

    const text = fs.readFileSync(filePath, 'utf-8');
    return NextResponse.json({ text });
  } catch (error) {
    return NextResponse.json(
      { error: error.message },
      { status: 500 }
    );
  }
}
