from django.urls import path
from. import views

app_name = 'reading'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    #path('books/',views.ListsView.as_view(),name='list'),
    #path('wisesaying/<int:pk>/',views.WisesayingView.as_view(),name='detail'),
    #reading/wisesaying/1(int형)/ 의 모든 url 취급
]
