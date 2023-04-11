# To Do LIST 🗓️

## (1) Introduction

- 미니 프로젝트 : 간편하게 할 일을 생성 및 관리 할 수 있는 웹페이지 Django를 사용하여 제작


- 프로젝트 규모 : 개인 프로젝트

- Skills
    - `Design_Guide` : Figma
    - `Languages` : Python, JavaScript, HTML, CSS
    - `FrameWork` : Django, Bootstrap

<br>
<br>

---

## (2) Basic Features

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

<br>
<br>

---

## (3) Design

### 1. index 페이지

- 남은 할 일 수 / 전체 할 일 수 표시
- 모든 할 일 목록을 조회
    - 정렬 및 카테고리별 조회
- 생성 버튼
- 각 할 일 별로 제목, 생성일, 카테고리, 마감일을 표시
- 각 할 일을 수정, 삭제, 완료를 할 수 있는 버튼 배치
- 완료 시, 완료된 일을 하단의 Done에 배치하여 목록을 따로 조회
- 상단으로 갈 수 있는 top 버튼 fixed로 배치

![](readme_asset/index_%ED%95%A0%EC%9D%BC%EC%A1%B0%ED%9A%8C.jpg)

< index페이지_디자인가이드_(제작도구:Figma) >

<br>
<br>

---

## (4) 구현 과정의 문제점 및 해결

### 1. 카테고리별 조회

- 문제점

    : 할 일의 목록에서 카테고리 별로 조회하는 기능을 구현하는데 있어 `html`의 `select form`에서 받은 데이터를 `views.py`로 어떻게 보내고 처리해야 하는지에 대한 방법이 어려웠다.

<br>

- 해결방법
    - Query Parameter로 값을 보내는 방법

    <br>

    1. category url을 작성한다.

    <br>

    ```python
    <!-- url 작성 -->

    from django.urls import path
    from . import views

    app_name = 'todos'
    urlpatterns = [
        path('category/', views.category, name='category'),
    ]
    ```

    <br>

    2. todos/index.html 에서 `form 태그`로 select form을 감싸고, action으로 category url을 실행하도록 한다. 또한 method는 `GET`으로 데이터를 받는다.

    3. select form에서 views.py로 보낼 데이터의 `name`을 `category_mode`로 지정한다.

    4. select form에서 `onChange` 속성을 `'form.submit()'`으로 하여 select가 변할 경우, 데이터의 submit이 동작하도록 하였다.

    <br>

    ```html
    <!-- index.html의 카테고리별 select form 작성 -->

    <form action="{% url 'todos:category' %}" method='GET'>
            <select class="form-select select-box" name='category_mode' onChange="form.submit()">
                <option selected>카테고리별</option>
                <option value="집안일">집안일</option>
                <option value="문화생활">문화생활</option>
                <option value="업무">업무</option>
                <option value="자기계발">자기계발</option>
            </select>
        </form>
    ```

    <br>

    5. views.py에서 받은 `request 데이터(request.GET)`의 `키(name)`를 변수 category_mode에 담는다.

    6. `if 조건문`을 사용하여 키값이 '집안일'일 경우, 변수 todos에 queryset API 중 `filter()`를 사용해 Todo Model의 category필드가 '집안일'인 쿼리들을 추출하도록 한다.

    <br>

    ```python
    <!-- views.py의 category 함수 작성 -->

    def category(request):
        category_mode = request.GET.get('category_mode')
        if category_mode == '집안일':
            todos = Todo.objects.filter(category='집안일')
        elif category_mode == '문화생활':
            todos = Todo.objects.filter(category='문화생활')
        elif category_mode == '업무':
            todos = Todo.objects.filter(category='업무')
        elif category_mode == '자기계발':
            todos = Todo.objects.filter(category='자기계발')    
        context = {
            'todos': todos,
        }
        return render(request, 'todos/index.html', context)
    ```
<br>

![](readme_asset/%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EB%B3%84%20%EC%A1%B0%ED%9A%8C%20%ED%95%B4%EA%B2%B0.JPG)

< 카테고리별로 조회 화면 >

