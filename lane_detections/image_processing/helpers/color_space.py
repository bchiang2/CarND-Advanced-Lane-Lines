import numpy as np
import cv2


# hsv(57°, 0%, 89%)
# White S channel < 0.03 ; V & L > 93
# def get_satruated_pixels(image):
#     hls = cv2.cvtColor(image, cv2.COLOR_RGB2HLS)
#     S = hls[:, :, 2]
#     thresh = (90, 255)
#     binary = np.zeros_like(S)
#     binary[(S > thresh[0]) & (S <= thresh[1])] = 1
#     return binary
#
# def get_satruated_pixels(image):
#     hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#     H = hsv[:, :, 0]
#     thresh = (10,100)
#     binary = np.zeros_like(H)
#     binary[(H > thresh[0]) & (H <= thresh[1])] = 1
#     return binary

def get_white_binary(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    S = hsv[:, :, 1]
    V = hsv[:, :, 2]
    thresh = (200, 255)
    binary = np.zeros_like(V)
    binary[(V > thresh[0]) & (V <= thresh[1]) & (S <= 20)] = 1
    return binary

def get_yellow_binary(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    H = hsv[:, :, 0]
    S = hsv[:, :, 1]
    V = hsv[:, :, 2]
    thresh = (200, 255)
    binary = np.zeros_like(V)
    binary[(H > 50) & (H < 70) & (V > 150) & (S > 100)] = 1
    return binary