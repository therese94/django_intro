from django.shortcuts import render
from datetime import datetime
import random

# Create your views here.


def index(request):         # 첫번째 인자는 반드시 request => 사용자가 보내는 요청에 대한 정보
    return render(request, 'index.html')    # render의 첫번째 인자도 반드시 requeset가 들어간다

def introduce(request):
    return render(request, 'introduce.html')

def dinner(request, name):
    menu = ['강남 더막창스', '노랑통닭', '양자강']
    pick = random.choice(menu)
    context = {
        'pick':pick,
        'name':name,
    }

    # Django template으로 context전달
    return render(request, 'dinner.html', context)

def image(request):
    context = {
        'image' : 'https://picsum.photos/id/1002/200/300'
    }
    
    return render(request, 'image.html', context)

def greeting(request, name):
    context = {
        'name' : name
    }
    return render(request, 'greeting.html', context)

def times(request, num1, num2):
    result = num1 * num2
    context = {
        'num1' : num1,
        'num2' : num2,
        'result' : result
    }
    return render(request, 'times.html', context)


def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피', ]
    my_sentence = 'Life is shor, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'empty_list': empty_list,
        'datetimenow': datetimenow, 
    }

    return render(request, 'template_language.html', context)


def info(request):
    
    return render(request, 'info.html')


def student(request, name):
    student = {'홍길동': 28, '김길동': 28, '박길동': 28}
    age = student[name]
    context = {
        'name': name,
        'age' : age, 
    }

    return render(request, 'student.html', context)

def isitBirthday(request):
    n = datetime.now()
    my_m = 10
    my_d = 13
    context= {
        'm' : n.month,
        'd' : n.day,
        'my_m' : my_m,
        'my_d' : my_d,

    }
    return render(request, 'isitBirthday.html', context)

def lotto(request):
    real_lotto = [21, 25, 30, 32, 40, 42]
    lottos = []
    for i in range(6):
        lottos.append(random.randint(1,101))
    context = {
        'real_lotto' : real_lotto,
        'lottos' : lottos,
    }
    return render(request, 'lotto.html', context)


def search(request):
    return render(request, 'search.html')
    
def result(request):
    query = request.GET.get('query')
    category = request.GET.get('category')
    context = {
        'query': query,
        'category': category,
    }
    return render(request, 'result.html', context)

def lotto_pick(request):
    
    
    return render(request, 'lotto_pick.html')

def lotto_result(request):
    lotto_input = sorted(list(map(int,request.GET.get('lotto_input').split())))
    
    lotto_ans = [21, 25, 30, 32, 40, 42]
    context = {
        'lotto_input' : lotto_input,
        'lotto_ans' : lotto_ans,
    }
    return render(request, 'lotto_result.html', context)


def static_example(request):
    return render(request, 'static_example.html')