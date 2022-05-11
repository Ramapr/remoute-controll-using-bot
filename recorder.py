import cv2
import os

#####################
#folder_path = "C:\\Users\\devuser\\vd"
# name = "video_"
# extra = '.avi'  # mp4
# fps = 30
# video_iter = 0
# #####################
# # get files with extension .mp4
# # list_of_video = list(filter(lambda x: True if x.endswith(extra) else False, os.listdir(folder_path)))
# # if len(list_of_video) > 0:
# #     # find last video
# #     iters = list(map(lambda x: int(x.split('_')[1][:-len(extra)]), list_of_video))
# #     video_iter = max(iters) + 1
#
# cap = cv2.VideoCapture(0)
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# codec = cv2.VideoWriter_fourcc(*'XVID') #'MPEG'
#
# # writer = cv2.VideoWriter(os.path.join(folder_path, name + str(video_iter) + extra),
# #                          codec,
# #                          fps,
# #                          (width, height)
# #                          )
#
# while True:
#     ret, frame = cap.read()
#     #writer.write(frame)
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
#
# cap.release()
# #writer.release()
# cv2.destroyAllWindows()

from threading import Thread
import time

class VideoStreamWidget(object):
    def __init__(self, src=0):
        self.capture = cv2.VideoCapture(src)
        # Start the thread to read frames from the video stream
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        # Read the next frame from the stream in a different thread
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()
            time.sleep(.01)

    def show_frame(self):
        # Display frames in main program
        cv2.imshow('frame', self.frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            self.capture.release()
            cv2.destroyAllWindows()
            exit(1)

if __name__ == '__main__':
    video_stream_widget = VideoStreamWidget()
    while True:
        try:
            video_stream_widget.show_frame()
        except AttributeError:
            pass