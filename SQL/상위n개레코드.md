# 문제설명
ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. ANIMAL_INS 테이블 구조는 다음과 같으며,
ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

동물 보호소에 가장 먼저 들어온 동물의 이름을 조회하는 SQL 문을 작성해주세요.

## 풀이
- MySQL : LIMIT 이용해서 맨 위의 값을 가져온다. 
- LIMIT 2 : 위에서 두번째까지 값을 가져옴
- LIMIT 3,9 : 3번째에서 9번째 사이 값을 가져옴
```mysql
SELECT NAME 
FROM ANIMAL_INS 
ORDER BY DATETIME
LIMIT 1;
```
- Oracle : rownum을 이용해서 서브쿼리 조회
```mysql
SELECT NAME
FROM (SELECT * FROM ANIMAL_INS ORDER BY DATETIME)
WHERE rownum = 1;
```

## 정리
 Oracle 위주로 하다 보니 MySQL은 익숙하지 않았다. LIMIT라는 편한 기능을 이용하면 되는 문제다.
