# To Do LIST 🗓️

## 1) Introduction

- 미니 프로젝트 : 간편하게 할 일을 생성 및 관리 할 수 있는 웹페이지 Django를 사용하여 제작


- 프로젝트 규모 : 개인 프로젝트

- Skills
    - `Design_Guide` : Figma
    - `Languages` : Python, JavaScript, HTML, CSS
    - `FrameWork` : Django, Bootstrap

## 2) Basic Features

1. 할 일 생성
    - `필요한 정보`<br>
    : 제목(title), 내용(content), 카테고리(category), 생성일자(created_at), 마감일자(deadline)
    - `modal`을 통해 생성페이지 보여주기
2. 할 일 수정
    - 기존 정보 조회
    - `modal`을 통해 수정페이지 보여주기
3. 할 일 삭제
    - `modal`을 통해 삭제할 것인지, 한번 더 확인하기
4. 할 일 정렬하여 조회
    - `정렬 목록`<br>
    : 생성일순, 마감일순, 카테고리순
5. 카테고리 별 조회
    - `select` 사용
6. 완료 버튼
    - 버튼을 통해 `완료/미완료 스위칭`하기

## 3) Design

### 1. index 페이지

- 남은 할 일 수 / 전체 할 일 수 표시
- 모든 할 일 목록을 조회
    - 정렬 및 카테고리별 조회
- 생성 버튼
- 각 할 일 별로 제목, 생성일, 카테고리, 마감일을 표시
- 각 할 일을 수정, 삭제, 완료를 할 수 있는 버튼 배치
- 완료 시, 완료된 일을 하단의 Done에 배치하여 목록을 따로 조회
- 상단으로 갈 수 있는 top 버튼 fixed로 배치

![](readme_asset/To%20Do%20LIST.jpg)

< index페이지_디자인가이드_(제작도구:Figma) >