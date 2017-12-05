import cv2
import numpy as np

BOTTOM_LEFT = (265, 700)
BOTTOM_RIGHT = (1130, 700)
TOP_LEFT = (510, 525)
TOP_RIGHT = (845, 525)

SRC = np.float32([
    BOTTOM_LEFT,
    BOTTOM_RIGHT,
    TOP_LEFT,
    TOP_RIGHT
])

DST = np.float32([
    BOTTOM_LEFT,
    BOTTOM_RIGHT,
    (265, 525),
    (1130, 525),
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