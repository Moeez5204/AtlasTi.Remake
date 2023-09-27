import customtkinter
import tkinter as tk




def Sidebar(self,root):
    self.sidebar = customtkinter.CTkFrame(root, width=200)
    self.sidebar.pack(side=tk.LEFT, fill=tk.Y)