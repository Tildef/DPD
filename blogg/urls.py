from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostLista.as_view(), name='blogg-hem'),
    path('post/<int:pk>/', views.PostSida.as_view(), name='post-sida'),
    path('anv/<str:username>/', views.AnvamdarePostLista.as_view(), name='post-anvandare'),
    path('post/<int:pk>/uppdatera/', views.UppdateraPost.as_view(), name='post-uppdatera'),
    path('post/<int:pk>/radera/', views.raderaPost.as_view(), name='post-radera'),
    path('post/ny/', views.SkapaPost.as_view(), name='post-ny'),
    path('om/', views.om, name='blogg-om'),

]