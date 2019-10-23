import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from skimage import io
from itertools import compress

class DominantColors:

    CLUSTERS = None
    IMAGE = None
    COLORS = None
    LABELS = None

    def __init__(self, image, clusters=3):
        self.CLUSTERS = clusters
        self.IMAGE = image

    def dominantColors(self):
        #read image
        #img = cv2.cvtColor(self.IMAGE, cv2.COLOR_BGR2RGB)
        #reshaping to a list of pixels
        self.IMAGE = img.reshape((img.shape[0] * img.shape[1], 3))

        #using k-means to cluster pixels
        kmeans = KMeans(n_clusters = self.CLUSTERS)
        kmeans.fit(self.IMAGE)

        #the cluster centers are our dominant colors.
        self.COLORS = kmeans.cluster_centers_
        self.LABELS = kmeans.labels_

        print(self.COLORS)

        return self.COLORS.astype(int)


    def rgb_to_hex(self, rgb):
        return '#%02x%02x%02x' % (int(rgb[0]), int(rgb[1]), int(rgb[2]))


    def plotClusters(self):
        #plotting
        fig = plt.figure()
        ax = Axes3D(fig)
        for label, pix in zip(self.LABELS, self.IMAGE):
            ax.scatter(pix[0], pix[1], pix[2], color = self.rgb_to_hex(self.COLORS[label]))
        plt.show()


    def plotHistogram(self):

        #labels form 0 to no. of clusters
        numLabels = np.arange(0, self.CLUSTERS+1)

        #create frequency count tables
        (hist, _) = np.histogram(self.LABELS, bins = numLabels)
        hist = hist.astype("float")
        hist /= hist.sum()

        #appending frequencies to cluster centers
        colors = self.COLORS

        #descending order sorting as per frequency count
        colors = colors[(-hist).argsort()]
        hist = hist[(-hist).argsort()]

        #creating empty chart
        chart = np.zeros((50, 500, 3), np.uint8)
        start = 0

        for i in range(self.CLUSTERS):
            colors[i][0] = int(colors[i][0])
            colors[i][1] = int(colors[i][1])
            colors[i][2] = int(colors[i][2])

        # Blue mask 제거
        fil = [colors[i][2] < 250 and colors[i][0] > 10 for i in range(self.CLUSTERS)]
        colors = list(compress(colors, fil))
        #creating color rectangles
        for i in range(len(colors)):
            end = start + hist[i] * 500

            #getting rgb values
            r = colors[i][0]
            g = colors[i][1]
            b = colors[i][2]

            #print(r,g,b)
            #using cv2.rectangle to plot colors
            cv2.rectangle(chart, (int(start), 0), (int(end), 50), (r,g,b), -1)
            start = end

        #display chart
        plt.figure()
        plt.axis("off")
        plt.imshow(chart)
        plt.show()

        return colors
