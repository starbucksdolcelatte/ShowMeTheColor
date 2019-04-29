from scipy.spatial import distance
import copy
# RGB based standard
# list[0] = spring, [1] = summer, [2] = fall, [3] = winter
label = ['spring', 'summer', 'fall', 'winter']
skin = [[197, 159, 140], [200, 164, 150], [195, 156, 138], [204, 168, 156]]
pupil = [[157, 92, 18], [145, 112, 28], [134, 96, 3], [136, 101, 10]]
hair = [[152, 103, 47], [95, 82, 81], [121, 87, 66], [85, 64, 67]]

# 이성경(res/lees.jpg) dominant colors by order of histogram
skin_lsg = [[222.5, 201.4, 188.9], [227.2, 209.5, 203.3]] # left cheek
pupil_lsg = [[159.8, 115.8, 61.7], [186.5, 156.1, 129.0],
             [126.0, 77.5, 42.8], [88.1, 41.1, 20.9]] # right eye

skin_lab = [[87.39, -2.18, 16.21],[84.48, 0.75, 14.23],[80.58, -0.07, 25.46],[91.47, -0.73, 9.96]]
skin_lsg_lab =  [[73.73, 19.20, 7.79],[70.94, 19.32, 8.28]] #left cheek
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
