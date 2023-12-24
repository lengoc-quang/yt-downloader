#importing libraries
from pytube import YouTube
from pytube.cli import on_progress
from customtkinter import *
import pymsgbox
import getpass

#set the color theme
set_appearance_mode("System")
set_default_color_theme("blue")

# set the window
root = CTk()
root.title("Youtube Downloader")
root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(350, 175))

#label
label = CTkLabel(root, text = "Enter video URL: ", width = 250)
label.place(relx = 0.5, rely = 0.1, anchor = CENTER)

# input field
input = CTkEntry(root, 300, 30, 4, 2)
input.bind("<Button-1>", lambda e: input.delete(0, END))
input.place(relx = 0.5, rely = 0.25, anchor = CENTER)

# progress bar
progress_bar = CTkProgressBar(root, 250, 15, 5)
progress_bar.place(relx = 0.5, rely = 0.65, anchor = CENTER)
progress_bar.set(0.0)
percentage_of_completion=0

def on_progress(stream, chunk, bytes_remaining):
    global percentage_of_completion
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size
    progress_bar.set(percentage_of_completion)

#function that download the video
def main() :
    url = str(input.get())
    youtube = YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download("".join(['C:\\Users\\', getpass.getuser(), '\\Videos']))
    youtube.register_on_progress_callback(on_progress)
    progress_bar.set(1)
    pymsgbox.alert("".join(['Download directory: C:\\Users\\', getpass.getuser(), '\\Videos']), "Downloaded successfully!")
    progress_bar.set(0)

# button
btn = CTkButton(master = root, text = "Download", command = main, width = 250)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

#run the window
root.mainloop()