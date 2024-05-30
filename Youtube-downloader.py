from pytube import YouTube
from tkinter import Tk
from tkinter import filedialog

def download_video(file, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        heighest_res_stream = streams.get_highest_resolution()
        heighest_res_stream.download(output_path=save_path)

    except Exception as e:
        print(e)
    
url = r"https://youtu.be/ZucVXYoegVU?si=wP_fUtB2rtl__BwU"
save_path = r"C:\Users\Abdullah Shaikh\OneDrive\Desktop\Projects"

download_video(url, save_path)

