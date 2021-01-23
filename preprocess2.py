import cv2
from matplotlib import pyplot as plt
import numpy as np
from os.path import isfile, join
from os import listdir
from imutils import paths

def test_module():
    print("Module is connected!")
    

    
def get_folder_list(string1):
    #string1 = 'DYS'
    string2 = 'fyp-deep-learning-eeg/FYP 2/output/' + string1
    imagePaths = paths.list_images(string2)
    str1 = []
    for imagePath in imagePaths:
        str1.append(imagePath[:45])
    str2 = str2 = list(set(str1))
    return str2
    
def load_all_image_folder(folder):
    images = np.empty(shape=(13,128), dtype=object)
    x = 0
    for i in folder:
        images[x] = load_image_folder(i)
        x = x+1

    return images

def load_image_folder(filepath, limit=None):
    
    onlyfiles = [f for f in listdir(filepath) if isfile(join(filepath,f)) and '.png' in f]
    # hantar terus all folder name in png 
    print('Num pics in folder: {}'.format(len(onlyfiles)))
    if limit != None:
        num_files = limit
        print('Only {} images being used'.format(num_files))
    else:
        num_files = len(onlyfiles)
        print('All images being used')
    images = np.empty(num_files, dtype=object)
    for n in range(0, num_files):
      images[n] = cv2.imread(join(filepath,onlyfiles[n]))
      images[n] = cv2.cvtColor(images[n], cv2.COLOR_BGR2RGB)
    return images
    
def prep_total_pipeline(folder_list, limit=None):
    X = 0
    y = 0

    for i in range(len(folder_list)): #sentiasa 2
        if limit == None:
            #images = load_image_folder(folder_list[i])# original
            images = multiple_folder(folder_list[i])
        else:
            #images = load_image_folder(folder_list[i], limit)
            images = multiple_folder(folder_list[i], limit)
        
        cropped = [] 
        for a in images:
            cropp = cropped_img(a)
            cropped.append(cropp) # change this to crop image
        
        if type(X) == int:
            X = np.array(cropped)
        else:
            X = np.vstack((X, np.array(cropped)))
        if type(y) == int:
            y = np.zeros(len(cropped))
        else:
            y_arr = np.zeros(len(cropped))
            y_arr.fill(i)
            y = np.append(y, y_arr)
        print('X shape: {} -=-=-=-= y shape: {}'.format(X.shape, y.shape))
    return np.array(X), y

def multiple_folder(folder_name):
    #folder_name = 'DYS'
    folder = get_folder_list(folder_name)
    allImages = load_all_image_folder(folder)
    allImages2 = allImages.flatten()
    return allImages2
    
def cropped_img(img):
    y1 = 50
    x1 = 183
    crop_img = img[y1:y1+480, x1:x1+540]
    
    return crop_img
