import pandas as pd
import cv2 as cv

df=pd.read_csv("driving_log_3_cleaned.csv",header=None)

# Preprocessing the images before training 
def preprocessed(img_paths):

    img = cv.imread(img_paths)

    if img is None:
        print("Cannot read:", img_paths)
        return None

    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img = img[65:140, :, :]
    img = cv.resize(img, (200,66))
    img = (img.astype('float32') / 127.5) - 1.0

    return img
  
# Preprocessing of Augmented images (Filpped images)

def preprocessed_aug(img):
    img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    img= img[65:140, :, :]
    img=cv.resize(img,(200,66))
    img = (img.astype('float32') / 127.5) - 1.0

    return img
