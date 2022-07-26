import PIL
from PIL import Image,ImageTk
import pytesseract
import cv2
import numpy as np
from keras.applications.inception_resnet_v2 import preprocess_input
from keras.models import load_model
from keras.preprocessing import image
from tkinter import *

width, height = 800, 600
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


price = '0'
def show_frame():

    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")

    img_counter = 0
    while True:
        ret, frame = cam.read()
        font = cv2.FONT_HERSHEY_SIMPLEX

        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)
        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            # SPACE pressed
            # ml model
            predict(frame)
            # price = '300'
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

    cam.release()

    cv2.destroyAllWindows()



def predict(image_path):

    model = load_model('model_inceptionresnetv2.h5')
    img = image.load_img(image_path, target_size=(299,299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    img_data = preprocess_input(x)
    prediction = np.argmax(model.predict(img_data), axis=1)
    price = predction

    root = Tk()
    root.bind('<Escape>', lambda e: root.quit())
    lmain = Label(root)
    lmain.pack()
    price_label = StringVar()
    label = Label(root, textvariable=price_label)
    price_label.set("Price")
    label.pack()

    var2 = StringVar()
    label2 = Label(root, textvariable=var2)
    label2.pack()

    var2.set(price)
    root.mainloop()

    #return 1 #prediction


# var.set("1")
# var2.set("2")
show_frame()
#root.mainloop()
