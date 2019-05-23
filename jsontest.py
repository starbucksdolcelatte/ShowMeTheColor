import json

def get_standard(filename):
    with open(filename, mode='r') as f:
        json_data = json.load(f)

    # 아래와 같은 계절별 기준값이 들어갈 리스트
    result_list = [[[],[]],[[],[]],[[],[]],[[],[]]]
    '''
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
    '''

    # iterate over each dictionary in our list
    i = 0
    j = 0
    for season in json_data:
        for std in json_data[season]:
            for body_part in json_data[season][std]:
                result_list[i][j].append(json_data[season][std][body_part])
            j += 1
        i += 1
        j = 0

    print(result_list)  # ['Hurzuf', 'Novinki']
get_standard('standard.json')
