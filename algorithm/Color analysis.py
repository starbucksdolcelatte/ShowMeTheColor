#!/usr/bin/env python
# coding: utf-8

# In[72]:


# 평균 색상 추출
import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from skimage import io
from itertools import compress

# tone 구별 
from scipy.spatial import distance
import copy
import math
import operator

# main함수
from colormath.color_objects import LabColor, sRGBColor, HSVColor
from colormath.color_conversions import convert_color

# color extract 클래스
class DominantColors:

    CLUSTERS = None
    IMAGE = None
    COLORS = None
    LABELS = None

    def __init__(self, image, clusters=3):
        self.CLUSTERS = clusters
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.IMAGE = img.reshape((img.shape[0] * img.shape[1], 3))

        #using k-means to cluster pixels
        kmeans = KMeans(n_clusters = self.CLUSTERS)
        kmeans.fit(self.IMAGE)

        #the cluster centers are our dominant colors.
        self.COLORS = kmeans.cluster_centers_
        self.LABELS = kmeans.labels_

    def rgb_to_hex(self, rgb):
        return '#%02x%02x%02x' % (int(rgb[0]), int(rgb[1]), int(rgb[2]))

    # Return a list in order of color that appeared most often.
    def getHistogram(self):
        numLabels = np.arange(0, self.CLUSTERS+1)
        #create frequency count tables
        (hist, _) = np.histogram(self.LABELS, bins = numLabels)
        hist = hist.astype("float")
        hist /= hist.sum()

        colors = self.COLORS
        #descending order sorting as per frequency count
        colors = colors[(-hist).argsort()]
        hist = hist[(-hist).argsort()]
        for i in range(self.CLUSTERS):
            colors[i] = colors[i].astype(int)
        # Blue mask 제거
        fil = [colors[i][2] < 250 and colors[i][0] > 10 for i in range(self.CLUSTERS)]
        colors = list(compress(colors, fil))
        return colors, hist

    def plotHistogram(self):
        colors, hist = self.getHistogram()
        #creating empty chart
        chart = np.zeros((50, 500, 3), np.uint8)
        start = 0

        #creating color rectangles
        for i in range(len(colors)):
            end = start + hist[i] * 500
            r,g,b = colors[i]
            #using cv2.rectangle to plot colors
            cv2.rectangle(chart, (int(start), 0), (int(end), 50), (r,g,b), -1)
            start = end

        #display chart
        plt.figure()
        plt.axis("off")
        plt.imshow(chart)
        plt.show()

        return colors
    
   
 #tone analysis 함수
def is_warm(lab_b, a):
    '''
    파라미터 lab_b = [skin_b, hair_b, eye_b]
    a = 가중치 [skin, hair, eye]
    질의색상 lab_b값에서 warm의 lab_b, cool의 lab_b값 간의 거리를
    각각 계산하여 warm이 가까우면 1, 반대 경우 0 리턴
    '''
    # standard of skin, eyebrow, eye (눈썹, 눈동자는 0으로) 
    warm_b_std = [38.022000000000006, 0, 0]
    cool_b_std = [17, 0, 0]

    warm_dist = 0
    cool_dist = 0

    body_part = ['skin', 'eyebrow', 'eye']
    for i in range(1):
        warm_dist += abs(lab_b[i] - warm_b_std[i]) * a[i]
        
        print(body_part[i],"의 warm 기준값과의 거리")
        print(abs(lab_b[i] - warm_b_std[i]))
        
        cool_dist += abs(lab_b[i] - cool_b_std[i]) * a[i]
        
        print(body_part[i],"의 cool 기준값과의 거리")
        print(abs(lab_b[i] - cool_b_std[i]))
        
    if(warm_dist <= cool_dist):
        return 1 #warm
    else:
        return 0 #cool

# 이미지 자르는 함수
def trimming (img): 
    x = 100; 
    y = 100; 
    w = 100; 
    h = 100; 
    
    img_trim = img[y:y+h, x:x+w] 
    return img_trim 


# 원래 main
def analysis(imgpath):
    #######################################
    #           Face detection            #
    #######################################
    img=cv2.imread(imgpath)
    
    h,w,c=img.shape
    if((h>500) and (w>500)):
        img = trimming(img) # 이미지가 너무 크면 잘라서 확인
    
    face = [img, img,
            img, img,
            img, img]

    
    #######################################
    #         Get Dominant Colors         #
    #######################################
    temp = []
    clusters = 4
    for f in face:
        dc = DominantColors(f, clusters)
        face_part_color, _ = dc.getHistogram()
        #dc.plotHistogram()
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
        Lab_b.append(float(format(lab.lab_b,".2f")))
        hsv_s.append(float(format(hsv.hsv_s,".2f"))*100)

    Lab_b[1]=0
    Lab_b[2]=0
    
    print('Lab_b[skin]',Lab_b[0])

    #######################################
    #      Personal color Analysis        #
    #######################################
    Lab_weight = [100, 0, 0]
    hsv_weight = [10, 0, 0]
    
    if(is_warm(Lab_b, Lab_weight)):
        tone = '웜톤(warm)'
    else:
        tone = '쿨톤(cool)'
        
    # Print Result
    print('{}의 퍼스널 컬러는 {}입니다.'.format(imgpath, tone))

    
def main():    
    analysis('color_data\warm_spring.png')
    
    
if __name__ == '__main__':
    main()


# In[ ]:




