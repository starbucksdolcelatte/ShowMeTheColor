import cv2
from detect_face import DetectFace
from dominant_colors import DominantColors
from tone_analysis import ToneAnalysis
import imutils
from colormath.color_objects import LabColor, sRGBColor, HSVColor
from colormath.color_conversions import convert_color


predictor = 'shape_predictor_68_face_landmarks.dat'
seasons = ['spring', 'summer', 'fall', 'winter']
a = [30, 20, 5] # 가중치
tone_analysis = ToneAnalysis()

for j in range(4): # j = season
    path = "res/tc2/" + seasons[j] + "/"
    for i in range(6):
        img = path + str(i+1) + '.jpg'
        print("")
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
        hsv_s = [] #skin, eyebr, eye
        for color in cy_rgb:
            rgb = sRGBColor(color[0], color[1], color[2], is_upscaled=True)
            lab = convert_color(rgb, LabColor, through_rgb_type=sRGBColor)
            lab_b.append(float(format(lab.lab_b,".2f")))
            hsv = convert_color(rgb, HSVColor, through_rgb_type=sRGBColor)
            hsv_s.append(float(format(hsv.hsv_s*100,".2f")))

        print("lab_b ", lab_b)
        print("hsv_s ", hsv_s)

        if(tone_analysis.is_warm(lab_b, a)):
            if(tone_analysis.is_spr(hsv_s, a)):
                print("봄웜톤")
            else:
                print("가을웜톤")
        else:
            if(tone_analysis.is_smr(hsv_s, a)):
                print("여름쿨톤")
            else:
                print("겨울쿨톤")
