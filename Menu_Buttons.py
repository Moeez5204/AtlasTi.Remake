import tkinter as tk
import customtkinter


# Create 3 menu buttons on top of the existing buttons

def menu_buttons(self):

        menu_buttons_frame = customtkinter.CTkFrame(self.sidebar)
        menu_buttons_frame.pack(fill=tk.X)
        menu_button_1 = customtkinter.CTkButton(menu_buttons_frame, text="Menu 1", width=68, corner_radius=5, command=self.switch_menu_1)
        menu_button_1.pack(side=tk.LEFT, padx=2.5)
        menu_button_2 = customtkinter.CTkButton(menu_buttons_frame, text="Menu 2", width=68, corner_radius=5, command=self.switch_menu_2)
        menu_button_2.pack(side=tk.LEFT, padx=2.5)
        menu_button_3 = customtkinter.CTkButton(menu_buttons_frame, text="Menu 3", width=68, corner_radius=5, command=self.switch_menu_3)
        menu_button_3.pack(side=tk.LEFT, padx=2.5)