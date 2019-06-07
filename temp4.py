from getjson import GetJson
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from colormath.color_objects import LabColor, sRGBColor, HSVColor
from colormath.color_conversions import convert_color
LABELS = [0, 1, 2, 3]
COLORS = ['orange', 'green', 'red', 'blue']
COLORS_wc = ['red', 'blue', 'red', 'blue']
seasons = ['spring', 'summer', 'fall', 'winter']
getJson = GetJson()
C = getJson.get_standard('res/standard_bc.json')

for c in C:
    print("")
    for i in range(4):
        print(c[i][0][0])
skin_BC_B_vals = [[season[i][0][0] for i in range(4)] for season in C]
print(skin_BC_B_vals)
skin_BC_C_vals = [[season[i][0][1] for i in range(4)] for season in C]
print(skin_BC_C_vals)
skin_B0C = [[skin_BC_B_vals[i], [0, 0, 0, 0], skin_BC_C_vals[i]] for i in range(4)]

#plotting

fig = pyplot.figure()
ax = Axes3D(fig)
ax.set_xlabel('$Lab_b$', fontsize=20)
ax.set_ylabel('$0$', fontsize=20)
ax.set_zlabel('$HVC_C$', fontsize=20)
for label, pix in zip(LABELS, skin_B0C):
    print(seasons[label])
    print(pix[0])
    print(pix[1])
    print(pix[2])
    ax.scatter(pix[0], pix[1], pix[2], color = COLORS[label])
pyplot.show()

fig = pyplot.figure()
ax = Axes3D(fig)
ax.set_xlabel('$Lab_b$', fontsize=20)
ax.set_ylabel('$0$', fontsize=20)
ax.set_zlabel('$HVC_C$', fontsize=20)
for label, pix in zip(LABELS, skin_B0C):
    print(seasons[label])
    print(pix[0])
    print(pix[1])
    print(pix[2])
    ax.scatter(pix[0], pix[1], pix[2], color = COLORS_wc[label])
pyplot.show()

w = [skin_B0C[0], skin_B0C[2]]
c = [skin_B0C[1], skin_B0C[3]]
Lw = [0,2]
Lc = [1,3]
fig = pyplot.figure()
ax = Axes3D(fig)
ax.set_xlabel('$Lab_b$', fontsize=20)
ax.set_ylabel('$0$', fontsize=20)
ax.set_zlabel('$HVC_C$', fontsize=20)
for label, pix in zip(Lw, w):
    print(seasons[label])
    print(pix[0])
    print(pix[1])
    print(pix[2])
    ax.scatter(pix[0], pix[1], pix[2], color = COLORS[label])
pyplot.show()

fig = pyplot.figure()
ax = Axes3D(fig)
ax.set_xlabel('$Lab_b$', fontsize=20)
ax.set_ylabel('$0$', fontsize=20)
ax.set_zlabel('$HVC_C$', fontsize=20)
for label, pix in zip(Lc, c):
    print(seasons[label])
    print(pix[0])
    print(pix[1])
    print(pix[2])
    ax.scatter(pix[0], pix[1], pix[2], color = COLORS[label])
pyplot.show()
'''
skin_HSV_h_vals = [[float(hsv.hsv_h) for hsv in skin_hsv_spr], [float(hsv.hsv_h) for hsv in skin_hsv_smr], [float(hsv.hsv_h) for hsv in skin_hsv_fal], [float(hsv.hsv_h) for hsv in skin_hsv_wnt]]
skin_HSV_s_vals = [[float(hsv.hsv_s) for hsv in skin_hsv_spr], [float(hsv.hsv_s) for hsv in skin_hsv_smr], [float(hsv.hsv_s) for hsv in skin_hsv_fal], [float(hsv.hsv_s) for hsv in skin_hsv_wnt]]
skin_HSV_v_vals = [[float(hsv.hsv_v) for hsv in skin_hsv_spr], [float(hsv.hsv_v) for hsv in skin_hsv_smr], [float(hsv.hsv_v) for hsv in skin_hsv_fal], [float(hsv.hsv_v) for hsv in skin_hsv_wnt]]

IMAGE_hsv = [[skin_HSV_h_vals[i], skin_HSV_s_vals[i], skin_HSV_v_vals[i]] for i in range(4)]


#plotting

fig = pyplot.figure()
ax = Axes3D(fig)
ax.set_xlabel('$HSV_H$', fontsize=20)
ax.set_ylabel('$HSV_S$', fontsize=20)
ax.set_zlabel('$HSV_V$', fontsize=20)
for label, pix in zip(LABELS, IMAGE_hsv):
    print(seasons[label])
    print(pix[0])
    print(pix[1])
    print(pix[2])
    ax.scatter(pix[0], pix[1], pix[2], color = COLORS[label])
pyplot.show()
'''
