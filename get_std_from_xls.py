import pandas as pd

class ListFromExcel:

    df = None
    skin = None
    pupil = None
    hair = None

    def __init__(self, path):
        self.df = pd.read_excel(path, sheet_name='original')
        self.skin = pd.concat([self.df[1:5],self.df[9:13]]).values.tolist()
        self.pupil = pd.concat([self.df[19:21],self.df[25:27]]).values.tolist()
        self.hair = pd.concat([self.df[31:33],self.df[37:39]]).values.tolist()

    '''
    코드에서 [1:5],[9:13]이 skin 이며 [:][0:3]이 spring의 rgb라는 등의 상수는
    철저히 res/tone_color_standard.xlsx 파일 기준으로 작성된 것이며
    다른 엑셀 문서에 대해서는 아래 함수가 작동하지 않을 수 있다.
    만약 엑셀에 새로운 기준값을 추가하는 등의 변동사항이 생기면
    이 코드 상의 상수도 적절히 변경해주어야 한다.

    이 파이썬 코드는
    엑셀에 정리된 색상 기준 값을 list로 변환하기 위해 작성되었으며
    리스트는 아래와 같이 이루어져있다.
    [standard_1[spr[r,g,b], smr[r,g,b], fal[r,g,b], wnt[r,g,b]],
     standard_2[spr[r,g,b], smr[r,g,b], fal[r,g,b], wnt[r,g,b]],
     standard_3[spr[r,g,b], smr[r,g,b], fal[r,g,b], wnt[r,g,b]],
     ...
     standard_n[spr[r,g,b], smr[r,g,b], fal[r,g,b], wnt[r,g,b]]]
    여기서 r,g,b 대신 [v,c]가 들어갈 수도, [l,a,b]가 들어갈 수도 있다.
    '''

    # RGB values
    def get_rgb(self, list):
        ret_list=[]
        for i in range(len(list)):
            ret_list.append([list[i][0:3], list[i][9:12],
                            list[i][18:21], list[i][27:30]])
        return ret_list

    # VC values from HVC color space
    def get_vc(self, list):
        ret_list=[]
        for i in range(len(list)):
            ret_list.append([list[i][3:5], list[i][12:14],
                            list[i][21:23], list[i][30:32]])
        return ret_list

    # Lab values
    def get_lab(self, list):
        ret_list=[]
        for i in range(len(list)):
            ret_list.append([list[i][5:8], list[i][14:17],
                            list[i][23:26], list[i][32:35]])
        return ret_list

    def convert_list(self, skin_list, hair_list, eye_list):
        '''
        skin[standard_1[spr[r,g,b], smr[r,g,b], fal[r,g,b], wnt[r,g,b]],
            standard_2[spr[r,g,b], smr[r,g,b], fal[r,g,b], wnt[r,g,b]],
            ...
            standard_n[spr[r,g,b], smr[r,g,b], fal[r,g,b], wnt[r,g,b]]],
        hair[], eye[]

        를 아래와 같이 변환
        spr[standard_1[skin[R,G,B], hair[R,G,B], eye[R,G,B]],
            ...
            standard_n[skin[R,G,B], hair[R,G,B], eye[R,G,B]]],
        smr[standard_1[skin[R,G,B], hair[R,G,B], eye[R,G,B]],
            ...
            standard_n[skin[R,G,B], hair[R,G,B], eye[R,G,B]]],
        ...
        wnt[standard_1[skin[R,G,B], hair[R,G,B], eye[R,G,B]],
            ...
            standard_n[skin[R,G,B], hair[R,G,B], eye[R,G,B]]]]
        주의: 매개변수 skin_list, hair_list, eye_list 길이 같아야 함
        '''
        ret = []
        temp = []
        for s in range(4): #season
            for i in range(len(skin_list)): #standard
                temp.append([skin_list[i][s], hair_list[i][s], eye_list[i][s]])
            ret.append(temp)
            temp = []
        return ret
