import tkinter as tk

def highlight_words():
    # Get the content of the Text widget
    text_content = text_widget.get("1.0", "end-1c")

    # List of words to highlight
    words_to_highlight = ["example", "highlight", "certain"]

    for word in words_to_highlight:
        start_index = "1.0"
        while True:
            start_index = text_widget.search(word, start_index, stopindex="end-1c", nocase=True, exact=True)
            if not start_index:
                break
            end_index = text_widget.index(f"{start_index}+{len(word)}c")
            text_widget.tag_add("highlight", start_index, end_index)
            start_index = end_index

# Create the main tkinter window
root = tk.Tk()
root.title("Highlight Words Example")

# Create a Text widget
text_widget = tk.Text(root, wrap=tk.WORD)
text_widget.pack(fill=tk.BOTH, expand=True)

# Create a button to highlight words
highlight_button = tk.Button(root, text="Highlight Words", command=highlight_words)
highlight_button.pack()

# Create a tag for highlighting
text_widget.tag_configure("highlight", background="green")

# Insert some text into the Text widget
text_widget.insert("1.0", "This is an example of how to highlight certain words in tkinter.\n")
text_widget.insert("end", "You can highlight words like example, highlight, and certain with one button click.")

# Start the tkinter main loop
root.mainloop()
