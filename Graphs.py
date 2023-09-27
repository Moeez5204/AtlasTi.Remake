
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def Normal_Graph(self):
    self.fig = Figure(figsize=(5, 3))
    self.ax = self.fig.add_subplot(111)
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    self.ax.plot(x, y)
    self.matplotlib_canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
    self.matplotlib_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


def Scatter_Graph(self):
    self.scatter_fig = Figure(figsize=(5, 3))
    self.scatter_ax = self.scatter_fig.add_subplot(111, projection='3d')
    self.scatter_x = np.random.rand(100)
    self.scatter_y = np.random.rand(100)
    self.scatter_z = np.random.rand(100)
    self.scatter_ax.scatter(self.scatter_x, self.scatter_y, self.scatter_z)
    self.scatter_canvas = FigureCanvasTkAgg(self.scatter_fig, master=self.frame)
    self.scatter_canvas_widget = self.scatter_canvas.get_tk_widget()
    self.scatter_canvas_widget.pack(fill=tk.BOTH, expand=True)
    self.scatter_canvas_widget.pack_forget()  # Hide the scatter plot initially