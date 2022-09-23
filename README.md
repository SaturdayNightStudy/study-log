# study-log
🌔 매주 토요일 밤 진행하는 스터디 발표 자료 저장소  
매주 토요일 저녁 9시에 일주일동안의 공부 내용을 발표합니다.

## 커밋 규칙
1. `study-log` 저장소를 자신의 레포지토리에 **fork** 합니다.
2. fork한 저장소를 별도로 clone 합니다.
   * 반드시 fork한 저장소를 clone 해주세요.
3. `clone`한 디렉토리에서 자신의 폴더 안에 자유롭게 발표 자료를 커밋 후 `Pull Request` 해주시면 감사하겠습니다.😁
   
## Pull Request 방법
1. 먼저 `clone` 저장소로 이동하여 본인의 이름으로 `branch`를 생성합니다.
   ```bash
    $git checkout -b branchname ##자신의 이름
    Switched to a new branch 'branchname'
   ```
2. 커밋 할 자료를 업로드합니다.
    ```bash
    $git add ./directory ##stage에 추가 할 디렉토리 또는 파일
    $git commit -m "[commit-type] 커밋 메시지"
    $git push --set-upstream origin <branchname>
    ```
3. 자료 검토 후, 깃허브 저장소 `Pull Request` 탭에서 `New Pull Request` 버튼을 클릭해주시면 제가 확인 후 메인 저장소에 merge 시키도록 하겠습니다.


## 학습 기록✅