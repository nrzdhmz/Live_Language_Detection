import tkinter as tk


class GuiDisplay:
    def __init__(self, width=800, height=100):
        self.root = tk.Tk()
        self.root.title("Live Zoom Subtitles")
        self.root.attributes("-topmost", True)
        self.root.geometry(f"{width}x{height}+100+50")
        self.root.configure(bg='black')
        self.root.overrideredirect(True)
        self.root.wm_attributes('-alpha', 0.8)

        self.label = tk.Label(
            self.root,
            text="",
            font=("Helvetica", 24),
            fg="white",
            bg="black",
            wraplength=width-20,
            justify="center"
        )
        self.label.pack(expand=True, fill='both', padx=10, pady=10)

    def update_text(self, text):
        if self.label['text'] != text:
            self.label.config(text=text)

    def run(self, update_callback, refresh_rate=200):
        def gui_loop():
            update_callback()
            self.root.after(refresh_rate, gui_loop)
        gui_loop()
        self.root.mainloop()

    def close(self):
        self.root.destroy()
