from curses import BUTTON1_CLICKED
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import filedialog, messagebox

def createWidgets():
    youtube_image = Label(root, text="Welcome to YouTube Video Downloader", font="100")
    youtube_image.grid(row=0, column=1, pady=20, padx=0)
    
    link_label = Label(root, text="Youtube URL: ", bg="#E8D")
    link_label.grid(row=1, column=0, pady=8, padx=3)
    
    root.link_text = Entry(root, width=60, textvariable=video_link)
    root.link_text.grid(row=1, column=1, pady=10, padx=0)
    
    destination_label = Label(root, text="Destination: ", bg="#E8D")
    destination_label.grid(row=2, column=0, pady=10, padx=3)
    
    root.destination_text = Entry(root, width=60, textvariable=download_path)
    root.destination_text.grid(row=2, column=1, pady=10, padx=0)
    
    browse_button = Button(root, text="Browse Directory", command=browse, width=15, bg="#05e8e0")
    browse_button.grid(row=3, column=1, pady=10, padx=0)
    
    download_button = Button(root, text="Download Video", command=download_video, width=20, bg="#05e8e0")
    download_button.grid(row=4, column=1, pady=10, padx=0)
    
    exit_button = Button(root, text="Exit", command=stop, bg="red")
    exit_button.grid(row=5, column=1, padx=0, pady=10)
    
def stop():
    if BUTTON1_CLICKED:
        messagebox.showwarning("Warning!", "Are you sure you want to exit?")
        
    root.destroy()
    
    
def browse():
    download_dir = filedialog.askdirectory(initialdir="Your Directory Path")
    
    download_path.set(download_dir)

    
def download_video(): 
    url = video_link.get()
    for link in url:
        if link == "":
            messagebox.showwarning("Warning", "URL is not provided.")
    folder = download_path.get()
    # url = video_link.get()
    for path in folder:
        if path == "":
            messagebox.showwarning("Warning", "Specify a path for your videos downloads!")
    
    yt = YouTube(url)

    stream = yt.streams.get_by_resolution("720p")
    stream.download(folder)
    
    messagebox.showinfo("Success!!", "Download Successful! You will find you video at\n"+folder)


root = tk.Tk()

root.geometry("680x400")
root.resizable(False, False)
root.title("YouTube Video Downloader")
root.config(background="#cec")

video_link = StringVar()
download_path = StringVar()

createWidgets()



root.mainloop()