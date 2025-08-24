# Live Zoom Subtitles 🎤💬

Generate real-time, on-screen subtitles for your Zoom meetings by capturing both your microphone and the system's audio. The subtitles appear in a transparent floating window that stays on top of other applications.

---

## ✨ Features
- **Dual Audio Capture:** Simultaneously listens to your microphone and other participants' audio via a virtual audio device.
- **Real-Time Transcription:** Converts speech to text with Google Speech Recognition.
- **Always-on-Top GUI:** Displays live subtitles in a sleek, non-intrusive floating window.

---

## 🚀 Getting Started

### 1. Prerequisites
Before you begin, ensure you have the following installed:
- **Python 3.8+**
- **[BlackHole](https://existential.audio/blackhole/)** (a virtual audio driver for macOS)
- **Zoom** or any other video conferencing application for testing.

### 2. Configuration

You must configure the audio device indices in `main.py` to match your setup. The script needs to know which index corresponds to your microphone and which one is the BlackHole audio device.

The default values are:
```python
BUILTIN_MIC_INDEX = 1   # Your microphone
BLACKHOLE_INDEX = 0     # Others / Zoom audio
```

### 3. Run the Application
Once everything is configured, you can start the application:

\`\`\`bash
python main.py
\`\`\`
