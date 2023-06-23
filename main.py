from tasktails import TaskTails
import platform
import os
import sys
import ctypes
import tkinter as tk
from easy_json import edit_value

def request_admin_access():
    if platform.system() == "Windows":
        # Elevate privileges by relaunching the script with admin access
        if not ctypes.windll.shell32.IsUserAnAdmin():
            root.destroy()
            script = "tasktails.py"
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, script, None, 1)
            edit_value('website_blocking', True, 'data/settings.json')

    elif platform.system() == "Linux":
        # Check if the script is running with sudo privileges
        if os.geteuid() != 0:
            args = ['sudo', sys.executable] + sys.argv + [os.environ]
            # Relaunch the script with sudo
            os.execlpe('sudo', *args)

def press_yes():
    if not ctypes.windll.shell32.IsUserAnAdmin():
        request_admin_access()

def press_no():
    root.destroy()
    edit_value('website_blocking', False, 'data/settings.json' )
    TaskTails()

root = tk.Tk()
question = tk.Label(root, text='proceed with site blocking feature?\n(You have to permit admin access to modify "host" file)')
question.grid(row=0, columnspan=2)

yes = tk.Button(root, text='yes', command=press_yes)
yes.grid(row=1, column=0, sticky='ew')
no = tk.Button(root, text='no', command=press_no)
no.grid(row=1, column=1, sticky='ew')

root.mainloop()