## 원티드 프리온보딩 사전과제

### 과제 목표

-   `React JS`로 Todo List App구현할 것
-   기능에 영향을 주는 라이브러리는 사용하지 말 것 (Router, HTTP Client 제외)
-   JWT는 발급 받아 LocalStorage에 보관하고, 토큰이 없는 사용자 예외처리

### 개인적인 목표 ✔️

-   사용자 경험에 최대한 충실하자.
-   모듈화에 신경쓰자.
-   기능을 최대한 분리하자.
-   Sass를 도입하자.
-   예외 케이스를 신경쓰자.
-   최대한 일관성을 유지하자.

### 세부 구현 내용

**반응형과 타이포그라피 구성**

```scss
//📂 typography.scss

$font-size-sm: 12px;
$line-height-sm: 16px;
$letter-spacing-sm: -0.005em;

$font-size-md: 16px;
$line-height-md: 24px;
$letter-spacing-md: -0.01em;

$font-size-lg: 32px;
$line-height-lg: 48px;
$letter-spacing-lg: -0.01em;
```

```scss
//📂 responsive.scss
$md-breakpoint: 768px;
$lg-breakpoint: 1200px;

@mixin responsive($screen) {
    @if ($screen == 'Tablet') {
        @media screen and (min-width: $md-breakpoint) {
            @content;
        }
    }

    @if ($screen == 'Desktop') {
        @media screen and (min-width: $lg-breakpoint) {
            @content;
        }
    }
}
```

**모듈화**
구조적으로 분리, 영향도 최소화

```plain text
📁
.
├── README.md
├── package-lock.json
├── package.json
├── public
│   ├── _redirects
│   ├── favicon.ico
│   ├── index.html
│   ├── logo192.png
│   ├── logo512.png
│   ├── manifest.json
│   └── robots.txt
└── src
    ├── App.css
    ├── App.js
    ├── App.test.js
    ├── api ## HTTP Fetch Api
    │   ├── auth.js
    │   └── todo.js
    ├── assets
    │   └── fonts ##SVG 아이콘 파일
    │       ├── todo.eot
    │       ├── todo.svg
    │       ├── todo.ttf
    │       └── todo.woff
    ├── components ## 분리 컴포넌트
    │   ├── RouteAuth.jsx
    │   └── TodoItem.jsx
    ├── index.js
    ├── logo.svg
    ├── pages ## 페이지 컴포넌트
    │   ├── Home.jsx
    │   ├── Sign.jsx
    │   └── TodoList.jsx
    ├── styles #Sass 파일
    │   ├── bases # 초기화, 공통 Style
    │   │   ├── _fonts.scss
    │   │   ├── _normalize.scss
    │   │   ├── _ui.scss
    │   │   └── _utils.scss
    │   ├── constants # sass 상수
    │   │   ├── _colors.scss
    │   │   └── _typography.scss
    │   ├── layouts # 화면 레이아웃
    │   │   ├── _buttons.scss
    │   │   ├── _content.scss
    │   │   ├── _form.scss
    │   │   ├── _header.scss
    │   │   └── _todo.scss
    │   ├── main.scss # import
    │   └── mixins # mixin
    │       ├── _fontstyles.scss
    │       └── _responsive.scss
    └── utils # 공통 함수&상수
        ├── constants.js
        └── util.js
```

**기능 분리**
재사용 할 수 있는 것은 재사용 (회원가입, 로그인)

```js
//📂 Sign.js
import { Link, useLocation, useNavigate } from 'react-router-dom';

const Sign = function () {
    const data = {
        signin: {
            text: '로그인',
            replaceText: '계정이 없으신가요?',
            replaceLink: '/signup',
            call: fetchSignIn
        },
        signup: {
            text: '회원가입',
            replaceText: '이미 계정이 있으신가요?',
            replaceLink: '/signin',
            call: fetchSignUp
        }
    };
};
.
.
.

//Path 호출
const path = useLocation().pathname.substring(1);
const elementText = data[path].text;

.
.
.
function submit() {
    return data[path].call();
}

```

