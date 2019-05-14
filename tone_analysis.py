from scipy.spatial import distance
import copy
from get_std_from_xls import ListFromExcel
import math
import operator

converter = ListFromExcel('res/tone_color_standard.xlsx')
# STANDARD(RGB based)
# list[0] = spring, [1] = summer, [2] = fall, [3] = winter
label = ['spring', 'summer', 'fall', 'winter']
skin_rgb = converter.get_rgb(converter.skin)
pupil_rgb = converter.get_rgb(converter.pupil)
hair_rgb = converter.get_rgb(converter.hair)
C = converter.convert_list(skin_rgb[0:2], hair_rgb, pupil_rgb)

# 이성경(res/lees.jpg) dominant colors by order of histogram
skin_lsg = [[222.5, 201.4, 188.9], [227.2, 209.5, 203.3]] # left cheek
pupil_lsg = [[159.8, 115.8, 61.7], [186.5, 156.1, 129.0],
             [126.0, 77.5, 42.8], [88.1, 41.1, 20.9]] # right eye
hair_lsg = [[138.6, 98.4, 55.0],[161.8, 121.4, 72.0]]

skin_lab = [[87.39, -2.18, 16.21],[84.48, 0.75, 14.23],[80.58, -0.07, 25.46],[91.47, -0.73, 9.96]]
skin_lsg_lab =  [[73.73, 19.20, 7.79],[70.94, 19.32, 8.28]] #left cheek


def dist(x, c, a):
    '''
    x와 c 사이의 거리를 구함.
    x : 인체 질의 색상(list : [skin[R,G,B], hair[R,G,B], eye[R,G,B]])
    c : 기준 색상(list : [skin[R,G,B], hair[R,G,B], eye[R,G,B]])
    a : 인체 부위별 가중치(list : [skin, hair, eye])
    '''
    distance = 0
    for body in range(3): #body = 0: skin, 1: hair, 2: eye
        diff = list(map(operator.sub, x[body], c[body]))
        distance += a[body] * sum(i*i for i in diff)
    return math.sqrt(distance)

def minDist(x, Ct, a):
    '''
    x와 계절 t에 대한 c집합 Ct 중 가장 짧은 거리를 구함.
    x : 인체 질의 색상(list : [skin[R,G,B], hair[R,G,B], eye[R,G,B]])
    c : 기준 색상(list : [skin[R,G,B], hair[R,G,B], eye[R,G,B]])
    C : 전체 계절에 대한 c들의 집합 list
    Ct : 계절 t에 대한 c들의 집합 list
    a : 인체 부위별 가중치(list : [skin, hair, eye])
    '''
    distance = []
    for c in Ct:
        distance.append(dist(x, c, a))
    return min(distance)

def probability(x, t, C, a):
    '''
    x의 특정 계절유형 t에 대한 소속도를 구함.
    x : 인체 질의 색상(list : [skin[R,G,B], hair[R,G,B], eye[R,G,B]])
    t : 특정 계절(int : 0: spring, 1: summer, 2: fall, 3: winter)
    c : 기준 색상(list : [skin[R,G,B], hair[R,G,B], eye[R,G,B]])
    C : 전체 계절에 대한 c들의 집합 list
    a : 인체 부위별 가중치(list : [skin, hair, eye])
    '''
    #분모
    denominator = 1/(sum(minDist(x, C[i], a) for i in range(4)))
    #분자
    numerator = 1/(minDist(x, C[t], a))

    return (numerator/denominator)


'''
for i in range(4):
    print(f'skin distance from {label[i]}')
    print('1 : ',distance.euclidean(skin[i], skin_lsg[0]))
    print('2 : ', distance.euclidean(skin[i], skin_lsg[1]))

    print(f'pupil distance from {label[i]}')
    print('1 : ',distance.euclidean(pupil[i], pupil_lsg[0]))
    print('2 : ', distance.euclidean(pupil[i], pupil_lsg[1]))
    print('3 : ', distance.euclidean(pupil[i], pupil_lsg[2]))
    print('4 : ', distance.euclidean(pupil[i], pupil_lsg[3]))
'''

'''
skin_dist = [[0,0,0,0], [0,0,0,0]]
pupil_dist = [[0,0,0,0] for _ in range(4)]

# i = seasons
for i in range(4):
    # skin
    for j in range(2):
    # j = 0 피부에서 가장 많은 색상과 각 계절과의 거리
    # j = 1 피부에서 두번째로 많은 색상과 각 계절과의 거리
        skin_dist[j][i] = distance.euclidean(skin[i], skin_lsg[j])

    # pupil
    for j in range(4):
        pupil_dist[j][i] = distance.euclidean(pupil[i], pupil_lsg[j])
# 거리가 짧은 순으로 정렬
# skin
sorted_skdist = copy.deepcopy(skin_dist)
sorted_ppdist = copy.deepcopy(pupil_dist)

for i in range(2):
    sorted_skdist[i].sort()
# pupil
for i in range(4):
    sorted_ppdist[i].sort()
print(skin_dist[0])
print(sorted_skdist[0])
print(pupil_dist[0])
print(sorted_ppdist[0])

# 거리가 짧은 계절 순으로 출력
# skin

for i in range(2):
    print('skin - round ', i)
    for season in range(4):
        print(f'{season+1}위:', label[skin_dist[i].index(sorted_skdist[i][season])])
print('\n')
# pupil
for i in range(4):
    print('pupil - round ', i)
    for season in range(4):
        print(f'{season+1}위:', label[pupil_dist[i].index(sorted_ppdist[i][season])])
'''


## Lab 색상
skin_dist_lab = [[0,0,0,0], [0,0,0,0]]
pupil_dist_lab = [[0,0,0,0] for _ in range(4)]

# i = seasons
for i in range(4):
    # skin
    for j in range(2):
    # j = 0 피부에서 가장 많은 색상과 각 계절과의 거리
    # j = 1 피부에서 두번째로 많은 색상과 각 계절과의 거리
        skin_dist_lab[j][i] = distance.euclidean(skin_lab[i], skin_lsg_lab[j])

# 거리가 짧은 순으로 정렬
# skin
sorted_skdist_lab = copy.deepcopy(skin_dist_lab)

for i in range(2):
    sorted_skdist_lab[i].sort()

print(skin_dist_lab[0])
print(sorted_skdist_lab[0])

# 거리가 짧은 계절 순으로 출력
# skin

for i in range(2):
    print('skin - round ', i)
    for season in range(4):
        print(f'{season+1}위:', label[skin_dist_lab[i].index(sorted_skdist_lab[i][season])])
print('\n')


# skin, hair, eye 순서
lee_seong_kyoung = [[222.5, 201.4, 188.9], [138.6, 98.4, 55.0], [159.8, 115.8, 61.7]]

print("******************")
a = [30, 20, 10]
spring = 0
summer = 1
fall = 2
winter = 3
print("이성경")
print("봄   : ", format(probability(lee_seong_kyoung, spring, C, a),".2f"), "%")
print("여름 : ", format(probability(lee_seong_kyoung, summer, C, a),".2f"), "%")
print("가을 : ", format(probability(lee_seong_kyoung, fall, C, a),".2f"), "%")
print("겨울 : ", format(probability(lee_seong_kyoung, winter, C, a),".2f"), "%")
print("******************")
