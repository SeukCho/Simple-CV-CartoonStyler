# Simple-CV-CartoonStyler
OpenCV를 활용한 간단한 카툰 필터 적용하기.

[사용법]
  > 스페이스바 : 일시정지 / 재생 토글   
  > \> : 배속 빠르게   
  > < : 배속 느리게   
  > Tab : 1배속   
  > [ : 10프레임 전으로   
  > ] : 10프레임 후로   
  > **r : 역재생**   

[기존 Video Player + Navigation](https://github.com/mint-lab/cv_tutorial/blob/master/video_player%2Bnavigation.py) 에 역재생 기능을 추가했습니다.      

![1](https://user-images.githubusercontent.com/74591896/223985583-27975138-2dda-4f96-9dbe-68b6a4460e0e.png)

역재생중에는 Speed가 -1로 표시되며 일시정지는 토글 할 수 있습니다.   
0프레임에 도달하면 자동으로 역재생이 종료되고 즉시 정재생하게 됩니다.   
역재생중에는 스피드를 변경할 수 없으며 역재생 토글 시 스피드는 1로 초기화됩니다.
