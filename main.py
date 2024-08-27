import requests
from bs4 import BeautifulSoup
import os
import platform
import sys
import os
import platform
import win32com.client
import tkinter as tk  # Import tkinter
from tkinter import messagebox  # Import messagebox for displaying info

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def get_top_champions():
    url = "https://www.op.gg/champions"  # Replace with actual OP.gg URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    data_elements = soup.find_all('td', class_='css-1qly9n1 eq1151q5')

    # Extract the champion data (assuming it's the text content of the 'td' element)
    champion_tier = [element.text.strip() for element in data_elements]
    data_elements = soup.find_all('strong')
    champion_name = [element.text.strip() for element in data_elements]
    # ... (Implement logic to extract top 5 champion data from soup)
    return champion_name , champion_tier
def display_info(name, tier):
    root = tk.Tk()
    root.title("Top Tier 1 Champions")
    root.after(10000, root.destroy)
    # Create labels for each champion and tier
    for i in range(20):  # Adjust range according to the number of champions you want to display
        label_name = tk.Label(root, text=f"{name[i]}")
        label_name.pack()

    root.mainloop()



def configure_autostart():
    """Configures the app to start automatically on system startup."""
    system = platform.system()
    if system == "Windows":
        # Windows auto-start configuration (using shortcut)
        startup_path = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        shortcut_path = os.path.join(startup_path, "LoL Top Champions.lnk")
        script_path = os.path.abspath(sys.argv[0])  # Get the absolute path to your script

        # Create the shortcut using win32com.client
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.Targetpath = script_path
        shortcut.WorkingDirectory = os.path.dirname(script_path)
        shortcut.save()

        # Ensure the shortcut is created and the script is executable
        # if os.path.exists(shortcut_path) and os.access(script_path, os.X_OK):
        #     print("Auto-start configuration successful!")
        # else:
        #     print("Error creating auto-start shortcut.")


def main():
    name, tier = get_top_champions()
    display_info(name, tier)
if __name__ == "__main__":
    configure_autostart() 
    main()


