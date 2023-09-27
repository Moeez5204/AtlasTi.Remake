import tkinter as tk
import customtkinter,re
from collections import Counter

import Graphs,Menu_Buttons,Sidebar_Frame
import Text_Widget,main




class TkinterMatplotlibApp:
    def __init__(self, root):



        #Root
        customtkinter.set_appearance_mode("dark")
        self.root = root
        self.root.title("Tkinter with Matplotlib")
        self.text_content = ""
        self.text_content_last = ""
        self.call = main.WordDictionary(document=self.text_content)

        # Create a frame for the canvas and graph
        self.frame = customtkinter.CTkFrame(root)
        self.frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Creates a Side bar and Main menu
        Sidebar_Frame.Sidebar(self,root)
        Menu_Buttons.menu_buttons(self)

        # Creates a Text Widget
        Text_Widget.Text_Widget(self)

        # Creates the graph
        Graphs.Normal_Graph(self)
        Graphs.Scatter_Graph(self)

        # Initialize z-index flag
        self.z_index = True

        # Schedule get_text_widget every 1000ms
        self.root.after(1000, self.update_text_content)
        self.root.after(1000, self.schedule_get_text_widget)

        # Create a dictionary to store buttons
        self.buttons = {}
        self.higlighted_words = []





    def switch_z_index(self):
        if self.z_index:
            # Hide the text widget and show the Matplotlib graph
            self.text_widget.pack_forget()
            self.matplotlib_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            self.z_index = False
        else:
            # Hide the Matplotlib graph and show the text widget
            self.matplotlib_canvas.get_tk_widget().pack_forget()
            self.text_widget.pack(fill=tk.BOTH, expand=True)
            self.z_index = True

        # Hide the scatter plot if it's currently displayed
        self.scatter_canvas_widget.pack_forget()

    def switch_menu_1(self):
        # Hide the Matplotlib graph and show the text widget
        self.matplotlib_canvas.get_tk_widget().pack_forget()
        self.text_widget.pack(fill=tk.BOTH, expand=True)
        self.z_index = True

        # Hide the scatter plot if it's currently displayed
        self.scatter_canvas_widget.pack_forget()

        # Reset and update the dictionary
        self.reset_dictionary()
        text = self.get_text_widget()
        self.update_word_locations(text)

    def switch_menu_2(self):
        # Hide the text widget and show the Matplotlib graph
        self.text_widget.pack_forget()
        self.matplotlib_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.z_index = False

        # Hide the scatter plot if it's currently displayed
        self.scatter_canvas_widget.pack_forget()

        # Reset and update the dictionary
        self.reset_dictionary()
        text = self.get_text_widget()
        self.update_word_locations(text)

    def switch_menu_3(self):
        # Hide the Matplotlib graph and show the 3D scatter plot
        self.matplotlib_canvas.get_tk_widget().pack_forget()
        self.scatter_canvas_widget.pack(fill=tk.BOTH, expand=True)
        self.z_index = True
        self.text_widget.pack_forget()

        # Reset and update the dictionary
        self.reset_dictionary()
        text = self.get_text_widget()
        self.update_word_locations(text)

    def get_text_widget(self):
        text = self.text_widget.get("1.0", "end-1c")
        cleaned_text = self.clean_text(text)  # Clean the text
        return cleaned_text

    def schedule_get_text_widget(self):
        text = self.get_text_widget()

        self.text_content = text
        self.reset_dictionary()
        self.update_word_locations(text)  # Update the dictionary with cleaned text

        self.root.after(1200, self.schedule_get_text_widget)  # Schedule get_text_widget every 1000ms

    def update_text_content(self, event=None):
        # Get the current content of the Text widget
        new_text_content = self.text_widget.get("1.0", "end-1c")

        if new_text_content != self.text_content:
            self.text_content = new_text_content
            self.update_word_locations(new_text_content)  # Update the dictionary when text changes

    def update_word_locations(self, text):
        self.call.document = text
        self.call.final()  # Call the final method with the updated text

        # Print the word frequency list in descending order of count
        word_frequency = Counter(text.split())
        sorted_word_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

        # Update button names based on word frequencies
        self.update_buttons(sorted_word_frequency)

    def update_buttons(self, word_frequency):
        # Clear existing buttons
        for button_name, button in self.buttons.items():
            button.pack_forget()
            button.destroy()

        # Create new buttons based on word frequencies
        for i, (word, count) in enumerate(word_frequency[:20]):
            button = customtkinter.CTkButton(self.sidebar,
                                             text=f"{i + 1}. {word} ({count})",
                                             width=120,
                                             command=lambda w=word: self.toggle_highlight(w)) # Pass the word to toggle_highlight
            button.pack(fill=tk.X, pady=2)
            self.buttons[word] = button

    def toggle_highlight(self, word):
        if word in self.highlighted_words:
            # Word is already highlighted, unhighlight it
            self.unhighlight_word(word)
        else:
            # Word is not highlighted, highlight it
            self.highlight_word(word)

    def highlight_word(self, word):
        if word in self.buttons:
            button = self.buttons[word]
            button.configure(bg="yellow")  # You can change the highlight color here
            self.highlighted_words[word] = button
        else:
            self.highlighted_words[word] = None  # Store the word if the button is not created yet

    def unhighlight_word(self, word):
        if word in self.highlighted_words:
            button = self.highlighted_words[word]
            if button:
                button.configure(bg="SystemButtonFace")  # Reset the background color
            del self.highlighted_words[word]

    def reset_dictionary(self):
        # Reset the dictionary
        self.call.dictionary = {}

    def clean_text(self, text):
        cleaned_text = re.sub(r'[^\w\s]', ' ', text)
        cleaned_text = cleaned_text.lower()
        return cleaned_text


if __name__ == "__main__":
    root = tk.Tk()
    app = TkinterMatplotlibApp(root)
    root.mainloop()