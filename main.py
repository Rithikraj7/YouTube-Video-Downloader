from tkinter import *
from tkinter import messagebox
from pytube import YouTube
from PIL import ImageTk, Image

# Function to handle the download button click
def download_video():
    # Get the video URL from the input field
    video_url = url_entry.get()

    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the highest resolution stream
        stream = yt.streams.get_highest_resolution()

        # Download the video
        stream.download()
        messagebox.showinfo("Download Complete", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
window = Tk()
window.title("YouTube Video Downloader")

image_path = "C:/Users/dilip/PycharmProjects/pythonProject5/youtube1.jpg"
image = Image.open(image_path)
resized_image = image.resize((300, 205), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized_image)
image_label = Label(window, image=photo)
image_label.pack()
# Create a label for the URL input
url_label = Label(window, text="Video URL:")
url_label.pack()

# Create an entry field for the URL
url_entry = Entry(window, width=50)
url_entry.pack()

# Create a download button
download_button = Button(window, text="Download", command=download_video)
download_button.pack()

window.resizable(False, False)

window.geometry("500x500")
window.configure(bg="red")
# Run the main event loop
window.mainloop()

