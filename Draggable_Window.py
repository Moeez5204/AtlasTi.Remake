import tkinter as tk
from tkinter import Canvas, Frame

class DraggableCanvas(Canvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.bind("<ButtonPress-1>", self.on_press)
        self.bind("<B1-Motion>", self.on_drag)

    def on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_drag(self, event):
        x, y = (event.x - self.start_x), (event.y - self.start_y)
        self.move("draggable", x, y)
        self.start_x = event.x
        self.start_y = event.y

class Solution:
    def __init__(self, root):
        self.root = root

        # Create the blue frame
        self.blue_frame = Frame(root, bg="blue", borderwidth=0)  # Set borderwidth to 0
        self.blue_frame.pack(fill=tk.BOTH, expand=True)

        # Calculate the center coordinates of the blue frame
        blue_frame_width = 1900  # Adjust the width as needed
        blue_frame_height = 2000  # Adjust the height as needed
        center_x = blue_frame_width // 2
        center_y = blue_frame_height // 2

        #4 Corners



        # Create a Canvas widget inside the blue frame
        self.canvas = DraggableCanvas(self.blue_frame, width=blue_frame_width, height=blue_frame_height, bg="blue")
        self.canvas.pack()

        # Calculate the size and position of the rounded rectangle
        rect_width = 100  # Width of the rounded rectangle
        rect_height = 50  # Height of the rounded rectangle
        rect_x1 = center_x - (rect_width // 2)
        rect_x2 = center_x + (rect_width // 2)
        rect_y1 = 20  # Move it slightly downwards
        rect_y2 = rect_y1 + rect_height
        self.corner_radius = 10  # Adjust the corner radius here

        # Add a comment about the corner radius
        self.canvas.create_text(center_x, rect_y2 + 10, text="Corner Radius Here", fill="white")

        # Create the rounded rectangle
        self.rectangle = self.canvas.create_rectangle(
            rect_x1, rect_y1, rect_x2, rect_y2, fill="red", outline="black", tags="draggable"
        )

        # Bind double-click event to expand the rectangle
        self.canvas.bind("<Double-Button-1>", self.expand_rectangle)

    def expand_rectangle(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.rectangle)
        new_x1 = x1 - (x2 - x1) / 2  # Double the width
        new_x2 = x2 + (x2 - x1) / 2
        new_y1 = y1 - (y2 - y1) / 2  # Double the height
        new_y2 = y2 + (y2 - y1) / 2
        self.canvas.coords(self.rectangle, new_x1, new_y1, new_x2, new_y2)

if __name__ == "__main__":
    root = tk.Tk()
    app = Solution(root)
    root.mainloop()
