import numpy as np
import cv2

from image_processing.calibration import get_undistorted_image

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


def get_top_down_view(image):
    undistorted_image = get_undistorted_image(image)
    M = cv2.getPerspectiveTransform(SRC, DST)
    warped = cv2.warpPerspective(undistorted_image, M, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return warped
