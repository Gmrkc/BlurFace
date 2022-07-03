from tkinter import *
import gui_utils

def loop():

    root = Tk()
    root.title('Blurred')

    w = 400 # width for the Tk root
    h = 250 # height for the Tk root
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(width=False, height=False)

    btn_upload_video = Button(root, text="Upload Video File", command=lambda: gui_utils.upload_video(btn_upload_video ,btn_download_video), 
        height=2, width=18, highlightbackground='#3E4149')

    btn_download_video = Button(root, text="Download Video File", command=lambda: gui_utils.download_video(btn_upload_video, btn_download_video), 
        state=DISABLED, height=2, width=18, highlightbackground='#3E4149')

    btn_upload_image = Button(root, text="Upload Image File", command=lambda: gui_utils.upload_image(btn_upload_image, btn_download_image), 
        height=2, width=18, highlightbackground='#3E4149')

    btn_download_image = Button(root, text="Download Image File", command=lambda: gui_utils.download_image(btn_upload_image, btn_download_image), 
        state=DISABLED, height=2, width=18, highlightbackground='#3E4149')

    btn_realtime_start = Button(root, text="Start (q for quit)", command=lambda: gui_utils.realtime_start(btn_realtime_start, btn_realtime_record_start), 
        height=2, width=18, highlightbackground='#3E4149')
    
    btn_realtime_record_start = Button(root, text="Start with record (q for quit)", command=lambda: gui_utils.realtime_record_start(btn_realtime_start, 
        btn_realtime_record_start), height=2, width=18, highlightbackground='#3E4149')
    #dummy = Button(root, text="",background='#323232', height=2, width=15)

    r1 = StringVar()

    video_rbutton = Radiobutton(root, text = "Video", value = "Video", variable = r1, command=lambda: gui_utils.view_selected(
        r1, btn_upload_image, btn_download_image, btn_upload_video, btn_download_video, btn_realtime_start, btn_realtime_record_start), height=2, width=18).pack()

    image_rbutton = Radiobutton(root, text = "Image", value = "Image", variable = r1, command=lambda: gui_utils.view_selected(
        r1, btn_upload_image, btn_download_image, btn_upload_video, btn_download_video, btn_realtime_start, btn_realtime_record_start), height=2, width=18).pack()

    realtime_rbutton = Radiobutton(root, text = "RealTime", value = "RealTime", variable = r1, command=lambda: gui_utils.view_selected(
        r1, btn_upload_image, btn_download_image, btn_upload_video, btn_download_video, btn_realtime_start, btn_realtime_record_start), height=2, width=18).pack()


    root.mainloop()

if __name__ == "__main__":
    loop()