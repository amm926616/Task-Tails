import subprocess
import sys

def restart_program():
    python = sys.executable
    subprocess.call([python, "main.py"])

# Your main script logic here

# When you want to restart the script
restart_program()
