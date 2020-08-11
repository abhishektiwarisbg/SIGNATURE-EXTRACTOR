import cv2
import imutils
import numpy as np
from utils.transform import four_point_transform


def dewarp_book(image):
    # get input image ration to keep best output resolution quality
    ratio = image.shape[0] / 500.0
    # copy source image for filter operations
    orig = image.copy()
    # resize the input image
    image = imutils.resize(image, height=500)

    # convert rgb input image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    return gray
