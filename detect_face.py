
# coding: utf-8
# import the necessary packages
from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2

class DetectFace:

    def __init__(self, shape_predictor_dat, image):
        # initialize dlib's face detector (HOG-based)
        # and then create the facial landmark predictor
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(shape_predictor_dat)

        #face detection part
        img = cv2.imread(image)
        self.img = imutils.resize(img, width = 500)
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

        # detect faces in the grayscale image
        self.rects = self.detector(self.gray, 1)
        print(rects)

    def detect_face_part(self):
        # loop over the face detections
        # i : name
        # 0 : mouth, 1 : right_eyebrow, 2 : left_eyebrow
        # 3 : right_eye, 4 : left_eye, 5 : nose, 6 : jaw
        for (i, rect) in enumerate(self.rects):
            # determine the facial landmarks for the face region, then
            # convert the landmark (x, y)-coordinates to a NumPy array
            shape = self.predictor(self.gray, rect)
            shape = face_utils.shape_to_np(shape)

            # loop over the face parts individually
            for (name, (i, j)) in face_utils.FACIAL_LANDMARKS_IDXS.items():
                # clone the original image so we can draw on it, then
                # display the name of the face part on the image
                clone = self.img.copy()
                cv2.putText(clone, name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                # loop over the subset of facial landmarks, drawing the
                # specific face part
                for (x, y) in shape[i:j]:
                    cv2.circle(clone, (x, y), 1, (0, 0, 255), -1)
                print(name)
                print(shape[i:j])

                # extract the ROI of the face region as a separate image
                (x, y, w, h) = cv2.boundingRect(np.array([shape[i:j]]))
                roi = self.img[y:y + h, x:x + w]
                roi = imutils.resize(roi, width=250, inter=cv2.INTER_CUBIC)

                # show the particular face part
                cv2.imshow("ROI", roi)
                cv2.imshow("Image", clone)
                cv2.waitKey(0)

            # visualize all facial landmarks with a transparent overlay
            output = face_utils.visualize_facial_landmarks(self.img, shape)
            cv2.imshow("Image", output)
            cv2.waitKey(0)

    def detect_right_eye(self):

    def detect_left_eye(self):

    def detect_mouth(self):

    def detect_right_cheek(self):

    def detect_left_cheek(self):
