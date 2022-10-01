## Jenkins를 활용해 자동 배포 해보기

### Jenkins

-   **CI (Continuous Integration)**
    -   코드 형상 관리에 있어 개발을 하면서도 **지속적으로** 관리 및 품질을 유지하는 것
-   대표적인 CI Tool으로써 `Git Repository`와 연동하여 손쉽게 관리 할 수 있다.

## Jenkins Tutorial

### Jenkins Install

```bash
    sudo apt-get install openjdk-11-jdk #jdk 설치 (ver 8 이상)

    wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add - #Jenkins 저장소 Key 다운로드

    echo deb http://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list #Jenkins 레포지토리 등록

    sudo apt-get install jenkins #Jenkins Install

    ##기본 8080 포트에서 다른 포트로 변경하기
    sudo vi /etc/default/jenkins
```

### WebHook 등록하기

Jenkins에서 관리 할 레포지토리에 `webhook`을 추가해준다.  
보통 Jenkins를 사설 서버에 설치하기 때문에 설치한 `서버 접속 주소 + /github-webhook`을 입력해주면 된다.

![webhook](https://user-images.githubusercontent.com/46988995/193408173-a0285d82-2bac-4bc5-b76c-dde464e44d2c.png)

### Jenkins Item 생성하기

1. 새로운 Item 메뉴 > 빌드 관리 이름 입력
   ![item-1](https://user-images.githubusercontent.com/46988995/193408261-e3ecfdb0-79eb-4a6b-a882-ed904e86882c.png)
2. 환경설정 셋팅
    - **소스관리** - Git > Repository URL > 배포하려는 Git URL 입력 - **(주의사항)** Repository는 바로 접근가능하도록 1depth 디렉토리로 관리해야한다.
      ![repository](https://user-images.githubusercontent.com/46988995/193408377-54d7756b-e375-4d07-9101-719145f08e21.png)
3. 참조 할 `branch` 입력 (\*/main)
4. 빌드 유발
    - **Git hook trigger for GISScm polling**
5. Build Steps 쉘 스크립트 설정

    ```bash
    sudo rm -rf /var/www/html/dist
    cd /var/lib/jenkins/workspace/Vue
    sudo npm install
    sudo npm run build
    ```

## nginx 서버와 연동하기

### nginx 설치

```bash
$ sudo apt-get install nginx
```

### sites-abvailable 설정

```bash
server {
	listen 8088 default_server;
	listen [::]:8088 default_server;

	root /var/www/html/dist;
	index index.html index.htm;
	server_name _;

	location / {
		try_files $uri $uri/ /index.html;
	}

}

```

### 심볼링크 연결하기

```bash
sudo ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-enabled/default.conf
```

### nginx restart

```bash
$ sudo systemctl restart nginx
```
