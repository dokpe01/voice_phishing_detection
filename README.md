# Voice Phishing Dectection (작성중)


# 1. Project Overview (프로젝트 개요)
none


# Project Plan (프로젝트 계획)
none

<br/>
<br/>

# 2. Members (팀원 소개)
| 허성욱 | 이경민 | 김나영 | 김정안 |
|:------:|:------:|:------:|:------:|
| [GitHub](https://github.com/dokpe01) | None | None |  None |

<br/>
<br/>

# 3. Key Features (주요 기능)
- **대화 맥락 탐지**:
  - 한국어가 사전 학습된 모델 `Kanana 1.5` 에 전이학습을 진행하고, 의심키워드에 가중치 부여
  - 통화 내용이 보이스피싱이라고 의심되는 지 전체 대화 맥락을 탐지

- **딥보이스 탐지**:
  - 정상적인 사람의 대화 음성과 부자연스러운 사람의 대화 음성을 구분
  - 결정 임계치를 초과할 경우 딥보이스라고 판단
 
- **실시간 분석 후 경고**:
  - 모델 자체를 앱에 내장할지 의논 중
  - 내장할 경우, 통화 내용이 외부로 유출될 가능성을 방지할 수 있음
  - 앱이 무거워짐
 
- **사후 관리**:
  - `PostgreSQL` RDMBS를 구축하여 보이스피싱과 관련된 정보를 저장하여 반복적인 피해를 방지하도록 구현


<br/>
<br/>

# 4. Tasks & Responsibilities (역할 분담)
|  |  |  |
|-----------------|-----------------|-----------------|
| 허성욱 | `팀장` | <ul><li> 프로젝트 총괄 </li><li> 대화 맥락 탐지 모델 개발 <li> 딥보이스 탐지 모델 개발 </li></ul> |
| 이경민 | `팀원` | <ul><li> 앱 개발 <li> 데이터베이스 설계 및 구축 </li></ul> |
| 김나영 | `팀원` | <ul><li> 데이터 분석 </li><li> 자연어 데이터 전처리 </li> </ul>  |
| 김정안 | `팀원` | <ul><li> 딥러닝 학습 데이터 크롤링 </li><li> 자연어 데이터 전처리 </li></ul>  |

<br/>
<br/>

# 5. Technology Stack (사용 기술)
|  |  |
|-----------------|-----------------| 
| Fast-API |  |
| PostgreSQL |  |
| Android Studio | | 
| Flutter |  |
| Pytorch |  |
| Tensorflow |  |
| Whisper |  |
| Kanana base 1.5 (2.1B) |  |
| MFCC |  |
| BS4 / Selenium |  |
| Git / GitHub |  |
| Google Sheet |  |


<br/>
<br/>

# 6. Project Structure (프로젝트 구조)
```plaintext
project/
├── Server/
├── Model/
└── ?
```

<br/>
<br/>

# 7. App Features (앱 기능)
none

    
<br/>
<br/>
