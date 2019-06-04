import cv2
from detect_face import DetectFace
from dominant_colors import DominantColors
from tone_analysis import ToneAnalysis
from getjson import GetJson
import imutils
from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color

# 이성경(res/lees.jpg) dominant colors by order of histogram
# skin, hair, eye 순서
lsk_rgb = [[222.5, 201.4, 188.9], [138.6, 98.4, 55.0], [159.8, 115.8, 61.7]]
lsk_lab = []
for color in lsk_rgb:
    rgb = sRGBColor(color[0], color[1], color[2], is_upscaled=True)
    lab = convert_color(rgb, LabColor, through_rgb_type=sRGBColor)
    lsk_lab.append([lab.lab_l, lab.lab_a, lab.lab_b])

# 봄웜1(res/spring_1_0.png) dominant colors by order of histogram
# skin, hair, eye 순서
sw1_rgb = [[201.58, 158.42, 142.44], [47.38, 37.76, 35.96], [44.92, 39.05, 41.00]]
sw1_lab = []
for color in sw1_rgb:
    rgb = sRGBColor(color[0], color[1], color[2], is_upscaled=True)
    lab = convert_color(rgb, LabColor, through_rgb_type=sRGBColor)
    sw1_lab.append([lab.lab_l, lab.lab_a, lab.lab_b])


# 채연(res/chaeyeon.jpg) dominant colors by order of histogram
# skin, hair, eye 순서
cy_rgb = [[239.74, 211.85, 196.76], [16.02, 23.75, 39.83], [51.38, 35.24, 40.31]]
cy_lab = []
for color in cy_rgb:
    rgb = sRGBColor(color[0], color[1], color[2], is_upscaled=True)
    lab = convert_color(rgb, LabColor, through_rgb_type=sRGBColor)
    cy_lab.append([lab.lab_l, lab.lab_a, lab.lab_b])

getJson = GetJson()
C = getJson.get_standard('res/standard.json')


tone_analysis = ToneAnalysis()

print("******************")
a = [400, 300, 10] # 가중치
spring = 0
summer = 1
fall = 2
winter = 3
result_prob = []
for season in range(4):
    result_prob.append(format(tone_analysis.probability(cy_rgb, season, C, a),".2f"))
print("결과")
print("봄   : ", result_prob[spring], "%")
print("여름 : ", result_prob[summer], "%")
print("가을 : ", result_prob[fall], "%")
print("겨울 : ", result_prob[winter], "%")
print("******************")
if(tone_analysis.is_warm(cy_rgb)):
    if(result_prob[spring] >= result_prob[fall]):
        print("봄 웜톤")
    else:
        print("가을 웜톤")
else:
    if(result_prob[summer] >= result_prob[winter]):
        print("여름 쿨톤")
    else:
        print("겨울 웜톤")

'''
# Set paths
image = "res/chaeyeon.jpg"
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
print("left cheek")
lc_dc.plotHistogram()

# Create an DominantColors instance on left cheek image
rc_dc = DominantColors(r_cheek, clusters)
rc_colors = rc_dc.dominantColors()
print("right cheek")
rc_dc.plotHistogram()

# Try : Dominant color on left_eye
clusters = 6
dc_le = DominantColors(l_eye, clusters)
colors = dc_le.dominantColors()
print("left eye")
dc_le.plotHistogram()

# Try : Dominant color on right_eye
dc_re = DominantColors(r_eye, clusters)
colors = dc_re.dominantColors()
print("right eye")
dc_re.plotHistogram()


# hair
hair_img = "res/chaeyeon_hair.jpg"
img = cv2.imread(hair_img)
resized_img = imutils.resize(img, width = 100)
clusters = 6
dc_hair = DominantColors(resized_img, clusters)
colors = dc_hair.dominantColors()
print("hair")
dc_hair.plotHistogram()

skin = DominantColors(df.cheek_img[0], clusters = 5)
skin_colors = list(skin.dominantColors()[0])
hair = DominantColors(resized_img, clusters = 6)
hair_colors = list(hair.dominantColors()[0])
eye = DominantColors(l_eye, clusters = 6)
eye_colors = list(eye.dominantColors()[0])
#skin_colors2 = list(skin.plotHistogram())
print("종윤님코드")
print(skin_colors)
print(hair_colors)
print(eye_colors)
print(" ")
print("descending order")
#print(skin_colors2)
print(" ")
'''
