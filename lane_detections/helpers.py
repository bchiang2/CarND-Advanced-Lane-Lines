import matplotlib.pyplot as plt

def plot_images(images):
    image_count = len(images)
    fig = plt.figure()
    for i, image in enumerate(images):
        tmp = fig.add_subplot(1, image_count, i+1)
        tmp.imshow(image)
    plt.show()
