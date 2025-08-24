from audio_handler import AudioHandler
from gui_display import GuiDisplay


if __name__ == "__main__":
    BUILTIN_MIC_INDEX = 1    
    BLACKHOLE_INDEX = 0       

    mic_handler = AudioHandler(device_index=BUILTIN_MIC_INDEX, language="en-US")
    zoom_handler = AudioHandler(device_index=BLACKHOLE_INDEX, language="en-US")

    mic_handler.start_listening()
    zoom_handler.start_listening()

    gui = GuiDisplay()

    def refresh_gui():
        combined_text = ""
        if mic_handler.get_last_text():
            combined_text += f"You: {mic_handler.get_last_text()}  "
        if zoom_handler.get_last_text():
            combined_text += f"Others: {zoom_handler.get_last_text()}"
        gui.update_text(combined_text)

    try:
        gui.run(refresh_gui)
    except KeyboardInterrupt:
        mic_handler.stop_listening()
        zoom_handler.stop_listening()
        gui.close()
