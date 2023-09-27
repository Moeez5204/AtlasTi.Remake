import tkinter as tk
import customtkinter

def Text_Widget(self):
    self.text_widget = customtkinter.CTkTextbox(self.frame, wrap=tk.WORD)
    self.text_widget.pack(fill=tk.BOTH, expand=True)
    self.text_widget.insert("1.0", "This is a text widget.")

    self.text_widget.bind("<<Modified>>", self.update_text_content)