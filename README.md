### this app base on
    1. python 3.6
    2. anaconda package
    3. windows 

#### `app.py` is get evidence by command in excelFiles
#### `makeEvidence.py` is make evidenceFile from `./screenShot` folder 


## TODO list 

### DB control 
1. DB evidence 
1. DB diff
1. DB DML

### machine control 
1. set Time , Date

### report 
1. test result merge 
1. logging

### install for windows

## MEMO
```
파이썬 라이브러리는 알아서 할것.

엑셀에서 읽어 드린 테스트케이스중

1번째는 테스트케이스명
2번째는 해당테스트케이스 실행여부
3번째이후는 테스트 명령어
 <명령어 룰>
 디비 제어 관련  : 디비관련 CRUD
 화면 제어 : 셀레니움 드라이버 제어
 커널제어(OS)관련: 시간 날짜 . 혹은 폴더 관련 제어
 디비 덤프 or diff


파이썬에서 엑셀 제어는 win32com 라이브러리를 이용하는 것이 좋지 않을까 생각을 해본다.

<20161118>
디비 관련 처리에 대해서...
    1. 데이터 베이스의 변화를 체크하는 라이브러리가 있으면 좋을 것 같은데 이전에 자바로 구현할 때 썻던 라이브러리는 오픈 라이브러리는
       행이 추가 되거나 삭제되는 부분에 대해서는 제대로 된 처리가 이루어 지지 않았다. 아미도 PRIMARY KEY 에 대한 설정이 없었기 때문이라 생각이 되는데
       이번에 새로 파이선에서 데이터베이스의 변화치를 표현하기 위해서 보고 잇는 Django dbdiff라이브러리의 경우에는 키 설정이 가능한지 한번 확인이 필요할 것 같다.

    2.하나의 테스트 케이스에서 복수의 디비데이터를 취득하여 타임라인별로 출력을 하려고 할때 고려해야하는 것
      -하나의 이미지로 타임별 테이블로 표현이 가능한가? 여러 테이블을 하나의 HTML로 만들것
      -각 테이블에 대한 정보가 필요할듯
        -테이블의 타이틀 설정하는 기능 필요
            -예:초기 , 변경, 등록, 등등 ....
```
