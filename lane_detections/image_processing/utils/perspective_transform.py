import cv2
import numpy as np

BOTTOM_LEFT = (256, 690)
BOTTOM_RIGHT = (1050, 690)
TOP_LEFT = (555, 480)
TOP_RIGHT = (730, TOP_LEFT[1])

SRC = np.float32([
    BOTTOM_LEFT,
    BOTTOM_RIGHT,
    TOP_LEFT,
    TOP_RIGHT
])

DST = np.float32([
    (BOTTOM_LEFT[0]+100, BOTTOM_LEFT[1]),
    (BOTTOM_RIGHT[0]-100, BOTTOM_RIGHT[1]),
    (BOTTOM_LEFT[0]+100, TOP_LEFT[1]),
    (BOTTOM_RIGHT[0]-100, TOP_LEFT[1]),
])

M = cv2.getPerspectiveTransform(SRC, DST)
M_INV = cv2.getPerspectiveTransform(DST, SRC)


def first_person_to_birds_eye_view(image):
    undistorted_image = image
    warped = cv2.warpPerspective(undistorted_image, M, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return warped


def birds_eye_to_first_person_view(image):
    newwarp = cv2.warpPerspective(image, M_INV, (image.shape[1], image.shape[0]))
    return newwarp
