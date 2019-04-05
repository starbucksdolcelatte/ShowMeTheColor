import cv2
from detect_face import DetectFace
from dominant_colors import DominantColors

# Set paths
image = "res/irene.jpg"
predictor = "shape_predictor_68_face_landmarks.dat"

# Create an DetectFace instance
df = DetectFace(predictor, image)
'''
# Try: Extract mouth part
mouth = df.extract_face_part(df.mouth)
cv2.imshow("Mouth", mouth)
cv2.waitKey(0)
'''
# Try: Extract right eye part
r_eye = df.extract_face_part(df.right_eye)
cv2.imshow("Right eye", r_eye)
cv2.waitKey(0)


# Try : Extract cheek part
cv2.imshow("Left cheek", df.cheek_img[0])
cv2.waitKey(0)
cv2.imshow("Right cheek", df.cheek_img[1])
cv2.waitKey(0)


# Create an DominantColors instance on left cheek image
clusters = 5
dc = DominantColors(df.cheek_img[0], clusters)
colors = dc.dominantColors()
print(colors)
dc.plotHistogram()

# Try : Dominant color on right_eye
clusters = 6
dc_re = DominantColors(r_eye, clusters)
colors = dc_re.dominantColors()
print(colors)
dc_re.plotHistogram()
