from django.shortcuts import render
import random
# Create your views here.


def index(request):         # 첫번째 인자는 반드시 request => 사용자가 보내는 요청에 대한 정보
    return render(request, 'index.html')    # render의 첫번째 인자도 반드시 requeset가 들어간다

def introduce(request):
    return render(request, 'introduce.html')

def dinner(request):
    menu = ['강남 더막창스', '노랑통닭', '양자강']
    random.choice(menu)
    context = {
        'pick':pick,
    }

    # Django template으로 context전달
    return render(request, 'dinner.html')