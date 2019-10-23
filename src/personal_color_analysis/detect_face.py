# coding: utf-8
# import the necessary packages
from imutils import face_utils
import numpy as np
import dlib
import cv2
import matplotlib.pyplot as plt

class DetectFace:
    def __init__(self, image):
        # initialize dlib's face detector (HOG-based)
        # and then create the facial landmark predictor
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor('../res/shape_predictor_68_face_landmarks.dat')

        #face detection part
        self.img = cv2.imread(image)
        #if self.img.shape[0]>500:
        #    self.img = cv2.resize(self.img, dsize=(0,0), fx=0.8, fy=0.8)

        # init face parts
        self.right_eyebrow = []
        self.left_eyebrow = []
        self.right_eye = []
        self.left_eye = []
        self.left_cheek = []
        self.right_cheek = []

        # detect the face parts and set the variables
        self.detect_face_part()


    # return type : np.array
    def detect_face_part(self):
        face_parts = [[],[],[],[],[],[],[]]
        # detect faces in the grayscale image
        rect = self.detector(cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY), 1)[0]

        # determine the facial landmarks for the face region, then
        # convert the landmark (x, y)-coordinates to a NumPy array
        shape = self.predictor(cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY), rect)
        shape = face_utils.shape_to_np(shape)

        idx = 0
        # loop over the face parts individually
        for (name, (i, j)) in face_utils.FACIAL_LANDMARKS_IDXS.items():
            face_parts[idx] = shape[i:j]
            idx += 1
        face_parts = face_parts[1:5]
        # set the variables
        # Caution: this coordinates fits on the RESIZED image.
        self.right_eyebrow = self.extract_face_part(face_parts[0])
        #cv2.imshow("right_eyebrow", self.right_eyebrow)
        #cv2.waitKey(0)
        self.left_eyebrow = self.extract_face_part(face_parts[1])
        self.right_eye = self.extract_face_part(face_parts[2])
        self.left_eye = self.extract_face_part(face_parts[3])
        # Cheeks are detected by relative position to the face landmarks
        self.left_cheek = self.img[shape[29][1]:shape[33][1], shape[4][0]:shape[48][0]]
        self.right_cheek = self.img[shape[29][1]:shape[33][1], shape[54][0]:shape[12][0]]

    # parameter example : self.right_eye
    # return type : image
    def extract_face_part(self, face_part_points):
        (x, y, w, h) = cv2.boundingRect(face_part_points)
        crop = self.img[y:y+h, x:x+w]
        adj_points = np.array([np.array([p[0]-x, p[1]-y]) for p in face_part_points])

        # Create an mask
        mask = np.zeros((crop.shape[0], crop.shape[1]))
        cv2.fillConvexPoly(mask, adj_points, 1)
        mask = mask.astype(np.bool)
        crop[np.logical_not(mask)] = [255, 0, 0]

        return crop
