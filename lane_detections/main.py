import glob
import cv2
import matplotlib.pyplot as plt
from moviepy.editor import VideoFileClip
import helpers
from lane_detections.image_processing.models.image import Image, CameraView
from lane_detections.image_processing.models.video import Video
from lane_detections.image_processing.utils.fit_lines import get_road
from lane_detections.image_processing.utils.edge_detection import get_edges


def test():
    for image_path in glob.glob('../test_images/test*.jpg'):
        image = plt.imread(image_path)


def process_image(image):
    img = Image(image)
    binary_color_lane = img.get_lane_binary(birds_eye=True)
    # return helpers.over_lay_image_to_rgb(
    #     rgb=img.get_image(birds_eye=True),
    #     binary=get_edges(binary_color_lane),
    #     alpha=1,
    #     beta=1
    # )
    # return helpers.over_lay_image_to_rgb(
    #     rgb=img.get_image(birds_eye=True),
    #     image=CameraView(binary_color_lane).image,
    #     alpha=0.2,
    #     beta=1
    # )
    front_with_road = cv2.addWeighted(
        img.get_image(birds_eye=False),
        1,
        CameraView(get_road(binary_color_lane)).front(),
        0.2,
        0)

    front_with_road_lane = helpers.over_lay_image_to_rgb(front_with_road, CameraView(binary_color_lane).front(), 0.9, 1, (255,0,0))
    return front_with_road_lane


def main():
    video = Video('../project_video.mp4')
    video.play_video(process_image)


if __name__ == "__main__":
    main()
