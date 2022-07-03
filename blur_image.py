import cv2
import numpy as np
import imutils
import time

def blur_face_image(path):

    modelFile = "dnn_models/res10_300x300_ssd_iter_140000.caffemodel"
    configFile = "dnn_models/deploy.prototxt.txt"
    net = cv2.dnn.readNetFromCaffe(configFile, modelFile)

    image = cv2.imread(path)
    (h, w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(image, 1.0, (300, 300), (104.0, 177.0, 123.0))
    net.setInput(blob)
    detections = net.forward()

    # output videosunun ismi
    word = path
    # Splits at '/'
    mlist = word.split("/")
    last = mlist[-1]
    # Splits at '.'
    mlastlist = last.split(".")
    raw_name = mlastlist[0]
    ext = mlastlist[1]

    for i in range(0, detections.shape[2]):

        confidence = detections[0, 0, i, 2]

        if confidence > 0.5:

            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            text = "{:.2f}%".format(confidence * 100)
            y = startY - 10 if startY - 10 > 10 else startY + 10
            cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
            cv2.putText(image, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
            try:
                image[startY: endY, startX: endX] = cv2.medianBlur(image[startY: endY, startX: endX], 51)
            except:
                pass
      	
    cv2.imwrite('outputs/{name}_output.{ext}'.format(name=raw_name, ext=ext), image)

    #cv2.imshow("Output", image)
    #cv2.waitKey(0)
    cv2.destroyAllWindows() 