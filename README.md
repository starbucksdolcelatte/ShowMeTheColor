# Show me the color
This is Personal color diagnosis system.

[![Personal Color Diagnosis system](http://img.youtube.com/vi/K7esg_dXYGo/0.jpg)](http://www.youtube.com/watch?v=K7esg_dXYGo "Personal Color Diagnosis system")
<br>**Click this image to see the Demo video!**
## Caution
This source code only covers personal color diagnosis. It doesn't have web framework, white balance adjust, and virtual makeup code. It is because I only contributed the personal color diagnosis feature in this team project!
이 소스코드는 퍼스널 컬러 진단 기능만 다룹니다. 데모에서 보여드린 것처럼 웹 프레임워크나 화이트 밸런스 조정 기능, 그리고 가상 메이크업 시뮬레이션 코드는 없습니다. 팀 프로젝트에서 제 파트가 아니었거든요!

## Usage
First of all, `git clone` to download the source code.

`cd src`
- Analysis a single image<br>
`python main.py --image IMAGEPATH`
- Analysis multiple images in a directory<br>
`python main.py --dir DIRECTORYPATH`<br>

 You have to install `imutils` and `opencv`, `dlib` packages.

먼저 `git clone` 을 통해 다운로드 받습니다.
`cd src` 
- 사진 한개의 퍼스널컬러 진단하기<br>
`python main.py --image IMAGEPATH`
- 여러 개의 사진이 담긴 디렉토리 한꺼번에 진단하기<br>
`python main.py --dir DIRECTORYPATH`<br>

 `imutils` 와 `opencv`, `dlib` packages를 설치해야 합니다. (pip install)



## 1. Face detection
`detect_face.py` using `shape_predictor_68_face_landmarks.dat` has DetectFace class, and it provides face detection function, the exact face parts, and the coordinates of them. We selected cheeks, eyes, eyebrows(instead of hair) for personal color analysis.<br><br>
`shape_predictor_68_face_landmarks.dat` 를 사용하는 `detect_face.py`에는 DetectFace 클래스가 있으며, 얼굴 감지 기능, 정확한 얼굴 부분 및 좌표를 제공합니다. 퍼스널컬러 분석을 위해 뺨, 눈, 눈썹 (머리카락 대신)을 선택했습니다.

## 2. Extract the Dominant Color
`color_extract.py` has DominantColors class, and it provides the dominant colors by k-means clustering algorithm, with RGB values.<br>I adopted the source code from (https://buzzrobot.com/dominant-colors-in-an-image-using-k-means-clustering-3c7af4622036) and modified it.<br><br>
`color_extract.py`에는 DominantColors 클래스가 있으며 RGB 값을 사용하여 k-means clustering 알고리즘으로 대표 색상을 제공합니다. (https://buzzrobot.com/dominant-colors-in-an-image-using-k-means-clustering-3c7af4622036)에서 얻은 소스 코드를 수정했습니다.

## 3. Personal Color Diagnosis
The RGB values are converted to Lab and HSV color space. The b value from Lab is the factor **determining warm/cool** and the S value from HSV is the factor **determining spring/fall or summer/winter**. Our team got the criteria values which classifies the personal color results by analyzing color values dataset from several images.
<br>`tone_analysis.py` is the source code for personal color classifying.<br><br>
RGB 값은 Lab 및 HSV 색 공간으로 변환됩니다. Lab의 b 값은 **따뜻한 / 차가움**을 결정하는 요소이고 HSV의 S 값은 **봄 / 가을 또는 여름 / 겨울을 결정하는 요소**입니다. 우리 팀은 여러 이미지의 색상 값 데이터 세트를 분석하여 퍼스널 컬러를 분류하는 기준 값을 얻었습니다.
<br>`tone_analysis.py`는 퍼스널 컬러 분류를 위한 소스 코드입니다.

## 4. Virtual Makeup Simulator
We classified several lipsticks as 4 personal colors by their colors and put their name, color code and class into the Database. After detecting the lip outlines, the system connects the lips and puts the chosen color from the DB.<br><br>

우리는 몇 가지 립스틱을 색상을 기준으로 4 가지 퍼스널 컬러로 분류하고 이름, 색상 코드 및 클래스를 데이터베이스에 넣었습니다. 입술 외곽선을 감지 한 후 점들을 연결하고 DB에서 선택한 색상을 넣습니다.

## 5. Web
Django is used for web framework.
웹 프레임워크로 장고를 사용했습니다.