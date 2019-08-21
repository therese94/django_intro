from django.urls import path
from . import views

# www.ssafy.com/login => 아래에 정의되어있지 않기때문에 404 not found 에러뜸
# www.ssafy.com/login => views.index
urlpatterns = [
    # path('사용자가 접속하는 경로')
    path('index/', views.index),
]
