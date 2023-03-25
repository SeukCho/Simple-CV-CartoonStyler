# Simple CV CartoonStyler
# 주석은 ChatGPT Example (chatgptexample.py) 비교 위주

import cv2 as cv

img = cv.imread('Lenna.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 5)

edges = cv.Laplacian(gray, cv.CV_8U, ksize=5)
# 엣지 검출을 위해 Lapllacian 필터를 사용함.
# Adaptive Thresholding은 조명 변화에 덜 민감하다고 함.
# 여기서는 수업시간에 배운 Laplacian Filter를 활용함.

edges = 255 - edges
color = cv.bilateralFilter(img, 9, 300, 300)
cartoon = cv.bitwise_and(color, color, mask=edges)

# 카툰 필터 강도를 조절할 수 있도록 트랙바를 생성
filter_strength = 1.0
def on_change_strength(value):
    global filter_strength
    filter_strength = value / 10.0

cv.namedWindow('Cartoonizer')
cv.createTrackbar('Strength', 'Cartoonizer', 10, 20, on_change_strength)

while True:
    # 필터 강도 조절하기
    filtered = None
    if filter_strength > 0:
        filtered = cv.edgePreservingFilter(cartoon, flags=1, sigma_s=60, sigma_r=0.6/filter_strength)
    # edgePreservingFilter 함수를 이용해 엣지 정보를 보존하고
    # 필터 강도에 따라 이미지의 블러 처리를 조절함

    if filtered is not None:
        filtered = cv.resize(filtered, (img.shape[1], img.shape[0]))
        final_image = cv.hconcat([img, filtered]) #원본, 필터 이미지
    else:
        final_image = cv.hconcat([img, img]) #원본 이미지만 2개

    cv.imshow('Cartoonizer', final_image)

    # 키보드 입력 받기
    key = cv.waitKey(1)
    if key == ord('+'): # + 버튼으로 필터 세기 증가
        if filter_strength < 2.0: # 2(20)일때는 더 증가하지 않도록
            filter_strength += 0.1
        cv.setTrackbarPos('Strength', 'Cartoonizer', int(filter_strength*10))
    elif key == ord('-'): # - 버튼으로 필터 세기 감소
        if filter_strength > 0: # 0일때는 더 감소하지 않도록
            filter_strength -= 0.1
        cv.setTrackbarPos('Strength', 'Cartoonizer', int(filter_strength*10))
    elif key == 27: # ESC 키를 누르면 종료
        break

cv.destroyAllWindows()