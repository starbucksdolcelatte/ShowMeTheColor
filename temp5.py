import cv2
from detect_face import DetectFace
from dominant_colors import DominantColors
from tone_analysis import ToneAnalysis
from getjson import GetJson
import imutils
from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color


predictor = 'shape_predictor_68_face_landmarks.dat'
seasons = ['spring', 'summer', 'fall', 'winter']
a = [30, 20, 5]
tone_analysis = ToneAnalysis()
for j in range(4):
    path = "res/tc2/" + seasons[j] + "/"
    for i in range(6):
        img = path + str(i+1) + '.jpg'
        print(img)
        df = DetectFace(predictor, img)
        # Try: Extract left eye part
        l_eye = df.extract_face_part(df.left_eye)
        # Try: Extract left eyebrow part
        l_eyebrow = df.extract_face_part(df.left_eyebrow)
        # Try : Extract cheek part
        l_cheek = df.cheek_img[0]

        # Create an DominantColors instance on left cheek image
        clusters = 5
        lc_dc = DominantColors(l_cheek, clusters)
        lc_dc.dominantColors()
        lc_colors = lc_dc.plotHistogram()

        leb_dc = DominantColors(l_eyebrow, clusters)
        leb_dc.dominantColors()
        leb_colors = leb_dc.plotHistogram()

        le_dc = DominantColors(l_eye, clusters)
        le_dc.dominantColors()
        le_colors = le_dc.plotHistogram()

        cy_rgb = [lc_colors[0], leb_colors[0], le_colors[0]]
        lab_b = [] #skin, eyebr, eye
        for color in cy_rgb:
            rgb = sRGBColor(color[0], color[1], color[2], is_upscaled=True)
            lab = convert_color(rgb, LabColor, through_rgb_type=sRGBColor)
            lab_b.append(float(format(lab.lab_b,".2f")))

        print(lab_b)
        if(tone_analysis.is_warm(lab_b, a)):
            print("웜톤")
        else:
            print("쿨톤")
