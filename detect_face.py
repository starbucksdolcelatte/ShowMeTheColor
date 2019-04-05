
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

        # init face parts
        self.mouth = []
        self.right_eyebrow = []
        self. left_eyebrow = []
        self.right_eye = []
        self. left_eye = []
        self.nose = []
        self.jaw = []

        # detect the face parts and set the variables
        self.detect_face_part()


    def detect_face_part(self):
        # loop over the face detections
        # i : name
        # 0 : mouth, 1 : right_eyebrow, 2 : left_eyebrow
        # 3 : right_eye, 4 : left_eye, 5 : nose, 6 : jaw
        face_parts = [[],[],[],[],[],[],[]]
        for (i, rect) in enumerate(self.rects):
            # determine the facial landmarks for the face region, then
            # convert the landmark (x, y)-coordinates to a NumPy array
            shape = self.predictor(self.gray, rect)
            shape = face_utils.shape_to_np(shape)

            idx = 0
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
                #print(name)
                #print(shape[i:j])

                face_parts[idx] = shape[i:j]
                idx += 1

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


        # set the variables
        # Caution: this coordinates fits on the RESIZED image.
        self.mouth = face_parts[0]
        self.right_eyebrow = face_parts[1]
        self.left_eyebrow = face_parts[2]
        self.right_eye = face_parts[3]
        self.left_eye = face_parts[4]
        self.nose = face_parts[5]
        self.jaw = face_parts[6]

    # parameter example : self.right_eye
    def extract_face_part(self, part):
        pts = part

        # Create an mask
        mask = np.zeros((self.img.shape[0], self.img.shape[1]))
        cv2.fillConvexPoly(mask, pts, 1)
        mask = mask.astype(np.bool)

        # extract right eye by applying polygon mask
        out = np.zeros_like(self.img)
        out[mask] = self.img[mask]
        #cv2.imshow("Image2", out)
        #cv2.waitKey(0)

        # crop the image
        (x, y, w, h) = cv2.boundingRect(pts)
        extracted_part = out[y:y + h, x:x + w]
        #cv2.imshow("Image2", extracted_part)
        #cv2.waitKey(0)

        return extracted_part
