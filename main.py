import cv2
from detect_face import DetectFace
from dominant_colors import DominantColors

# Set paths
image = "res/fall_0_0.png"
predictor = "shape_predictor_68_face_landmarks.dat"

# Create an DetectFace instance
df = DetectFace(predictor, image)

# Try: Extract mouth part
mouth = df.extract_face_part(df.mouth)

# Try: Extract right eye part
r_eye = df.extract_face_part(df.right_eye)

# Try: Extract left eye part
l_eye = df.extract_face_part(df.left_eye)

# Try : Extract cheek part
l_cheek = df.cheek_img[0]
r_cheek = df.cheek_img[1]


# Create an DominantColors instance on left cheek image
clusters = 5
lc_dc = DominantColors(l_cheek, clusters)
lc_colors = lc_dc.dominantColors()
print(lc_colors)
lc_dc.plotHistogram()

# Create an DominantColors instance on left cheek image
rc_dc = DominantColors(r_cheek, clusters)
rc_colors = rc_dc.dominantColors()
print(rc_colors)
rc_dc.plotHistogram()

# Try : Dominant color on right_eye
clusters = 6
dc_re = DominantColors(r_eye, clusters)
colors = dc_re.dominantColors()
print(colors)
dc_re.plotHistogram()
