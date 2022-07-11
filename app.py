import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import filedialog, messagebox

def createWidgets():
    
    link_label = Label(root, text="Youtube URL: ", bg="#E8D579")
    link_label.grid(row=1, column=0, pady=5, padx=5)
    
    root.link_text = Entry(root, width=60, textvariable=video_link)
    root.link_text.grid(row=1, column=1, pady=5, padx=5)
    
    destination_label = Label(root, text="Destination: ", bg="#e8d579")
    destination_label.grid(row=2, column=0, pady=5, padx=5)
    
    root.destination_text = Entry(root, width=45, textvariable=download_path)
    root.destination_text.grid(row=2, column=1, pady=5, padx=5)
    
    browse_button = Button(root, text="Browse", command="", width=10, bg="#05e8e0")
    browse_button.grid(row=2, column=2, pady=5, padx=5)
    
    download_button = Button(root, text="Download Video", command="", width=25, bg="#05e8e0")
    download_button.grid(row=3, column=1, pady=5, padx=5)
    
def browse():
    download_dir = filedialog.askdirectory(initialdir="Your Directory Path")
    download_path.set(download_dir)
    
def download_video(): 
    url = video_link.get()
    folder = download_path.get()
    
    get_video = YouTube(url)
    get_stream = get_video.streams.first()
    get_stream.download(folder)
    
    messagebox.showinfo("Success!!", "Download Successful! You will find you video at\n"+folder)

root = tk.Tk()

root.geometry("750x150")
root.resizable(False, False)
root.title("Video Downloader")
root.config(background="#ccc")

video_link = StringVar()
download_path = StringVar()

createWidgets()

root.mainloop()