import cv2

class Video(object):
    def __init__(self, video_path):
        self.video_path = video_path

    def play_video(self, image_function):
        cap = cv2.VideoCapture(self.video_path)
        while (cap.isOpened()):
            ret, frame = cap.read()
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            processed_frame = image_function(rgb)
            cv2.imshow('frame', cv2.cvtColor(processed_frame, cv2.COLOR_RGB2BGR))
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


