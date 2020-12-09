from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import sys
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from itertools import compress
import cv2

from scipy.spatial import distance
import copy
import math
import operator

from colormath.color_objects import LabColor, sRGBColor, HSVColor
from colormath.color_conversions import convert_color

class DominantColors:

    CLUSTERS = None
    IMAGE = None
    COLORS = None
    LABELS = None

    def __init__(self, image, clusters=3):
        self.CLUSTERS = clusters
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.IMAGE = img.reshape((img.shape[0] * img.shape[1], 3))

        kmeans = KMeans(n_clusters = self.CLUSTERS)
        kmeans.fit(self.IMAGE)
        self.COLORS = kmeans.cluster_centers_
        self.LABELS = kmeans.labels_

    def rgb_to_hex(self, rgb):
        return '#%02x%02x%02x' % (int(rgb[0]), int(rgb[1]), int(rgb[2]))

    # Return a list in order of color that appeared most often.
    def getHistogram(self):
        numLabels = np.arange(0, self.CLUSTERS+1)
        (hist, _) = np.histogram(self.LABELS, bins=numLabels)
        hist = hist.astype("float")
        hist /= hist.sum()

        colors = self.COLORS
        colors = colors[(-hist).argsort()]
        hist = hist[(-hist).argsort()]
        for i in range(self.CLUSTERS):
            colors[i] = colors[i].astype(int)

        fil = [colors[i][2] < 250 and colors[i][0] > 10 for i in range(self.CLUSTERS)]
        colors = list(compress(colors, fil))
        return colors, hist

    def plotHistogram(self):
        colors, hist = self.getHistogram()
        chart = np.zeros((50, 500, 3), np.uint8)
        start = 0

        for i in range(len(colors)):
            end = start + hist[i] * 500
            r, g, b = colors[i]
            cv2.rectangle(chart, (int(start), 0), (int(end), 50), (r, g, b), -1)
            start = end

        plt.figure()
        plt.axis("off")
        plt.imshow(chart)
        plt.show()

        return colors

def is_warm(lab_b, a):
    warm_b_std = [38.022000000000006, 0, 0]
    cool_b_std = [17, 0, 0]

    warm_dist = 0
    cool_dist = 0

    for i in range(1):
        warm_dist += abs(lab_b[i] - warm_b_std[i]) * a[i]
        cool_dist += abs(lab_b[i] - cool_b_std[i]) * a[i]

    if(warm_dist <= cool_dist):
        return 1
    else:
        return 0

def trimming(img):
    x = 100
    y = 100
    w = 100
    h = 100

    img_trim = img[y:y+h, x:x+w]
    return img_trim


def analysis(imgpath):
    img = cv2.imread(imgpath)

    h, w, c = img.shape
    if((h > 500) and (w > 500)):
        img = trimming(img)

    face = [img, img,
            img, img,
            img, img]

    temp = []
    clusters = 4
    for f in face:
        dc = DominantColors(f, clusters)
        face_part_color, _ = dc.getHistogram()
        temp.append(np.array(face_part_color[0]))
    cheek1 = np.mean([temp[0], temp[1]], axis=0)
    cheek2 = np.mean([temp[2], temp[3]], axis=0)
    cheek3 = np.mean([temp[4], temp[5]], axis=0)

    Lab_b, hsv_s = [], []
    color = [cheek1, cheek2, cheek3]
    for i in range(3):
        rgb = sRGBColor(color[i][0], color[i][1], color[i][2], is_upscaled=True)
        lab = convert_color(rgb, LabColor, through_rgb_type=sRGBColor)
        hsv = convert_color(rgb, HSVColor, through_rgb_type=sRGBColor)
        Lab_b.append(float(format(lab.lab_b, ".2f")))
        hsv_s.append(float(format(hsv.hsv_s, ".2f"))*100)

    Lab_b[1] = 0
    Lab_b[2] = 0

    Lab_weight = [100, 0, 0]

    if(is_warm(Lab_b, Lab_weight)):
        tone = '웜톤(warm)'
    else:
        tone = '쿨톤(cool)'

    # Print Result
    return (tone)

app=Flask(__name__)

@app.route("/", methods=['GET','POST'])
def hello():
    if request.method == 'GET':
        return render_template('color-1.html')

    elif request.method == 'POST':
        f = request.files['img-path']
        f.save('./uploads'+secure_filename(f.filename))
        result = analysis('./uploads'+f.filename)

        if(result == "쿨톤(cool)"):
            return render_template('cool.html')

        elif result == "웜톤(warm)":
            return render_template('warm.html')
        
if __name__ == "__main__":
    app.run()