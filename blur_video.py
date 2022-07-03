import cv2
import numpy as np
import imutils
import time

def blur_face_video(path):

    # dnn modelleri yükleme
    modelFile = "dnn_models/res10_300x300_ssd_iter_140000.caffemodel"
    configFile = "dnn_models/deploy.prototxt.txt"

    net = cv2.dnn.readNetFromCaffe(configFile, modelFile)
    cap = cv2.VideoCapture(path) # videoyu okutma
    time.sleep(1.0)

    # frame boyutları
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    # output videosunun ismi
    word = path
    # Splits at '/'
    mlist = word.split("/")
    last = mlist[-1]
    # Splits at '.'
    mlastlist = last.split(".")
    raw_name = mlastlist[0]
    ext = mlastlist[1]

    # writer objesi oluşturma
    if ext == "mp4":
        video_cod = cv2.VideoWriter_fourcc(*'mp4v')
    elif ext == "mov":
        video_cod = cv2.VideoWriter_fourcc(*'m', 'p', '4', 'v')

    video_output= cv2.VideoWriter(('outputs/{name}_output.{ext}'.format(name=raw_name, ext=ext)), video_cod, 30, (frame_width, frame_height))

    while True:

        frame = cap.read()[1] # tek tek frame
        
        if frame is not None:
            (h, w) = frame.shape[:2]
            blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
    
            # blob -> dnn network
            net.setInput(blob)
            detections = net.forward()

            for i in range(0, detections.shape[2]):

                confidence = detections[0, 0, i, 2]

                if confidence < 0.5:
                    continue

                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h]) # bulunan şekil çevresine kutu
                (startX, startY, endX, endY) = box.astype("int")

                text = "{:.2f}%".format(confidence * 100)
                y = startY - 10 if startY - 10 > 10 else startY + 10
                cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2) # diktörtgen
                cv2.putText(frame, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2) # olasılık yazısı
            
                try:
                    frame[startY: endY, startX: endX] = cv2.medianBlur(frame[startY: endY, startX: endX], 51) # diktörgene blur
                except:
                    pass

            video_output.write(frame) # her frame kaydetme

            # oluşturduktan sonra önizleme
            # cv2.imshow("Frame", frame)
            key = cv2.waitKey(1) & 0xFF
    
            # if the `q` key was pressed, break from the loop
            if key == ord("q"):
                break
        
        else:
            break

    cap.release()
    video_output.release()
    cv2.destroyAllWindows() 