HTTP 통신은 따로 분리

```jsx
//📂 auth.js
/**
 * 회원가입 API
 * @param {object} request : 요청 객체
 */
async function requestSignUp(request) {
    const response = await fetch(`${constants.REQUEST_URL}/auth/signup`, {
        method: 'POST',
        headers: { 'Content-Type': ' application/json' },
        body: JSON.stringify(request)
    });
    return checkHttpResponse(response);
}
```

```jsx
//📂 Sign.js

const Sign = function () {

    function submit() {
        return data[path].call();
    }
    //로그인
    function fetchSignIn() {
        requestSignIn({ email: accountInfo.email, password: accountInfo.password }).then((res) => {
            if (res.result) {
                localStorage.setItem('token', res.data.access_token);
                navigate('/todo');
            } else {
                alert(res.message);
            }
        });
    }

    return (
        <main>
            <div className="form">
                <h1 className="text-lg title">{elementText}</h1>
                .
                .
                .
                <button
                    type="button"
                    className="button-normal submit xl"
                    disabled={!(isAvailableEmail && isAvailablePassword)}
                    onClick={submit}
                >
                    {elementText}
                </button>
            </div>
        </main>
    );
};
```

검증용 라우터를 따로 처리하자.
```jsx

//before : 각 화면에서 state 값이 바뀔 때마다 권한 체크해서 redirect
    useEffect(function () {
        if (!checkAuthState()) {
            navigate('/');
        }
    });
```

```jsx
//after : 미들웨어 역할을 수행하는 라우터 생성 (RouteAuth) 
function App() {
    return (
        <div className="app">
            <header>
                <h1 className="text-lg">✅ Todo List</h1>
            </header>
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<RouteAuth component={<Home />} destination={'home'} />} />
                    <Route path="/todo" element={<RouteAuth component={<TodoList />} destination={'todo'} />} />
                    <Route path="/signin" element={<Sign />} />
                    <Route path="/signup" element={<Sign />} />
                </Routes>
            </BrowserRouter>
        </div>
    );
}

```

```jsx
//📂 RouteAuth.scss
import { Navigate } from 'react-router-dom';

const RouteAuth = function ({ component, destination }) {
    const auth = localStorage.getItem('token');
    if (destination === 'home') {
          return (auth ? <Navigate to={'/todo'} /> : component) 
    } else {
        return (auth ? component : <Navigate to={'/'}/>)
    }
};

export default RouteAuth;


```

**예외 케이스 관리**
클라이언트는 항상 서버를 믿어서는 안된다는 신념...!!
![request](https://user-images.githubusercontent.com/46988995/195632272-f0fd4173-2d3d-44af-9931-dadef603ffa3.png)

```jsx
/**
 * 응답 확인 Middleware
 * @param {object} response : 응답 객체
 */
function checkHttpResponse(response) {
    let message = 'success';
    if (response.ok) {
        return response.text().then(function (res) {
            res = res ? JSON.parse(res) : {};
            return {
                result: true,
                data: res || null,
                message
            };
        });
    } else {
        const statusCode = response.status;
        return response.json().then(function (res) {
            if (res.message) {
                message = res.message;
            } else {
                if (statusCode === 400) {
                    message = '올바르지 않은 요청입니다.';
                } else if (statusCode === 401) {
                    message = '권한이 없는 사용자 입니다.';
                } else if (statusCode === 404) {
                    message = '요청 주소가 존재하지 않습니다.';
                } else {
                    message = '알 수 없는 오류입니다.';
                }
            }
            return {
                result: false,
                message
            };
        });
    }
}

export { checkHttpResponse };

```

## 구현 결과
 + [**🚀 Netlify**](https://sjchoi-wanted-todolist.netlify.app/todo)
+ [**🔗 Github**](https://github.com/yondo123/wanted-pre-onboarding-fe-7)