# Simple-CV-Cartoonizer
OpenCV를 활용한 간단한 카툰 필터 적용하기.

[사용법]
  > 상단의 바로 필터 강도 변경   
  > +, - 키로 동일한 기능 수행   
  > ESC 키로 종료


![1](https://user-images.githubusercontent.com/74591896/227714300-f5768b2b-b4eb-4005-8dbd-e0310d4b0d55.png)

예시로 사용한 Lenna.png 에 적용한 모습

ChatGPT가 제안한 코드와의 차이점(scvcs.py 내 주석으로도 설명)
1. Adaptive Thresholding 대신 수업 시간에 다뤘던 Laplacian 필터를 사용함    
2. 카툰 필터 강도를 조절할 수 있도록(엣지는 유지하고, 이미지에 블러를 여러 세기로 적용) 트랙바와 키보드 입력 받는 기능 추가   
이때 최대값과 최솟값(0, 2.0) 에서의 예외처리를 적용 
