Django Setting

가상환경 - 장고 파일을 만들려고 해당 폴더를 만들고 그 안에 들어가서 진행한 작업

```bash
# 파이썬 버전 확인
# 반드시 3.7.x 버전이 맞는지 확인 후 진행
$ python -V
Python 3.7.4

# 가상환경 생성
# python -m venv <가상환경 설치경로>
$ python -m venv venv

# 가상환경 적용
$ source venv/Scripts/activate

# 버전확인
(venv) # <= 가상환경 적용 시 git bash 에서 해당 환경 이름이 표시된다.
$ python -V
Python 3.7.4

# 설치된 모듈 확인
(venv)
$ pip list
Package    Version
---------- -------
pip        19.0.3
setuptools 40.8.0


# pip upgrade
(venv)
python -m pip install --upgrade pip

# pip upgrade 확인
(venv)
$ pip list
Package    Version
---------- -------
pip        19.2.2
setuptools 40.8.0
```



------------------------------------

VS code 및 기타세팅



VS Code Extensions 에서 `Python` 과 `Django` 설치

Ctrl + Shift + P => python select interpreter => 방금생성한 가상환경을 선택(.\venv\Scripts\python.exe)

- .vscode/settings.json 파일이 생성되며 터미널에서 자동으로 가상환경 적용된다면 OK

Git ignore.io에 접속해서 python, django, windows, vscode 선택후 생성 및 복사

- gitignore파일 생성후 붙여넣기



### VS Code Django 환경세팅

```json
{
    // 파이썬 환경 선택 => 자동으로 해줌
    "python.pythonPath": "venv\\Scripts\\python.exe",
    // Django에서 사용되는 파일 타입에 대한 정의
    "files.associations": {
        "**/templates/*.html": "django-html",
        "**/templates/*": "django-txt",
        "**/requirements{/**,*}.{txt,in}": "pip-requirements"
    },
    // django-html 에서도 html emmet 을 적용
    "emmet.includeLanguages": {"django-html": "html"},

    // django-html 에서 tab size를 2칸으로 고정
    "[django-html]": {
        "editor.tabSize": 2
    },
 }
```





### Start Django project

```bash
(venv)
pip install django
```

- Django를 설치한 순간부터 django-admin이라는 command를 사용할 수 있게 된다.
- 이 command를 통해 django project에 여러가지 명령을 할 수 있다.



Start project

```bash
(venv)
$ django-admin startproject django_intro .
```

- 현재 디렉토리에서 django_intro라는 이름으로 프로젝트를 시작하겠다.

- Django project naming

  - 캐릭터는 사용될 수 없다

  - python과 django에서 이미 사용되는 이름은 사용하지 않는다.

    (django라는 이름은 django 그 자체와 충돌이 발생하며, test라는 이름도 django내부 모듈이름)



### Runserver ###

```bash
$ python manage.py runserver
```

Ctrl + c 로 종료

기본적으로 `localhost:8000` 에서 실행이된다.

