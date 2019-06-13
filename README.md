# Show me the color
This is Personal color diagnosis system.

[![Personal Color Diagnosis system](http://img.youtube.com/vi/K7esg_dXYGo/0.jpg)](http://www.youtube.com/watch?v=K7esg_dXYGo "Personal Color Diagnosis system")
<br>**Click this image to see the Demo video!**

## 1. Face detection
`detect_face.py` with `shape_predictor_68_face_landmarks.dat` has DetectFace class, and it provides face detection function, the exact face parts, and the coordinates of them. We selected cheeks, eyes, eyebrows(instead of hair) for personal color analysis.

## 2. Extract the Dominant Color
`dominant_colors.py` has DominantColors class, and it provides the dominant colors by k-means algorithm, with RGB values.<br>I modified the source code from (https://buzzrobot.com/dominant-colors-in-an-image-using-k-means-clustering-3c7af4622036).


## 3. Personal Color Diagnosis
The RGB values from step 2 is converted to Lab and HSV color space. The b value from Lab is the factor **determining warm/cool** and the S value from HSV is the factor **determining spring/fall or summer/winter**. Our team got the criteria values which classifies the personal color results by analyzing color values dataset from several images.
<br>`tone_analysis.py` and `temp5.py` is the source code for personal color classifying and the usage.

## 4. Virtual Makeup Simulator
We classified several lipstics as 4 personal colors by their colors and put their name, color code and class into the Database. After detecting the lip outlines, the system connects the lips and puts the chosen color from the DB.

## 5. Web
Django is used for web framework.
