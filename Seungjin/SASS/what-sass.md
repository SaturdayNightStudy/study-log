## SASS의 필요성

1. 규모가 크고 복잡한 웹 어플리케이션에서의 효율적인 구조화
2. 프로그래밍 언어 처럼 변수, 조건문, 반복문 활용을 통해 중복되지 않은 공통 컴포넌트 작성
3. 중첩 코드블록(Nesting) 사용으로 계층적인 스타일링 편이

### SASS 간편 설치하기

1. 패키지 모듈 설치
    ```bash
    npm i node-sass  #node-sass
    ```
2. 스크립트 커맨드 추가

    ```json
        "scripts": {
                "test": "echo \"Error: no test specified\" && exit 1",
                "node-sass": "node-sass",
                "sass": "node-sass ./styles/main.scss ./main.css"

        }
    ```

    ```bash
        npm run sass ##sass -> css compile
    ```

3. linter 설정
    ```bash
    npm i -D sass-lint
    ```

## 기본 문법

### 디버깅

`@debug` 명령어를 통해 디버깅을 할 수 있다.

### 자료형

scss에서는 9개의 자료형을 사용할 수 있으며 `type-of`로 타입 체크도 쉽게 할 수 있다.

```scss
$font-weights: (
    'regular': 400,
    'medium': 500,
    'bold': 700
);

@function foo($x) {
    @return $x;
}

@mixin syntax-colors($args...) {
    @debug type-of($args); //arglist
}

@debug type-of(10px); // number
@debug type-of('#8c8c8c'); // string
@debug type-of(#8c8c8c); // color
@debug type-of(true); // bool
@debug type-of(null); // null
@debug type-of(10px 20px 30px); // list
@debug type-of($font-weights); // map
@debug type-of(get-function(foo)); // function

@include syntax-colors($string: #080, $comment: #800);
```

사용할 수 있는 타입 목록

-   number
-   string
-   color
-   bool
-   null
-   list
-   map
-   function
-   arglist

### 변수

css에서 사용하는 여러 속성 값들을 변수로 지정할 수 있다. `$` 예약어를 사용한다.

-   영문자, 대시(-), 언더바(\_), 숫자를 사용할 수 있다.
-   숫자로 변수명을 시작할 수 없다.
-   대소문자를 구분한다.

```sass
$width: 1;
$image-url : url('./assets/images/logo.svg);

p {
    width: $width;
}

div {
		background-image: $image-url;
}
```

### 조건문

`@if, @if~@else`로 조건문을 작성한다. 조건문 내부에서 OR 연산자 또는 AND 연산자를 사용할 수 있다.

```scss
$color: #ededed;
$position: fixed;

//기본 @if 지시문
p {
    @if (type-of($color) == color) {
        color: $color;
    }
}

//if ~ else
.section {
    @if ($position == fixed or $position == absolute) {
        position: $position;
    } @else {
        position: relative;
    }
}

//if ~ else if ~ else
@if (condition1) {
    //..style
} @else if(condition2) {
    //..style
} @else {
    //..style
}
```

### 반복문

`@for` 를 사용해 반복문을 작성한다. 선언할 때 내장 변수를 같이 선언하는데, 반복문 내에서 사용할 변수이다.

```scss
@for $item for 1 through 4 {
    //loop code
}
```

반복문 내에서 변수를 쓰려면 `#{$variable}`형태로 사용하면된다.

```scss
$sm-cols: 4; //grid 컬럼 갯수
@for $item from 1 through 4 {
    .col-sm-#{$item} {
        width: $item / $sm-cols * 100%;
    }
}
```

```css
/* 컴파일 결과 */
.container .col-sm-1 {
    width: 25%;
}
.container .col-sm-2 {
    width: 50%;
}
.container .col-sm-3 {
    width: 75%;
}
.container .col-sm-4 {
    width: 100%;
}
```

### Map

sass에서 제공하는 `map`은 자바스크립트에서의 객체 자료형 처럼 key-value로 이루어진 자료형이다.

```scss
//font-style Map 정의
$font-style: (
    sm: 12px,
    md: 16px,
    lg: 18px
);
```

### map-get

해당 key에 맞는 value를 가져온다.

```scss
p {
    font-size: map-get($font-style, sm); //12px;
}
```

### map-has-key

정의된 map 내부에 해당 key가 존재하는지 확인한다.

```scss
@function get-font-size($size) {
    @if (map-has-key($font-style, $size)) {
        @return map-get($font-style, $size);
    } @else {
        @return 10px;
    }
}

p {
    font-size: get-font-size(xl); //10px
}

.lg-font {
    font-size: get-font-size(lg); //18px
}
```

### Mixin

css내에서 반복적으로 사용하는 코드들을 재사용할 수 있도록 도와주는 기능이다. `@mixin` 키워드 뒤에 mixin 이름을 지정해준다. 사용하려는 부분에 @include 키워드로 해당 mixin을 호출할 수 있다. (자바스크립트의 함수 사용 방법과 상당히 유사하다.)

```scss
//mixin 정의
@mixin mixin-name() {
    color: red;
}

//mixin 호출
p {
    @include mxin-name();
}
```

```css
p {
    color: red;
}
```

파라미터도 전달해서 사용할 수 있다. (미사용 시 생략 가능)

```scss
@mixin font-style($color) {
    font-size: 12px;
    line-height: 12px;
    letter-spacing: 0.05em;
    color: $color;
}

p {
    @include font-style(#ededed);
}
```

### Placeholder

`mixin`과 마찬가지로 공통 컴포넌트 역할에 사용한다. (그러나 함수나 mixin처럼 인자를 받을 수 없음)  
단순히 컴포넌트 간 동일 스타일 요소들을 상속 받는 요소로 사용한다.

```scss
//공통 컴포넌트
%button-base {
    height: 20px;
    padding: 0 6px;
    font-weight: 700;
    border-radius: 4px;
}

//상속
.button-red {
    @extend %button-base;
    backdround-color: red;
}

.button-yellow {
    @extend %button-base;
    backdround-color: yellow;
}

.button-green {
    @extend %button-base;
    backdround-color: green;
}
```
