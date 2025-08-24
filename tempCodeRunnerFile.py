from audio_handler import AudioHandler
import time

audio = AudioHandler(language="en-US")
audio.start_listening()

try:
    while True:
        last_text = audio.get_last_text()
        if last_text:
            print("Latest detected text:", last_text)
        time.sleep(1)
except KeyboardInterrupt:
    audio.stop_listening()
    print("Stopped listening.")
