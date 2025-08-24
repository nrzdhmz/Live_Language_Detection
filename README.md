# Live Zoom Subtitles 🎤💬

Real-time subtitles for Zoom by capturing:

* Your microphone input
* System audio via BlackHole

Subtitles appear in a floating GUI window, always on top.

---

## Features

* Captures audio from two sources (you + others)
* Converts speech to text with Google Speech Recognition
* Displays live subtitles in a transparent GUI

---

## How to Run

1. Clone the repo:

```bash
git clone https://github.com/nrzdhmz/Live_Zoom_Subtitles.git
cd Live_Zoom_Subtitles
```

2. Install dependencies:

```bash
pip install SpeechRecognition pyaudio
```

(On macOS, you may need `brew install portaudio` for PyAudio.)

3. Run the Application:

```bash
python main.py
```

---

## Configuration

In `main.py`:

```python
BUILTIN_MIC_INDEX = 1   # Your microphone
BLACKHOLE_INDEX = 0     # Others / Zoom audio
```

---

## Requirements

* Python 3.8+
* [BlackHole (macOS)](https://existential.audio/blackhole/)
* Zoom or any other app for testing
