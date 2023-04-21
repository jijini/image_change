import cv2

# 이미지 파일 읽기
image = cv2.imread("D:\python\ex230421\hh.png")

# 흑백 이미지로 변환
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 이미지 화면에 보여주기
cv2.imshow("Gray Image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()