import cv2
from detect_face import DetectFace
from dominant_colors import DominantColors
from tone_analysis import ToneAnalysis
from getjson import GetJson
import imutils
from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color
from itertools import compress

predictor = 'shape_predictor_68_face_landmarks.dat'
getJson = GetJson()
C = getJson.get_standard('res/standard.json')

# [spring[skin, eyebrow, eye, mouth], summer[skin, eyebrow, eye, mouth],
#  fall[skin, eyebrow, eye, mouth], winter[skin, eyebrow, eye, mouth]]
LLL = [[[],[],[],[]] for _ in range(4)]
aaa = [[[],[],[],[]] for _ in range(4)]
bbb = [[[],[],[],[]] for _ in range(4)]

RR = [[[],[],[],[]] for _ in range(4)]
GG = [[[],[],[],[]] for _ in range(4)]
BB = [[[],[],[],[]] for _ in range(4)]


seasons = ['spring', 'summer', 'fall', 'winter']
for j in range(4):
    path = "res/tc/" + seasons[j] + "/"
    for i in range(25):
        img = path + str(i+1) + '.jpg'
        print(img)

        df = DetectFace(predictor, img)

        # Try: Extract mouth part
        mouth = df.extract_face_part(df.mouth)

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

        le_dc = DominantColors(l_eye, clusters)
        le_dc.dominantColors()
        le_colors = le_dc.plotHistogram()

        leb_dc = DominantColors(l_eyebrow, clusters)
        leb_dc.dominantColors()
        leb_colors = leb_dc.plotHistogram()

        m_dc = DominantColors(mouth, clusters)
        m_dc.dominantColors()
        m_colors = m_dc.plotHistogram()

        # skin, hair, eye, mouth 순서
        fil = [leb_colors[i][2] < 250 and leb_colors[i][0] > 10 for i in range(clusters)]
        leb_colors = list(compress(leb_colors, fil))
        fil = [le_colors[i][2] < 250 and le_colors[i][0] > 10 for i in range(clusters)]
        le_colors = list(compress(le_colors, fil))
        fil = [m_colors[i][2] < 250 and m_colors[i][0] > 10 for i in range(clusters)]
        m_colors = list(compress(m_colors, fil))

        cy_rgb = [lc_colors[0:3], leb_colors[0:3], le_colors[0:3], m_colors[0:3]]
        cy_lab = []


        for iii in range(3):
            for sth in range(4):
                color = cy_rgb[sth][iii]
                RR[j][sth].append(color[0])
                GG[j][sth].append(color[1])
                BB[j][sth].append(color[2])
                rgb = sRGBColor(color[0], color[1], color[2], is_upscaled=True)
                lab = convert_color(rgb, LabColor, through_rgb_type=sRGBColor)
                cy_lab.append([format(lab.lab_l,".2f"), format(lab.lab_a,".2f"), format(lab.lab_b,".2f")])
                LLL[j][sth].append(format(lab.lab_l,".2f"))
                aaa[j][sth].append(format(lab.lab_a,".2f"))
                bbb[j][sth].append(format(lab.lab_b,".2f"))
                sth += 1

    bodys = ['left cheek', 'left eyebrow', 'left eye', 'mouth']
    print(seasons[j])
    for ii in range(4):
        print(bodys[ii])
        print("L : ", LLL[j][ii])
        print("a : ", aaa[j][ii])
        print("b : ", bbb[j][ii])

        print("R : ", RR[j][ii])
        print("G : ", GG[j][ii])
        print("B : ", BB[j][ii])

    plotRGB = [[[RR[j][ii][iii], GG[j][ii][iii], BB[j][ii][iii]] for iii in range(75)]
                for ii in range(4)]
    print("**************")
    print(plotRGB[0])
    print(plotRGB[1])
    print(plotRGB[2])
    print(plotRGB[3])

'''
        tone_analysis = ToneAnalysis()

        print("******************")
        a = [400, 200, 20] # 가중치
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
'''




'''
    closer_to_warm = 28 - cy_lab[0][2]
    print("distance to warm : ", closer_to_warm)
    closer_to_cool = cy_lab[0][2] - 19
    print("distance to cool : ", closer_to_cool)


    if(closer_to_warm < closer_to_cool):
        if(result_prob[spring] >= result_prob[fall]):
            print("봄 웜톤")
        else:
            print("가을 웜톤")
    else:
        if(result_prob[summer] >= result_prob[winter]):
            print("여름 쿨톤")
        else:
            print("겨울 쿨톤")
'''
