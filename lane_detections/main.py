import glob
import matplotlib.pyplot as plt
from image_processing.calibration import get_undistorted_image
from image_processing.perspective_transform import get_top_down_view
from image_processing.edge_detection import get_edges
from image_processing.color_space import get_satruated_pixels
from image_processing.line_filter import filter

def main():
    for image_path in glob.glob('../test_images/*.jpg'):
        image = plt.imread(image_path)
        image = get_undistorted_image(image=image)
        image = get_top_down_view(image=image)
        image = get_satruated_pixels(image=image)
        image = get_edges(image)
        image = filter(image)
        plt.imshow(image)
        plt.show()





if __name__ == "__main__":
    main()
