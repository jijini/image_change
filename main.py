import cv2

# 이미지 파일 읽기
image = cv2.imread("D:\python\ex230421\hh.png")

# 흑백 이미지로 변환
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 변환된 이미지 저장
cv2.imwrite("gray_image.jpg", gray_image)