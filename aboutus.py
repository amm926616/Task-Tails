import tkinter as tk
from settings import Settings 

class Aboutus:
    def __init__(self, window):
        # Set the window title
        settings = Settings()
        window.title("About Us")
        window.config(bg=settings.bg_color)
        
        # Add a label for your names
        names_label = tk.Label(window, text="Developed by Aung Myint Myat and Wai Yan Htut", font=("Arial", 18, "bold"), fg=settings.fg_color, bg=settings.bg_color, padx=10)
        names_label.pack()
        
        # Add a label for the description
        description_label = tk.Label(window, text="\nWe are self-taught software developers. We write programs in C, C++, Javascript, Java \nand Python scripts for automation and various other purposes.", fg=settings.fg_color, bg=settings.bg_color)
        description_label.pack()
        
        # Add a label for the program information
        program_label = tk.Label(window, text="The program may have flaws and bugs, but we hope it can be helpful for your study. Enjoy!", fg=settings.fg_color, bg=settings.bg_color)
        program_label.pack()
        
        # Add a label for contact information
        contact_label = tk.Label(window, text="\nContact us for feedbacks and bug reports:", font=("Arial", 12), fg=settings.fg_color, bg=settings.bg_color)
        contact_label.pack()

        # Our emails
        amm = tk.Text(window, wrap="none", height=1, width=19, borderwidth=0, highlightthickness=0, fg=settings.fg_color, bg=settings.bg_color)
        amm.insert("1.0", "amm926616@gmail.com")
        amm.config(state='disabled')
        amm.pack()

        wyh = tk.Text(window, wrap="none", height=1, width=23, borderwidth=0, highlightthickness=0, fg=settings.fg_color, bg=settings.bg_color)
        wyh.insert("1.0", "waiyanhtut354@gmail.com")
        wyh.config(state='disabled')
        wyh.pack()

        contribute = tk.Label(window, text='\nIf you want to contribute this project on github, Go ahead.\nWe appreciate it very much.', fg=settings.special_text_color, bg=settings.bg_color)
        contribute.pack()

