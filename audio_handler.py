import speech_recognition as sr
import threading

class AudioHandler:
  """
  Handles audio capture from microphone and converts speech to text.
  """

  def __init__(self, language="en-US"):
    self.recognizer = sr.Recognizer()
    self.language = language
    self.last_text = ""
    self.running = False

  def start_listening(self):
    """
    Start listening in a separate thread to avoid blocking the main program.
    """
    self.running = True
    thread = threading.Thread(target=self._listen_loop, daemon=True)
    thread.start()

  def _listen_loop(self):
    """
    Continuous listening loop.
    """
    with sr.Microphone() as source:
      self.recognizer.adjust_for_ambient_noise(source)
      self.recognizer.pause_threshold = 0.8
      while self.running:
        try:
          print("Listening...")
          audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
          text = self.recognizer.recognize_google(audio, language=self.language)
          self.last_text = text
          print(f"Detected Speech: {text}")
        except sr.WaitTimeoutError:
          continue
        except sr.UnknownValueError:
          continue
        except sr.RequestError as e:
          print(f"API error: {e}")


  def stop_listening(self):
    self.running = False

  def get_last_text(self):
    """
    Returns the last detected text.
    """
    return self.last_text
