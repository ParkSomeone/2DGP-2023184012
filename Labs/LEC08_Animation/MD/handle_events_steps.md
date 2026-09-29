# handle_events() 구현 단계

## 현재 역할

`handle_events()`는 매 반복마다 윈도우에서 발생한 입력과 종료 이벤트를 확인하는 함수다.
현재는 함수 호출 확인용 `print()`만 수행한다.

## 작동 단계

1. pico2d 이벤트 목록을 확인한다.
2. 윈도우 닫기 또는 종료 키 입력을 찾는다.
3. 종료 이벤트가 있으면 게임 루프 종료 상태를 설정한다.
4. 종료 이벤트가 없으면 함수 실행을 끝내고 `update()`로 진행한다.

## 단계별 구현

### 1단계: 이벤트 저장 공간 준비

- 현재 프레임에서 발생한 이벤트를 저장할 구조를 준비한다.

### 2단계: 이벤트 목록 가져오기

- pico2d의 이벤트 확인 기능으로 현재 이벤트 목록을 가져온다.

### 3단계: 이벤트 순회

- 가져온 이벤트를 하나씩 검사한다.

### 4단계: 종료 버튼 판별

- 윈도우 닫기 이벤트를 확인한다.

### 5단계: 종료 키 판별

- 필요한 종료 키 입력을 확인한다.

### 6단계: 종료 상태 변경

- 종료 이벤트가 발생하면 게임 종료 상태 변수를 변경한다.

### 7단계: 메인 루프 연결

- 종료 상태이면 `while True`를 끝내고, 그렇지 않으면 `update()`와 `render()`를 계속 실행한다.

## 단계별 구현 확인 코드

각 단계의 구현 직후 다음과 같은 임시 출력문을 넣어 실행 여부를 확인한다.

1. 이벤트 저장 공간 준비: `print('[handle_events] stage 1: event storage ready')`
2. 이벤트 목록 가져오기: `print('[handle_events] stage 2: events loaded')`
3. 이벤트 순회: `print('[handle_events] stage 3: events checked')`
4. 종료 버튼 판별: `print('[handle_events] stage 4: close event checked')`
5. 종료 키 판별: `print('[handle_events] stage 5: quit key checked')`
6. 종료 상태 변경: `print('[handle_events] stage 6: quit state updated')`
7. 메인 루프 연결: `print('[handle_events] stage 7: loop connection checked')`

7단계까지 정상 동작을 확인하고 나면 위의 모든 확인용 `print()`문을 삭제한다. 최종 코드에는 이벤트 처리 기능만 남겨야 한다.

## 완료 기준

- 창의 닫기 버튼으로 프로그램을 종료할 수 있다.
- 종료 이벤트가 없으면 다음 프레임 처리가 계속된다.
