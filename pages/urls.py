from django.urls import path
from . import views

# www.ssafy.com/login => 아래에 정의되어있지 않기때문에 404 not found 에러뜸
# www.ssafy.com/login => views.index
urlpatterns = [
    # path('사용자가 접속하는 경로')
    path('workshop_result/', views.workshop_result),
    path('workshop_input/', views.workshop_input),
    path('static_example/', views.static_example),
    path('lotto_pick/', views.lotto_pick),
    path('lotto_result/', views.lotto_result),
    path('result/', views.result),
    path('search/', views.search),
    path('lotto/', views.lotto),
    path('isitBirthday/', views.isitBirthday),
    path('info/', views.info),
    path('student/<str:name>', views.student),
    path('template_language/', views.template_language),
    path('times/<int:num1>/<int:num2>', views.times),
    path('greeting/<str:name>/', views.greeting),
    path('image/', views.image),
    path('dinner/<str:name>/', views.dinner),
    path('index/', views.index),
    path('introduce/', views.introduce),
]
