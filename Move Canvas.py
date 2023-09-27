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
        self.blue_frame = Frame(root, bg="blue")
        self.blue_frame.pack(fill=tk.BOTH, expand=True)

        # Calculate the center coordinates of the blue frame
        blue_frame_width = 400  # You can adjust the width as needed
        blue_frame_height = 300  # You can adjust the height as needed
        center_x = blue_frame_width // 2
        center_y = blue_frame_height // 2

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
        corner_radius = 10 #

        # Add a comment about the corner radius
        self.canvas.create_text(center_x, rect_y2 + 10,corner_radius =8, fill="white")

        # Create the rounded rectangle
        self.canvas.create_rectangle(
            rect_x1, rect_y1, rect_x2, rect_y2, fill="red", outline="black", tags="draggable"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = Solution(root)
    root.mainloop()
