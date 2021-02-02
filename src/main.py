from personal_color_analysis import personal_color
import argparse # 인자값을 받아 처리하는 argparse
# arg( 인자 ) +  parse( 구문 분석 )
# import argarse
# 
import os
import re


def main():
    # 위치 인자값 받을 인스턴스 생성,
    parser = argparse.ArgumentParser(description = 'Please input your image.')

    # 입력받을 인자값 등록
    parser.add_argument('--image', required = False, help='input .jpg or .png file')
    parser.add_argument('--dir', required = False, help='input image directory')

    # 입력받은 인자값을 args에 저장
    args = parser.parse_args()

    ##################################
    #         a single image         #
    ##################################
    # os.path -- 일반적인 경로명 조작
    # 이 모듈은 경로명에 유용한 함수를 구현한다.
    # os.path.abspath(path) 경로명 path의 정규화된 절대 버전을 반환
    print(os.path.abspath(os.path.curdir))

    find_regex = r'^([A-Z]:)?[\\|\/]'
    if args.image != None:
        path = args.image
    ##################################
    #  multiple images in directory  #
    ##################################
    elif args.dir != None:
        path = args.dir
    else:
        return
    
    if re.search(find_regex, path) is None:
        path = os.path.join(os.path.curdir, path)
    print(os.path.abspath(path)) # 절대 경로 확인
    if os.path.isdir(path):
        for img in os.listdir(path):
            if not (img.lower().endswith(".png") or img.lower().endswith(".jpg")):
                continue
            personal_color.analysis(os.path.join(path, img)) #personal_color.analysis에 전달

# __name__은 호출해서 사용한 모듈의 이름을 저장하는 변수
# 프로그램들에게 해당 파일이 모듈로서가 아닌 파일로서 실행될 때만 코드를 실행
if __name__ == '__main__':

    main()
