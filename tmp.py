import cv2
import numpy as np
import glob
import matplotlib.pyplot as plt

# prepare object points
NX = 9
NY = 6


def get_prepared_object_points():
    objpoints = np.zeros((NX * NY, 3), np.float32)
    objpoints[:, :2] = np.mgrid[0:NX, 0:NY].T.reshape(-1, 2)
    return objpoints


def _get_image_corners(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (NX, NY), None)
    if ret:
        return corners
    return None


def _get_calibration_points():
    images_points = []
    objects_points = []
    image_paths = glob.glob(r'./camera_cal/*.jpg')
    for image_path in image_paths:
        image = plt.imread(image_path)
        corners = _get_image_corners(image=image)
        if corners is not None:
            images_points.append(corners)
            objects_points.append(get_prepared_object_points())
    return objects_points, images_points


obj_points, img_points = _get_calibration_points()


def get_undistorted_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, gray.shape[::-1], None, None)
    undistorted_image = cv2.undistort(image, mtx, dist, None, mtx)
    return undistorted_image

img = plt.imread('./test_images/straight_lines1.jpg')

undistorted = get_undistorted_image(img)
plt.imshow(undistorted)
plt.show()