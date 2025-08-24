import speech_recognition as sr
import threading


class AudioHandler:
    def __init__(self, device_index, language="en-US"):
        self.recognizer = sr.Recognizer()
        self.language = language
        self.last_text = ""
        self.running = False
        self.device_index = device_index

    def start_listening(self):
        self.running = True
        thread = threading.Thread(target=self._listen_loop, daemon=True)
        thread.start()

    def stop_listening(self):
        self.running = False

    def _listen_loop(self):
        mic = sr.Microphone(device_index=self.device_index)
        with mic as source:
            self.recognizer.adjust_for_ambient_noise(source)
            while self.running:
                try:
                    audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                    text = self.recognizer.recognize_google(audio, language=self.language)
                    self.last_text = text
                except sr.WaitTimeoutError:
                    continue
                except sr.UnknownValueError:
                    continue
                except sr.RequestError as e:
                    print(f"API error: {e}")

    def get_last_text(self):
        return self.last_text
