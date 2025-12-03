# **📚 CV_class_2025_2_Assignment_4**

이번 과제에서는 **Photometric Stereo(물체의 노말·알베도 추정)** 와**Plane Sweep Stereo(깊이 추정)** 의 핵심 파이프라인을 직접 구현하고 결과를 시각화하는 것을 목표로 합니다.

아래 과정을 따라 과제를 진행해주세요:D

과제 관련 문의가 있다면 아래 조교 메일로 연락해주세요.

- 최수영: csy010921@naver.com

---

## 🧩 **Project 4: Photometric Stereo + Stereo Matching**

이 프로젝트에서는 이번 프로젝트에서는 두 개의 독립적인 모듈을 구현하게 됩니다.

### 1) Photometric Stereo (PSData 사용)

제공된 물체 이미지들(frog, pig, scholar 등 여러 카테고리) 중 하나를 선택해 물체 표면의 **알베도(albedo)** 와 **법선(normals)** 을 추정합니다.

### 주요 목표

- 여러 조명 아래 촬영된 다수 이미지 로딩
- Lambertian Reflectance 기반 법선 벡터 계산
- Albedo 추정
- 노말 벡터 시각화
- 알베도 / 노말 결과 저장(`output/파일명.png`, `.npy`)

구현해야 할 함수들은 **student.py에만 TODO로 제공**됩니다.

### 2) Plane Sweep Stereo (Left–Right 뷰로 깊이 추정)

제공된 stereo 데이터셋(`input/left`, `input/right`)을 사용하여 여러 disparity 가설을 Sweep하여 깊이 맵을 추정합니다.

### 주요 목표

- Normalized Cross-Correlation(NCC) 계산
- Plane Sweep을 통해 최적 disparity 선택
- 3D 점들을 right view로 재투영해 align 시각화
- Depth 결과 저장(`output/파일명.png`, `.npy`)

---

## 🪜 **단계별 진행**

아래 단계들은 **`student.py`의 TODO**를 따라 Photometric Stereo 및 Plane Sweep Stereo의 핵심 기능을 구현하는 과정입니다.

1. **Photometric Stereo 구현 (TODO 1–2)**
    - 알베도(albedo) 계산
    - 노말(normals) 계산
2. **Stereo NCC 계산 (TODO 3)**
    - 좌·우 이미지 사이의 NCC 기반 매칭 비용 계산
3. **Plane Sweep (TODO 4)**
    - 여러 disparity 후보 중 최적의 값을 선택해 깊이맵 생성
4. **Right-view 투영 (TODO 5)**
    - 추정된 깊이맵을 이용해 left-view 이미지를 right-view로 재투영하여 검증

---

## 🚀 **실행 및 테스트 방법**

1. **Photometric Stereo 실행**
    - `photometric_stereo.py` 의 빈칸을 채운 후, 터미널에서 아래와 같이 명령어를 입력해 실행합니다.
        - 원하는 객체(category) 입력: `cat`, `frog`, `pig`, `scholar` 등을 입력해주세요.
        - 데이터셋은 `/Project4_Stereo/data/PSData` 경로에 위치해있습니다.
        - ex) `python photometric_stereo.py cat`
    - 결과 파일은 자동으로 `output/` 폴더에 저장됩니다.
        - `{category}_albedo.png`
          
          <img width="299" height="382" alt="image" src="https://github.com/user-attachments/assets/14ca44c6-6346-4211-b0a6-8b14719f6942" />
          
        - `{category}_normals.png`
          
          <img width="350" height="449" alt="image-2" src="https://github.com/user-attachments/assets/38781f5d-1b67-4662-835f-17aad19bbea2" />
        - `{category}_normals.npy`

2. **Stereo Matching 실행 → 레포트 작성**
    - `/Project4_Stereo/data/Flowers-perfect` 경로에 위치한 데이터셋을 사용합니다.
    - 터미널에 아래의 명령어를 입력해 `plane_sweep_stereo.py` 파일을 실행합니다.
        - `python plane_sweep_stereo.py Flowers`
    - 결과는 자동으로 `output/` 폴더에 저장됩니다.
        - `Flowers_depth.npy`
        - `Flowers_ncc.png`
          
          <img width="535" height="366" alt="image-3" src="https://github.com/user-attachments/assets/b438529f-f47f-4794-83cf-a5eb212d0028" />        
        - `Flowers_ncc.gif`
          
            ![Flowers_ncc](https://github.com/user-attachments/assets/c52a6477-6364-496a-bd82-2635807fe42f)
                
        - `Flowers_projected.gif`
          
            ![Flowers_projected](https://github.com/user-attachments/assets/fdfa4833-8a02-441b-bccf-451249f50c02)
            
3. **설명 PDF 작성**
    - 아래의 내용을 포함해 레포트를 1p 이내로 작성해주세요.
        - plane sweep이 어떤 원리인지 **자기 말로 요약**해 설명하세요.
        - NCC가 무엇인지 설명해주세요.
        - depth 결과를 분석해주세요.
            - ex) 가까운 영역은 왜 밝고 먼 영역은 어두운지
    - `output` 폴더에 pdf를 업로드 해주세요.
    - 제출 파일명
        - `학번.pdf`

---

## **과제 제출 총정리**

- 본 레포지토리를 자신의 컴퓨터로 **pull**한 뒤, `student.py`의 TODO 함수를 구현합니다.
- 구현 후, **output** 폴더 안에 아래 파일들을 추가되었는지 확인합니다. 아래 파일들이 필수적으로 포함되어 있어야합니다.
    - `{category}_albedo.png`
    - `{category}_normals.png`
    - `{category}_normals.npy`
    - `Flowers_depth.npy`
    - `Flowers_ncc.png`
    - `Flowers_ncc.gif`
    - `Flowers_projected.gif`
    - **개인 설명 PDF(**`학번.pdf`**)**
- 모든 파일을 추가한 뒤 **push**하면 과제 제출이 완료됩니다.
