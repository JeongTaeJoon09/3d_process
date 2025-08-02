2차시 업무 제출합니다.

3D Process : 2D → 3D 변환
이 실습은 OpenCV와 Python을 사용하여 2D 이미지를 3D 형태로 시각화하는 과정을 진행한 것 입니다.
Depth Map을 생성하고 이를 기반으로 3D 포인트 클라우드를 만들어 시각화했습니다.

1. 프로젝트 구조

3d_process/
│
├── _3d_process.py         # 2D → 3D 변환 알고리즘 구현
├── test_3d_process.py     # Unit Test 코드
├── sample_3d.jpg          # 샘플 이미지
├── depth_map.jpg          # 변환된 Depth Map
├── 3d_result.jpg          # 3D 변환 결과 이미지
└── README.md              # 프로젝트 설명 문서

2. 실행 방법

필요 라이브러리 : numpy, matplotlib, pytest
terminal 설치 : pip install opencv-python numpy matplotlib pytest

이미지 변환 실행 : python _3d_process.py

실행하면 depth_map.jpg (생성된 Depth Map) 과 3d_result.jpg (3D로 변환된 이미지)가 생성됩니다.
그리고, matplotlib 창에서 3D 포인트 클라우드가 표현되어 출력됩니다.

3. 테스트 실행

pytest로 테스트 할 수 있습니다. : pytest test_3d_process.py

예시 결과는 다음과 같습니다.
============================= test session starts =============================
collected 5 items

test_3d_process.py .....                                           [100%]

============================== 5 passed in 0.20s ==============================


