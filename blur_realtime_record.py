import cv2
import numpy as np
import imutils
import uuid

def blur_face_realtime():

    modelFile = "dnn_models/res10_300x300_ssd_iter_140000.caffemodel"
    configFile = "dnn_models/deploy.prototxt.txt"
    net = cv2.dnn.readNetFromCaffe(configFile, modelFile)
    video_capture = cv2.VideoCapture(0)

    w = int(video_capture.get(3))
    h = int(video_capture.get(4))

    unique_filename = str(uuid.uuid4())

    video_cod = cv2.VideoWriter_fourcc(*'mp4v')
    video_output= cv2.VideoWriter('outputs/{unique_filename}.mp4'.format(unique_filename=unique_filename), video_cod, 10, (w,h))

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        if frame is not None:

            #frame = imutils.resize(frame, width=750)

            # grab the frame dimensions and convert it to a blob
            (h, w) = frame.shape[:2]
            blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))

            net.setInput(blob)
            detections = net.forward()

            # loop over the detections
            for i in range(0, detections.shape[2]):
                confidence = detections[0, 0, i, 2]

                # filter out weak detections by ensuring the `confidence` is
                if confidence < 0.5:
                    continue

                # compute the (x, y)-coordinates of the bounding box for the
                # object
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                # draw the bounding box of the face along with the associated
                # probability
                text = "{:.2f}%".format(confidence * 100)
                y = startY - 10 if startY - 10 > 10 else startY + 10
                cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2)
            
                try:
                    frame[startY: endY, startX: endX] = cv2.medianBlur(frame[startY: endY, startX: endX], 51)
                except:
                    pass
                cv2.putText(frame, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

            video_output.write(frame) 
            # show the output frame
            cv2.imshow("Frame", frame)
            # her frame kaydetme
            key = cv2.waitKey(1) & 0xFF

            # if the `q` key was pressed, break from the loop
            if key == ord("q"):
                break
        else:
            break 



    # do a bit of cleanup
    video_capture.release()
    video_output.release()
    
    cv2.destroyAllWindows()
   