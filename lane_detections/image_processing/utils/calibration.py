import cv2
import numpy as np
import glob
import matplotlib.pyplot as plt
import pickle
import os

PICKLED_FILE_PATH = r"calibration.pickle"

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
    image_paths = glob.glob(r'../camera_cal/*.jpg')
    for image_path in image_paths:
        image = plt.imread(image_path)
        corners = _get_image_corners(image=image)
        if corners is not None:
            images_points.append(corners)
            objects_points.append(get_prepared_object_points())
    return objects_points, images_points


if os.path.exists(PICKLED_FILE_PATH):
    print('Using pickled file')
    with open(PICKLED_FILE_PATH, 'rb') as f:
        data_set = pickle.load(f)
else:
    print('Making pickled file')
    obj_points, img_points = _get_calibration_points()
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, (1280, 720), None, None)
    data_set = {
        'obj_points': obj_points,
        'img_points': img_points,
        'ret': ret,
        'mtx': mtx,
        'dist': dist,
        'rvecs': rvecs,
        'tvecs': tvecs,
    }
    with open(PICKLED_FILE_PATH, 'wb') as f:
        pickle.dump(data_set, f, pickle.HIGHEST_PROTOCOL)


def get_undistorted_image(image):
    undistorted_image = cv2.undistort(image, data_set['mtx'], data_set['dist'], None, data_set['mtx'])
    return undistorted_image
