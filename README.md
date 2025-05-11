![image](https://github.com/user-attachments/assets/2bf2fe77-69e4-4234-b171-7b6939fcb18b)# 🧑‍🌾 안.농.하세요 (안전한 농가 하세요)
### Khuthon 2025 – 농업의 기술화 / DKU Team 돌아가면_냅두자
> - https://thon.khlug.org/about/2025

> - 영상/음성 인식 AI 기술 기반 조류 퇴치 자동화 시스템
> - 기존 조류퇴치기의 한계점을 극복
> - 실시간으로 새를 식별하고, 식별된 종별로 맞춤형 사운드를 출력하여 농작물 피해를 줄인다.
---
## 서비스 화면 
![Image](https://github.com/user-attachments/assets/f5ccf4b4-12a0-494d-ac73-29898cac0f35)
---
## 🐤 팀원 소개
팀 소개 – 돌아가면_냅두자
- 👨🏻 김민성 (DB 설계, 영상 인식 처리)
  - kms0509@dankook.ac.kr
- 👩🏻 위다연 (UI, 영상 인식 처리)
  - wida10@dankook.ac.kr 
- 👨🏻 이용민 (서버 설계, 음성 인식 처리)
  - 32203349@dankook.ac.kr 
- 👩🏻 박주희 (기획, 음성 출력 처리)
  - pjuhee23@dankook.ac.kr 

## 📌 프로젝트·서비스 소개 
- Roboflow 기반 영상 인식과 BirdNET 기반 음성 분석을 활용
- 농작물에 피해를 주는 유해 조류를 실시간으로 자동 식별하는 스마트 퇴치 솔루션

- 현재 식별 대상은 4종의 주요 유해조수: 멧비둘기 (Rock-pigeon), 참새 (Sparrow), 까치 (Magpie), 까마귀 (Crow)

- 감지된 조류의 종류에 따라 각 종이 혐오 반응을 보이는 주파수의 퇴치음을 출력하여
효율적으로 작물 피해를 방지
  - Refernece: Nonlethal Bird Deterrent Strategies: Methods for reducing fruit crop losses in Oregon (Scott B Lukas, 2020)​ 종-특이적 주파수 관련 연구
- 시스템은 영상과 음성을 클라이언트 장치에서 수집한 뒤 서버로 전송
- 서버는 외부 AI 분석 도구(Roboflow, BirdNET)를 통해 종 판단
- 판단 결과에 따라 해당 종에 적합한 퇴치 사운드(Bird-deterrent sound​)를 스피커를 통해 재생
 

## ✅ 구현 범위
 

## 🍎 주요 기능
- 실시간 조류 식별 (영상/음성 동시 분석)
- 웹 사이트에 움직임 감지 시 전송된 실제 프레임과 분석 이후의 프레임 출력
- 웹 사이트에 조류 음성 감지 시 전송된 실제 음성 파일과 퇴치 사운드 출력
- 종 별 맞춤 퇴치 사운드 출력


## ⚙️ 기술 스택
 – 기술 스택 정리
구성 요소	기술 / 도구	역할
- 🎥 카메라 -	영상 촬영이 가능한 디지털 카메라 (Canon 등)	영상 스트리밍 / 이미지 캡처
- 🎤 마이크 - USB 마이크	실시간 음성 녹음
- 📡 통신 - Python socket	클라이언트-서버 간 영상/음성 전송
- 🧠 외부 AI API - 영상	Roboflow	이미지 기반 실시간 조류 탐지
- 🧠 외부 AI 오픈소스 - 음성 분석기	BirdNET-Analyzer	조류 소리 기반 종 분석
- 🖥️ 서버 - Python + Flask / FastAPI	API 연동, 퇴치 판단, 출력 제어
- 🔊 스피커	-	조류별 퇴치 사운드 재생
- 🗃 데이터 저장 - 서버 스토리지
- 🌐 프론트	- React 사용


## 📄 참고자료
- 정책 자료: https://www.mafra.go.kr/bbs/home/792/572965/artclView.do
- Nonlethal Bird Deterrent Strategies: Methods for reducing fruit crop losses in Oregon.

