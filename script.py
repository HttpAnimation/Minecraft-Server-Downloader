import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def read_versions_file():
    versions = []
    try:
        with open("versions.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    version, url = line.split("|")
                    versions.append((version.strip(), url.strip()))
    except FileNotFoundError:
        messagebox.showerror("File Not Found", "The 'versions.txt' file was not found.")
    return versions

def download_version(url):
    try:
        subprocess.run(["wget", url])
        messagebox.showinfo("Download Complete", "File downloaded successfully.")
    except subprocess.CalledProcessError:
        messagebox.showerror("Download Failed", "Failed to download the file.")

def set_dark_theme():
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton", foreground="white", background="gray30")
    style.configure("TLabel", foreground="white", background="gray30")
    style.configure("TFrame", background="gray30")

def main():
    versions = read_versions_file()
    
    root = tk.Tk()
    root.title("Version Downloader")
    root.geometry("400x300")
    set_dark_theme()

    canvas = tk.Canvas(root)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(root, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    num_columns = 3  # Number of buttons per row
    for index, (version, url) in enumerate(versions):
        row = index // num_columns
        col = index % num_columns

        button_frame = ttk.Frame(frame)
        button_frame.grid(row=row, column=col, padx=10, pady=5)

        button = ttk.Button(button_frame, text=version, command=lambda u=url: download_version(u))
        button.pack(padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
