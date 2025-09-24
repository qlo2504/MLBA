import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator

class TextTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Translator")
        self.root.resizable(False, False)
        self.create_widgets()   # ❌ bỏ self.translator = Translator()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="20 20 20 20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(main_frame, text="Enter text to translate:").grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        self.input_text = ttk.Entry(main_frame, width=60)
        self.input_text.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))

        ttk.Label(main_frame, text="Choose source language:").grid(row=2, column=0, sticky=tk.W, pady=(0, 5))
        self.source_lang = ttk.Combobox(main_frame, width=20)
        self.source_lang['values'] = ['en', 'vi', 'fr', 'de', 'es', 'zh-cn', 'ja', 'ko', 'ru']
        self.source_lang.current(0)
        self.source_lang.grid(row=2, column=1, sticky=tk.E, pady=(0, 5))

        ttk.Label(main_frame, text="Choose target language:").grid(row=3, column=0, sticky=tk.W, pady=(0, 5))
        self.target_lang = ttk.Combobox(main_frame, width=20)
        self.target_lang['values'] = ['en', 'vi', 'fr', 'de', 'es', 'zh-cn', 'ja', 'ko', 'ru']
        self.target_lang.current(1)
        self.target_lang.grid(row=3, column=1, sticky=tk.E, pady=(0, 5))

        translate_button_frame = ttk.Frame(main_frame)
        translate_button_frame.grid(row=4, column=0, columnspan=2, pady=10)

        self.translate_button = ttk.Button(
            translate_button_frame, text="Translate", command=self.translate_text
        )
        self.translate_button.pack()

        self.result_text = ttk.Label(main_frame, text="", wraplength=400)
        self.result_text.grid(row=5, column=0, columnspan=2, pady=10)

    def translate_text(self):
        try:
            text = self.input_text.get()
            src = self.source_lang.get()
            dest = self.target_lang.get()

            if text:
                translation = GoogleTranslator(source=src, target=dest).translate(text)
                self.result_text.config(text=translation)
            else:
                self.result_text.config(text="Please enter text to translate")
        except Exception as e:
            self.result_text.config(text=f"Error: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = TextTranslatorApp(root)
    root.mainloop()
