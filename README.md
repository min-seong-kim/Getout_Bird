# 🧑‍🌾 안.농.하세요 (안전한 농가 하세요)
### Khuthon 2025 – 농업의 기술화 / DKU Team 돌아가면_냅두자

> - 영상/음성 인식 AI 기술 기반 조류 퇴치 자동화 시스템
> - 기존 조류퇴치기의 한계점을 극복
> - 실시간으로 새를 식별하고, 식별된 종별로 맞춤형 사운드를 출력하여 농작물 피해를 줄인다.

## 🐤 팀원 소개
팀 소개 – 돌아가면_냅두자
- 👨🏻 김민성 (DB 설계, 영상 인식 처리)
- 👩🏻 위다연 (Frontend, 영상 인식 처리)
- 👨🏻 이용민 (서버 설계, 음성 인식 처리)
- 👩🏻 박주희 (기획, 음성 출력 처리)

## 📌 프로젝트·서비스 소개 
- ?? 기반 영상 인식과 BirdNET 기반 음성 분석을 활용
- 농작물에 피해를 주는 유해 조류를 실시간으로 자동 식별하는 스마트 퇴치 솔루션.

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
- 종별 맞춤 퇴치 사운드 출력


## ⚙️ 기술 스택
 – 기술 스택 정리
구성 요소	기술 / 도구	역할
- 🎥 카메라	일반 디지털 카메라 (Canon 등)	영상 스트리밍 / 이미지 캡처
- 🎤 마이크	USB 마이크	실시간 음성 녹음
- 📡 통신	Python socket	클라이언트-서버 간 영상/음성 전송
- 🧠 외부 AI API	Roboflow	이미지 기반 실시간 조류 탐지
- 🧠 외부 AI 분석기	BirdNET-Analyzer	조류 소리 기반 종 분석
- 🖥️ 서버	Python + Flask / FastAPI	API 연동, 퇴치 판단, 출력 제어
- 🔊 스피커	-	조류별 퇴치 사운드 재생
- 🗃 데이터 저장	(선택) SQLite / CSV 로그	조류 감지 로그 기록, 분석용
- 🌐 프론트	웹 대시보드


## 🔎 ERD

## 📱 화면 구성

## ⚠️ Constraints

## 🌱 확장 가능성

## 📄 참고자료
- 정책 자료: https://www.mafra.go.kr/bbs/home/792/572965/artclView.do
- Nonlethal Bird Deterrent Strategies: Methods for reducing fruit crop losses in Oregon.

