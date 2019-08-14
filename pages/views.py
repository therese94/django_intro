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