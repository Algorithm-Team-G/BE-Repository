# Algorithm Term Project (Team G)

> 가천대학교 AI소프트웨어학과 알고리즘 강의 Term Project용 Repository

---

## Overview

### 조직 내 업무 분배 서비스

조직에서 어떠한 프로젝트를 진행함에 있어서 필요한 업무를 적절한 작업자에게 할당해 준다.

> \* **주의**  
> 해당 프로젝트는 임의의 조직과 업무를 가정하고 시뮬레이션하는 것이다.
> 때문에 몇 가지 제약조건이 존재한다.
> 1. 해당 서비스는 조직의 PM만 이용할 수 있다고 전제를 둔다.
>    때문에, 회원 시스템이 존재하지 않는다.
> 2. 조직의 팀과 직군, 업무 등을 사전에 정의해서 데이터셋을 제작했다.
>    따라서 정의된 것 외의 정보는 취급하지 못한다.

### 활용한 알고리즘

**Hungarian Algorithm**

Bipartital Graph에서 서로 다른 그룹의 두 노드를 매칭시키는 알고리즘으로, '작업 할당', '남녀 매칭' 등의 작업을 처리함에 있어서 효과적이다.

> **Basic Conception**
> - Graph Theory
> - Greedy Algorithm

<br>

\* 해당 레포지토리의 `Hungarian.py`는 아래 링크의 코드를 가져와 서비스에 맞게끔 커스터마이징하였다:  
[(네이버 블로그) [Python] 헝가리안 알고리즘 - 배분문제, 카이](https://m.blog.naver.com/solar767/222755686519)

<br>

---

## Project Architecture

(대중적인 시스템 아키텍처를 기반으로 구성함)

```
~(root)
├ common
│ └ Config.py                   # 애플리케이션의 전역 설정을 관리하는 파일. 환경 변수 및 기본 설정을 포함.
├ controller
│ ├ TaskController.py           # 작업 관련 API 요청을 처리하는 컨트롤러. 클라이언트의 요청을 받고, 서비스와 연결하여 응답을 반환.
├ ddl
│ ├ algorithm_ddl.txt           # 데이터베이스 테이블 구조를 정의하는 DDL(Data Definition Language) 스크립트.
│ └ algorithm_example.xlsx      # 알고리즘 예시 데이터가 포함된 Excel 파일. 데이터 샘플 제공.
├ dto
│ ├ request
│ │ ├ TaskDTO.py                # 클라이언트로부터 받은 작업 관련 데이터 전송 객체. 요청 시 필요한 필드 정의.
│ │ └ WorkerTasksDTO.py         # 근무자와 관련된 작업 요청 데이터를 정의하는 DTO.
│ └ response
│   └ UnassignedTaskDTO.py      # 할당되지 않은 작업에 대한 응답 데이터 전송 객체. 클라이언트에 반환되는 데이터 형식 정의.
├ entity
│ ├ Job.py                      # 작업(Job) 엔티티 클래스. 데이터베이스의 Job 테이블에 매핑되는 모델.
│ ├ Task.py                     # 작업(Task) 엔티티 클래스. 데이터베이스의 Task 테이블에 매핑되는 모델.
│ ├ Team.py                     # 팀(Team) 엔티티 클래스. 데이터베이스의 Team 테이블에 매핑되는 모델.
│ ├ Worker.py                   # 근무자(Worker) 엔티티 클래스. 데이터베이스의 Worker 테이블에 매핑되는 모델.
│ └ WorkerTaskCount.py          # 근무자 작업 수를 추적하는 엔티티 클래스. 근무자의 작업 수와 관련된 데이터 모델.
├ exception
│ ├ HttpException.py            # HTTP 관련 예외 처리를 위한 클래스. API 요청 중 발생할 수 있는 HTTP 예외를 정의.
│ └ ValueException.py           # 값 관련 예외 처리를 위한 클래스. 잘못된 값이 입력될 때 발생하는 예외 정의.
├ repository
│ ├ TaskRepository.py           # 작업 데이터베이스 접근을 담당하는 레포지토리 클래스. CRUD 연산을 포함.
│ ├ TeamRepository.py           # 팀 데이터베이스 접근을 담당하는 레포지토리 클래스. CRUD 연산을 포함.
│ └ WorkerRepository.py         # 근무자 데이터베이스 접근을 담당하는 레포지토리 클래스. CRUD 연산을 포함.
├ service
│ └ TaskService.py              # 작업 관련 비즈니스 로직을 처리하는 서비스 클래스. 데이터베이스와의 상호작용 관리.
├ test
│ └ test.py                     # 테스트 코드가 포함된 파일. 각 기능의 단위 테스트 및 통합 테스트 수행.
├ utils
│ ├ DB.py                       # 데이터베이스 연결 및 쿼리 실행을 위한 유틸리티 클래스. DB 관련 기능 제공.
│ ├ DateFormat.py               # 날짜 형식 변환을 위한 유틸리티 클래스. 날짜 및 시간 관련 기능 제공.
│ ├ Graph.py                    # 그래프 관련 알고리즘 구현을 위한 유틸리티 클래스. 알고리즘 처리 기능 제공.
│ └ Hungarian.py                # 헝가리안 알고리즘 구현을 위한 유틸리티 클래스. 최적화 문제 해결 기능 제공.
└ main.py                       # 애플리케이션의 진입점. 서버를 시작하고 초기 설정을 로드하는 파일.
```

<br>

---

## API 명세서

| Title                     | HTTP Method | API Path               | Request                                                                                           | Response                                                                                                              | Status Code                | Description                                                                                      |
|---------------------------|-------------|------------------------|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|----------------------------|--------------------------------------------------------------------------------------------------|
| 분배된 업무 불러오기       | GET         | /task/assign           | | { teamId }: { "name": <string\>, "workers": { {workerId}: { "name": <string\>, "tasks": [ { "id": <int\>, "title": <string\>, "begin": <string\>, "duration": <int\> }, ... ] } , ... } } } | 200, 400, 500 | 업무 기간 : begin(시작 날짜) + duration(기간) <br> 날짜 양식: yyyy-MM-dd                     |
| 분배되지 않은 업무 불러오기 | GET         | /task/unassigned       | | [ { "id": <int\>, "title": <string\>, "team": <string\> }, ... ] | 200, 400, 500 | |
| 업무 추가하기              | POST        | /task                  | { "title": <string\>, "job": <string\>, "begin": <string\>, "end": <string\>, "importance": <int\> } | | 200, 400, 500 | 날짜(begin,end) 양식: yyyy-MM-dd |
| 업무 분배 케이스 생성하기  | POST        | /task/recommend        | [ <int\>, <int\>, ... ]                                                                             | [ { {teamId}: { "name": <string\>, "workers": { {workerId}: { "name": <string\>, "tasks": [ { "id": <int\>, "name": <string\> }, ... ] } , ... } } , ... } ] | 200, 400, 500 | - requset로 분배하기를 원하는 업무들의 ID를 보낸다. <br> - 각각의 케이스가 object로 표현되어 리스트에 담긴 채 response로 전달된다. <br> - 케이스 속에서, 각각의 워커는 자신이 분배받은 업무의 ID와 제목을 리스트로 담아서 받는다. |
| 업무 분배하기              | POST        | /task/assign           | { {workerId}: [ <int\>, <int\>, ... ], {workerId}: [ <int\>, <int\>, ... ], ... } | | 200, 400, 500 | - 선택한 케이스의 데이터를 가공하여, 각 워커가 담당한 업무의 ID를 리스트에 담아서 전달한다. |

<br>

---

## Creator

### Protaku - (Kug HuiGeun)

> **DB supporter (a bit)**  
> Kim Junyoung
