import cv2
from detect_face import DetectFace

image = "res/irene.jpg"

# Create an instance
df = DetectFace("shape_predictor_68_face_landmarks.dat", image)

# Try: Extract mouth part
mouth = df.extract_face_part(df.mouth)
cv2.imshow("Mouth", mouth)
cv2.waitKey(0)

# Try: Extract right eye part
r_eye = df.extract_face_part(df.right_eye)
cv2.imshow("Right eye", r_eye)
cv2.waitKey(0)
