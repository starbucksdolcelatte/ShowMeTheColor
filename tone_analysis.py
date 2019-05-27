from scipy.spatial import distance
import copy
import math
import operator

class ToneAnalysis:
    def dist(self, x, c, a):
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

    def minDist(self, x, Ct, a):
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
            distance.append(self.dist(x, c, a))
        return min(distance)

    def probability(self, x, t, C, a):
        '''
        x의 특정 계절유형 t에 대한 소속도를 구함.
        x : 인체 질의 색상(list : [skin[R,G,B], hair[R,G,B], eye[R,G,B]])
        t : 특정 계절(int : 0: spring, 1: summer, 2: fall, 3: winter)
        c : 기준 색상(list : [skin[R,G,B], hair[R,G,B], eye[R,G,B]])
        C : 전체 계절에 대한 c들의 집합 list
        a : 인체 부위별 가중치(list : [skin, hair, eye])
        '''
        print(t)
        print(C[t])
        #분모
        denominator = sum((1/self.minDist(x, C[i], a)) for i in range(4))
        #분자
        numerator = 1/(self.minDist(x, C[t], a))
        return (numerator/denominator)*100

    def is_warm(self, lab):
        if (lab[1] >= lab[2]):
            return 0 #cool
        else:
            return 1 #warm
