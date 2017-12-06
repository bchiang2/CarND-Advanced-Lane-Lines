import glob
import cv2
import matplotlib.pyplot as plt
from moviepy.editor import VideoFileClip
import helpers
from lane_detections.image_processing.models.image import Image, CameraView
from lane_detections.image_processing.models.video import Video


def test():
    for image_path in glob.glob('../test_images/test*.jpg'):
        image = plt.imread(image_path)


def process_image(image):
    img = Image(image)
    lane_binary = CameraView(img.get_lane_binary(birds_eye=True)).front()
    return helpers.over_lay_binary_to_rgb(
        rgb=img.get_image(birds_eye=False),
        binary=lane_binary
    )


def main():
    video = Video('../project_video.mp4')
    video.play_video(process_image)


if __name__ == "__main__":
    main()
