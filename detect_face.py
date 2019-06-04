
# coding: utf-8
# import the necessary packages
from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2
import matplotlib.pyplot as plt


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
        self.left_eyebrow = []
        self.right_eye = []
        self.left_eye = []
        self.nose = []
        self.jaw = []
        self.cheek_img = [[],[]] # index 0 : left, 1 : right

        # detect the face parts and set the variables
        self.detect_face_part() # mouth, right_eyebrow, ..., jaw : np.array
        self.cheek_img = self.detect_cheek() # image

    # return type : np.array
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
                '''
                # show the particular face part
                cv2.imshow("ROI", roi)
                cv2.imshow("Image", clone)
                cv2.waitKey(0)
                '''
            # visualize all facial landmarks with a transparent overlay
            output = face_utils.visualize_facial_landmarks(self.img, shape)
            #cv2.imshow("Image", output)
            #cv2.waitKey(0)

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
    # return type : image
    def extract_face_part(self, part):
        pts = part

        # Create an mask
        mask = np.zeros((self.img.shape[0], self.img.shape[1]))
        cv2.fillConvexPoly(mask, pts, 1)
        mask = mask.astype(np.bool)

        #print(mask)

        # Mask For background
        inversed_mask = np.logical_not(mask)
        #print(inversed_mask)


        # Create a blank black image
        blue = np.zeros_like(self.img)
        # Fill image with blue color(set each pixel to blue)
        blue[:] = [255, 0, 0]
        # extract background by applying inversed_mask

        # extract right eye by applying polygon mask
        out2 = np.zeros_like(self.img)
        out2[inversed_mask] = blue[inversed_mask]
        #cv2.imshow("out2", out2)
        #cv2.waitKey(0)

        # extract right eye by applying polygon mask
        out = np.zeros_like(self.img)
        out[mask] = self.img[mask]
        #out = out[mask] + blue

        #cv2.imshow("out", out)
        #cv2.waitKey(0)

        # crop the image
        (x, y, w, h) = cv2.boundingRect(pts)
        crop1 = out[y:y + h, x:x + w]
        crop2 = out2[y:y + h, x:x + w]
        crop = cv2.add(crop1,crop2)
        #cv2.imshow("Image2", crop)
        #cv2.waitKey(0)

        return crop


    # return type = image
    def detect_cheek(self):
        cheek = [[],[]]

        # rect is the face detected
        shape = self.predictor(self.gray, self.rects[0])
        shape = face_utils.shape_to_np(shape)

        # Cheeks are detected by relative position to the face landmarks
        left = self.img[shape[29][1]:shape[33][1], shape[4][0]:shape[48][0]] #left cheek
        right = self.img[shape[29][1]:shape[33][1], shape[54][0]:shape[12][0]] #right cheek

        cheek[0] = left
        cheek[1] = right

        # show the particular face part
        #cv2.imshow("left", left)
        #cv2.imshow("right", right)
        #cv2.waitKey(0)

        return cheek
