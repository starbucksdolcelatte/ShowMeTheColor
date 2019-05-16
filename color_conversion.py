from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color

#sRGB 클래스 인스턴스 생성. RGB 값을 넣을 때 is_upscaled=True로 해줘야 함
rgb = sRGBColor(222.5, 201.4, 188.9, is_upscaled=True)
print(rgb)
#lab로 변환. through_rgb_type=sRGBColor 로 넣어준다.(AdobeRGBColor클래스 사용 X)
lab = convert_color(rgb, LabColor, through_rgb_type=sRGBColor)
print(lab)
