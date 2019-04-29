import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plotStd(arr):
    season_label = ['spring', 'summer', 'fall', 'winter']
    season_color = ['green', 'blue', 'red', 'gray']
    fig = plt.figure()
    ax = Axes3D(fig)
    for seasons in arr:
        i = 0
        for s in seasons:
            ax.scatter(s[0], s[1], s[2], label = season_label[i], color = season_color[i])
            i += 1
    ax.set_xlabel('L value')
    ax.set_ylabel('a value')
    ax.set_zlabel('b value')
#    plt.xlabel('L value')
#    plt.ylabel('a value')
#    plt.zlabel('b value')
    plt.show()

#[봄여름가을겨울]*5개의 기준
skin_lab = [[[87.39, -2.2, 16.21],
            [84.48, 0.75, 14.23],
            [80.58, -0.1, 25.46],
            [91.47, -0.7, 9.96]],
           [[84.57, -0.21, 28.38],
            [84.81, 6.59, 19.93],
            [73.88, 2.55, 20.96],
            [89.53, 0.74, 12.14]],
           [[79.84, 11.02, 33.65],
            [83.7, 5.53, 17.71],
            [75.69, 4.55, 27.02],
            [81.76, 14.12, 29.2]],
           [[81.8, 6, 34.05],
            [82.88, 10.99, 26.24],
            [72.75, 3.2, 38.52],
            [73.82, 8.42, 27.3]],
		   [[83.4, 3.6575, 28.0725],
            [83.9675, 5.965, 19.5275],
            [75.725, 2.5575, 27.99],
            [84.145, 5.6375, 19.65]]]

plotStd(skin_lab)
