import glob
import cv2
import matplotlib.pyplot as plt
import helpers
from lane_detections.image_processing.models.image import Image, CameraView
from lane_detections.image_processing.models.video import Video
from lane_detections.image_processing.utils.fit_lines import get_road


def test():
    for image_path in glob.glob('../test_images/test*.jpg'):
        image = plt.imread(image_path)


def process_image(image):
    img = Image(image)
    binary_color_lane = img.get_lane_binary(birds_eye=True)
    rgb_road_overlay, lanes_polynomial = get_road(binary_color_lane)

    front_view_with_road = cv2.addWeighted(
        img.get_image(birds_eye=False),
        1,
        CameraView(rgb_road_overlay).front(),
        0.2,
        0)

    image_with_cv_overlay = helpers.over_lay_image_to_rgb(
        rgb=front_view_with_road,
        image=CameraView(binary_color_lane).front(),
        alpha=0.8,
        beta=1,
        weights=(255, 0, 0))

    helpers.place_texts(image_with_cv_overlay, lanes_polynomial.get_texts())
    return image_with_cv_overlay


def main():
    video = Video('../project_video.mp4')
    video.play_video(image_function=process_image)


if __name__ == "__main__":
    main()
