import tkinter as tk
import customtkinter
import lorem
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Set CustomTkinter appearance mode and default color theme
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Test")
        self.geometry(f"{1000}x{500}")

        self.left_sidebar_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        self.left_sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.menu_top_bar = customtkinter.CTkFrame(self.left_sidebar_frame, width=200, height=10, corner_radius=20)
        self.menu_top_bar.pack(side=tk.TOP)

        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.left_sidebar_frame)
        self.scrollable_frame.pack(fill=tk.BOTH, expand=True)

        # Add buttons to the scrollable frame
        self.widgets_to_lift = []  # Store widgets to lift

        for i in range(21):  # Add some buttons to demonstrate scrolling
            button = customtkinter.CTkButton(self.scrollable_frame, text=f"Button {i}")
            button.pack(padx=20, pady=10, fill=tk.X)
            button.configure(command=lambda b=button: self.button_click(b))

        # Create a frame for the main content
        self.main_content_frame = customtkinter.CTkFrame(self)
        self.main_content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(self.main_content_frame, orient=tk.HORIZONTAL)
        scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        # Text widget
        font = ("San Francisco", 12)
        random_text = lorem.text()

        self.text_widget = tk.Text(self.main_content_frame, wrap=tk.NONE, xscrollcommand=scrollbar.set,
                                   font=font)
        self.text_widget.insert("1.0", random_text)
        self.text_widget.pack(fill=tk.BOTH, expand=True)
        self.widgets_to_lift.append(self.text_widget)

        # Create a Matplotlib 3D figure
        fig = Figure(figsize=(6, 6))
        ax = fig.add_subplot(111, projection='3d')  # Create a 3D subplot

        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        X, Y = np.meshgrid(x, y)
        Z = np.sin(np.sqrt(X ** 2 + Y ** 2))

        ax.plot_surface(X, Y, Z, cmap='viridis')

        # Create a FigureCanvasTkAgg object to display the 3D plot
        self.canvas = FigureCanvasTkAgg(fig, master=self.main_content_frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.place(relwidth=1.0, relheight=1.0)

        self.canvas_widget.lower()  # Start with the canvas widget lowered

        self.bind("<KeyPress-1>", lambda event: self.switch_to_text())
        self.bind("<KeyPress-2>", lambda event: self.switch_to_3d_graph())

    def switch_to_text(self):
        self.text_widget.lift()
        self.canvas_widget.lower()

    def switch_to_3d_graph(self):
        self.text_widget.lower()
        self.canvas_widget.lift()


if __name__ == "__main__":
    app = App()
    app.mainloop()
