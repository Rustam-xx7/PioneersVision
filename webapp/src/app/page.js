"use client";

import { useState, useEffect } from "react";
import Image from "next/image";

import Footer from "./Footer";

export default function Home() {
  const [isRunning, setIsRunning] = useState(false);
  const [logs, setLogs] = useState([]);
  const [status, setStatus] = useState("Ready");
  const [recognizedText, setRecognizedText] = useState("");

  const addLog = (message) => {
    const timestamp = new Date().toLocaleTimeString();
    setLogs((prev) => [...prev, `[${timestamp}] ${message}`]);
  };

  const checkStatus = async () => {
    try {
      const res = await fetch("/api/recognition");
      const data = await res.json();
      setIsRunning(data.isRunning);
    } catch (error) {
      console.error("Status check failed:", error);
    }
  };

  const fetchRecognizedText = async () => {
    try {
      const res = await fetch("/api/text");
      const data = await res.json();
      setRecognizedText(data.text || "");
    } catch (error) {
      console.error("Failed to fetch text:", error);
    }
  };

  useEffect(() => {
    addLog("🚀 PioneersVision Next.js interface loaded");
    checkStatus();
    fetchRecognizedText();

    const statusInterval = setInterval(checkStatus, 3000);
    const textInterval = setInterval(fetchRecognizedText, 2000);

    return () => {
      clearInterval(statusInterval);
      clearInterval(textInterval);
    };
  }, []);

  const handleStart = async () => {
    addLog("▶️ Starting recognition...");
    setStatus("Starting...");

    try {
      const res = await fetch("/api/recognition", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ action: "start" }),
      });

      const data = await res.json();

      if (data.success) {
        setIsRunning(true);
        setStatus("🎥 Recognition Running");
        addLog("✅ " + data.message);
      } else {
        setStatus("❌ Failed to start");
        addLog("❌ " + data.message);
      }
    } catch (error) {
      setStatus("❌ Error");
      addLog("❌ Error: " + error);
    }
  };

  const handleStop = async () => {
    addLog("⏹️ Stopping recognition...");
    setStatus("Stopping...");

    try {
      const res = await fetch("/api/recognition", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ action: "stop" }),
      });

      const data = await res.json();

      if (data.success) {
        setIsRunning(false);
        setStatus("Ready");
        addLog("✅ " + data.message);
      } else {
        setStatus("❌ Failed to stop");
        addLog("❌ " + data.message);
      }
    } catch (error) {
      setStatus("❌ Error");
      addLog("❌ Error: " + error);
    }
  };

  return (
    <>
      <div className="min-h-screen p-8 px-20">
        <div className="max-w-screen mx-auto">
          <span className="text-white text-5xl font-semibold font-mono w-full  top-10 left-0 flex justify-center">
            Pioneers Vision
          </span>
          <div className="herroSection h-[100vh]  w-full flex justify-around items-center mt-0  gap-6">
            <div className="left  h-fit w-full">
              <Image
                src="/smart_glass_img1-removebg-preview.png"
                alt="Smart glass"
                width={500}
                height={480}
              />
            </div>
            <div className="right bg-black/10 mt-20 h-60 rounded-md w-full flex flex-col justify-center items-center gap-6">
              <span className="font-semibold text-2xl font-mono text-white border-b border-white/50 px-2">
                See the World. Understand Every Gesture.
              </span>
              <span className="text-white/80 text-center">
                Real-time sign language recognition powered by AI, designed for
                smart glasses.
              </span>
            </div>
          </div>
          <div className="h-fit w-full  flex justify-center my-4">
            <span className="text-white text-center font-mono">
              “Experience the Future of Communication”
            </span>
          </div>
          <div className="modelSection h-[80vh] bg-black/50 rounded-xl mb-4 flex justify-around items-center gap-4 mt-6">
            <div className="left w-full h-full p-6  flex flex-col justify-center items-center gap-6">
              <span className="font-semibold font-serif text-2xl text-white border-b border-white/50 px-2">
                Where Vision Meets Understanding.
              </span>
              <span className="font-mono w-[80%] text-white/90">
                Our system uses advanced computer vision and machine learning
                models to detect hand gestures with precision. Each movement is
                analyzed, recognized, and translated into meaningful language —
                all in real time.
              </span>
              <span className="font-mono w-[80%] text-white/90">
                The goal is simple yet powerful: to make communication
                accessible for everyone, everywhere, using intelligent wearable
                technology.
              </span>
            </div>
            <div className="right w-[40%] ">
              <Image
                src="/model-withglass2.jpg"
                alt="Model Image"
                width={300}
                height={500}
                className="rounded-xl"
              />
            </div>
          </div>
          <div className="handSection h-[60vh] bg-black/50 rounded-xl mb-4 flex justify-around items-center gap-4 mt-8">
            <div className="left w-[40%]">
              <Image
                src="/hand-gesture1-removebg-preview.png"
                alt="Hand with smart glass"
                width={400}
                height={500}
                className="rounded-xl"
              />
            </div>
            <div className="right w-full h-full flex flex-col justify-center items-center gap-4 ">
              <span className="font-semibold font-serif text-xl text-white border-b border-white/50 px-2">
                Every Gesture Has a Voice.
              </span>
              <span className="font-mono w-[80%] text-white/90">
                For millions, hands are a language. Our technology ensures that
                language is never ignored.
              </span>
              <span className="font-mono w-[80%] text-white/90">
                We imagine a world where no one is left unheard — where
                technology bridges silence and creates connection.
              </span>
            </div>
          </div>
          <div className="bg-black/30  rounded-xl shadow-2xl shadow-black/40 my-8 p-8">
            {/* Header */}
            <div className="mb-6">
              <h1 className="text-4xl font-bold text-gray-100 mb-2">
                Gesture Recognition Console
              </h1>
              <p className="text-gray-200">ASL Gesture Recognition System</p>
            </div>

            {/* Controls */}
            <div className="flex flex-wrap gap-3 items-center mb-6">
              <button
                onClick={handleStart}
                disabled={isRunning}
                className="px-6 py-3 bg-green-500 text-white font-semibold rounded-lg hover:bg-green-600 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 hover:shadow-lg active:scale-95"
              >
                ▶️ Start Recognition
              </button>
              <button
                onClick={handleStop}
                disabled={!isRunning}
                className="px-6 py-3 bg-red-500 text-white font-semibold rounded-lg hover:bg-red-600 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 hover:shadow-lg active:scale-95"
              >
                ⏹️ Stop Recognition
              </button>
              <span
                className={`px-4 py-2 rounded-lg font-semibold ${
                  isRunning
                    ? "bg-green-100 text-green-700"
                    : "bg-gray-100 text-gray-700"
                }`}
              >
                {status}
              </span>
            </div>

            {/* Main Content - Two Columns */}
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-6">
              {/* Left: Camera Window Indicator */}
              <div className="lg:col-span-2">
                <h3 className="text-lg font-semibold text-gray-400 mb-3">
                  📹 Camera Feed
                </h3>
                <div className="bg-gray-900 rounded-lg p-8 aspect-video flex items-center justify-center border-2 border-dashed border-gray-600">
                  <div className="text-center">
                    {isRunning ? (
                      <div>
                        <div className="mb-4 animate-pulse">
                          <div className="w-16 h-16 bg-red-500 rounded-full mx-auto mb-4 flex items-center justify-center">
                            <div className="w-12 h-12 bg-red-600 rounded-full"></div>
                          </div>
                        </div>
                        <p className="text-green-400 font-mono text-lg">
                          🎥 RECORDING
                        </p>
                        <p className="text-gray-400 text-sm mt-2">
                          OpenCV window is active. Make ASL gestures!
                        </p>
                      </div>
                    ) : (
                      <div>
                        <p className="text-gray-400 text-lg mb-2">
                          Camera is inactive
                        </p>
                        <p className="text-gray-500 text-sm">
                          Click "Start Recognition" to begin
                        </p>
                      </div>
                    )}
                  </div>
                </div>

                {/* Info Box */}
                <div className="mt-4 p-4 border-2 border-dashed border-gray-300 rounded-lg bg-gray-50">
                  <p className="text-gray-700 text-sm mb-1">
                    💡 <strong>Tip:</strong> OpenCV window opens separately
                  </p>
                  <p className="text-gray-600 text-sm">
                    Press ESC in the camera window to stop
                  </p>
                </div>
              </div>

              {/* Right: Recognized Text */}
              <div className="lg:col-span-1">
                <h3 className="text-lg font-semibold text-gray-100 mb-3">
                  📝 Recognized Text
                </h3>
                <div className="bg-blue-50 rounded-lg border-2 border-blue-200 p-4 h-72 overflow-y-auto">
                  {recognizedText.trim() ? (
                    <div className="space-y-2">
                      <p className="text-gray-700 text-lg leading-relaxed break-words">
                        {recognizedText}
                      </p>
                    </div>
                  ) : (
                    <p className="text-gray-400 italic text-center py-12">
                      No recognized text yet...
                    </p>
                  )}
                </div>
                <p className="text-xs text-gray-400 mt-2">
                  ✓ Updates every 2 seconds
                </p>
              </div>
            </div>

            {/* System Log */}
            <div>
              <h3 className="text-lg font-semibold text-gray-200 mb-3">
                🔧 System Log
              </h3>
              <div className="bg-slate-900 text-green-400 p-4 rounded-lg max-h-64 overflow-y-auto font-mono text-sm">
                {logs.length === 0 && (
                  <div className="text-gray-500">No logs yet...</div>
                )}
                {logs.map((log, i) => (
                  <div key={i} className="mb-1">
                    {log}
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
      <Footer />
    </>
  );
}
