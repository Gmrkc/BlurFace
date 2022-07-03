from fileinput import filename
from tkinter import *
from tkinter import filedialog
import blur_video
import blur_image
import blur_realtime
import blur_realtime_record

def view_selected(r1, btn_upload_image, btn_download_image, btn_upload_video, btn_download_video, btn_realtime_start, btn_realtime_record_start):
    #print(r1.get())
    if r1.get() == "Video":
        btn_upload_image.pack_forget()
        btn_download_image.pack_forget()
        btn_realtime_start.pack_forget()
        btn_realtime_record_start.pack_forget()
        btn_upload_video.pack()
        btn_download_video.pack()
    elif r1.get() == "Image":
        btn_upload_video.pack_forget()
        btn_download_video.pack_forget()
        btn_realtime_start.pack_forget()
        btn_realtime_record_start.pack_forget()
        btn_upload_image.pack()
        btn_download_image.pack()
    elif r1.get() == "RealTime":
        btn_upload_image.pack_forget()
        btn_download_image.pack_forget()
        btn_upload_video.pack_forget()
        btn_download_video.pack_forget()
        btn_realtime_start.pack()
        btn_realtime_record_start.pack()

def upload_video(uploadbtn, downloadbtn):
    global file_video
    file_video = filedialog.askopenfilename(filetypes=(("mp4 files", "*.mp4"), ("mov files", "*.mov")))
    if len(file_video) == 0:
        uploadbtn['state'] = NORMAL
        downloadbtn['state'] = DISABLED
    if len(file_video) > 0:
        downloadbtn['state'] = NORMAL

def upload_image(uploadbtn, downloadbtn):
    global file_image
    file_image = filedialog.askopenfilename(filetypes=(("png files", "*.png"), ("jpg files", "*.jpg")))
    if len(file_image) == 0:
        uploadbtn['state'] = NORMAL
        downloadbtn['state'] = DISABLED
    if len(file_image) > 0:
        downloadbtn['state'] = NORMAL

def download_video(uploadbtn, downloadbtn):
    try:
        if len(file_video) > 0:
            blur_video.blur_face_video(file_video)
        downloadbtn['state'] = DISABLED
        uploadbtn['state'] = NORMAL
    except:
        pass

def download_image(uploadbtn, downloadbtn):
    try:
        if len(file_image) > 0:
            blur_image.blur_face_image(file_image)
        downloadbtn['state'] = DISABLED
        uploadbtn['state'] = NORMAL
    except:
        pass

def realtime_start(realtimebtn, realtimerecordbtn):
    realtimerecordbtn['state'] = DISABLED
    blur_realtime.blur_face_realtime()
    realtimerecordbtn['state'] = NORMAL

def realtime_record_start(realtimebtn, realtimerecordbtn):
    realtimebtn['state'] = DISABLED
    blur_realtime_record.blur_face_realtime()
    realtimebtn['state'] = NORMAL