<br>
<br>
<br>

### 2. 할 일 생성, 단일 조회, 수정 시, modal을 통해서 수행하기

- 문제점

    : 쉬운 방법은 각각의 기능에 따른 html 파일을 생성하고, 각각의 페이지에서 기능을 수행하는 것이다. 하지만 modal을 통해 기능을 구현해보고 싶었다. 따라서 `처음`에는 bootstrap의 modal을 사용하고, `modal`의 body에 `Django Template Language(DTL)`을 넣어 데이터를 가져오려고 했는데 출력이 되지 않았다.

    <br>

    이러한 현상의 원인으로는 `modal창`의 경우, `동적`으로 열리고 닫히는 반면, `DTL 코드`의 경우, `서버 측에서 렌더링`이 되기 때문에 이러한 동적인 부분에 대응이 잘 안 될 수 있다. 즉, modal창이 렌더링되기 전, DTL 코드가 실행되어 데이터가 조회되지 않을 수 있다.

    <br>

    또는 `modal창`이 다른 `DOM 요소와의 분리`되어 있어 DTL 코드가 해당 요소에 액세스 하지 못할 수 있다.

<br>

- 해결방법

    - jquery를 사용하여, modal을 실행할 경우, data-remote로 원하는 url을 modal 창에 로드하는 방법

    <br>

    1. jquery CDN을 가져온다.

    <br>

    ```html
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    ```

    2. modal이 실행되는 버튼을 만든다.
        - `data-remote`에 실행할 `url`을 넣어주어야 한다.
        - `data-bs-target`에 `id`를 지정한다.

    <br>

    ```html
    <!-- 할 일 제목 클릭 시, detail로 연결되는 modal -->

    <a data-remote="{% url 'todos:detail' todo.pk %}" data-bs-toggle="modal" data-bs-target="#detail">
        {{ todo.title }}
    </a>
    ```

    3. 외부에 modal 창을 생성한다.
        - modal의 id를 위의 2번에서 작성한 id와 맞춰준다.

    <br>

    ```html
    <!-- detail_modal -->

    <div class="modal fade" id="detail" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
            </div>
        </div>
    </div>
    ```

    4. modal이 실행될 경우, data-remote의 url을 가져올 수 있도록 JavaScript 코드를 추가한다.
        - `id`를 `modal의 id`와 맞춰서 어떤 modal에서 script를 적용할지 선택한다.
        - `show.bs.modal` : modal이 열릴 때 바로 이벤트가 실행된다.
        - `var $modal = $(this)`: 현재 이벤트가 발생한 modal창을 jQuery 객체로 가져온다.
        - `var remoteUrl = e.relatedTarget.dataset.remote;` : modal trigger 버튼요소의 data-remote 속성을 가져온다.
        - `if (remoteUrl) {$modal.find(".modal-content").load(remoteUrl);}` : remoteUrl이 존재하면, modal내부의 modal-content 요소를 선택하고, 해당부분에 url을 통해 가져온 데이터를 로드하여 표시하게된다. 
    
    <br>

    ```html
    <!-- script 코드 -->

    <script>
    $(document).ready(function() {
        $("#detail").on("show.bs.modal", function(e) {
        var $modal = $(this);
        var remoteUrl = e.relatedTarget.dataset.remote;
        if (remoteUrl) {
            $modal.find(".modal-content").load(remoteUrl);
            }
        });
    });
    </script>
    ```

    - 이 방법의 경우도, modal에 로드하여 표시할 `외부 템플릿을 각각 작성`하여야 한다. 하지만 이를 통해 웹페이지가 아닌 modal을 통해 데이터를 조회 할 수 있게 되었다.

<br>

![](readme_asset/%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0_modal%20%ED%95%B4%EA%B2%B0.JPG)

< 단일 할 일 modal 화면 >

<br>

![](readme_asset/%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0_modal%20%ED%95%B4%EA%B2%B0.JPG)

< 생성하기 modal 화면 >

<br>

![](readme_asset/%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0_modal%20%ED%95%B4%EA%B2%B0.JPG)

< 수정하기 modal 화면 >