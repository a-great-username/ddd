import pydicom
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt
import glob
import sys
import re
from vtkplotter import *

def transform_to_hu(medical_image, image):
    intercept = medical_image.RescaleIntercept
    slope = medical_image.RescaleSlope
    hu_image = image * slope + intercept

    return hu_image

def window_image(image, window_center, window_width):
    img_min = window_center - window_width // 2
    img_max = window_center + window_width // 2
    window_image = image.copy()
    window_image[window_image < img_min] = img_min
    window_image[window_image > img_max] = img_max
    
    return window_image

# file_path = "./DICOM/0008782/DWI0001.dcm"
# output_path = "./"

paths = glob.glob("./DICOM/0009455/*.dcm")
# print(type(paths))
dwi_files = []
for path in paths:
    if re.search("DWI",path):
        # print(path) 
        dwi_files.append(path)
        # print(pydicom.read_file(path))
        # input()
        # print(pydicom.read_file(path).pixel_array.shape)
        # volume = load(pydicom.read_file(path)) #returns a vtkVolume object
        # show(volume, bg='white') 
    # print(path.split('.'))
# print(len(dwi_files))
# input()
# plt.figure(figsize=(6,8))
# i=0#

# # print(print('glob: {}'.format(path)))
for dwi_file in dwi_files:
#     i+=1
    dwi = pydicom.read_file(dwi_file)
#     # print(dwi.SliceThickness )
#     # print(dwi.SpacingBetweenSlices)
    image = dwi.pixel_array
#     print(type(image))
    # print(image.shape)
    # print(image.min())
    # print(image.max())
    # plt.subplot(6,8,i)
    # plt.imshow(image, cmap=plt.cm.bone)  # set the color map to bone
    # plt.title(dwi_file.split('/')[-1])
    # plt.axis('off')
    # plt.imshow(image, cmap='gray')


      
# plt.show()
# ps = dwi_files[0].PixelSpacing
# ss = dwi_files[0].SliceThickness
# ax_aspect = ps[1]/ps[0]
# sag_aspect = ps[1]/ss
# cor_aspect = ss/ps[0]    

# img_shape = list(dwi_files[0].pixel_array.shape)
# img_shape.append(len(dwi_files))
# img3d = np.zeros(img_shape)

# for i, s in enumerate(dwi_files):
#     img2d = s.pixel_array
#     img3d[:, :, i] = img2d


# a1 = plt.subplot(2, 2, 1)
# plt.imshow(img3d[:, :, img_shape[2]//2], cmap=plt.cm.bone)
# a1.set_aspect(ax_aspect)

# a2 = plt.subplot(2, 2, 2)
# plt.imshow(img3d[:, img_shape[1]//2, :], cmap=plt.cm.bone)
# a2.set_aspect(sag_aspect)

# a3 = plt.subplot(2, 2, 3)
# plt.imshow(img3d[img_shape[0]//2, :, :].T, cmap=plt.cm.bone)
# a3.set_aspect(cor_aspect)

# plt.show()