from django.urls import path
from . import views


urlpatterns =[path('', views.PostView.as_view()),
              path('<int:pk>/', views.PostDetail.as_view()),
              path('review/<int:pk>/', views.AddComments.as_view(), name='add_comments'),
              path('review/<int:pk>/add_likes/', views.AddLikes.as_view(), name='add_likes'),
              path('review/<int:pk>/del_likes/', views.DelLike.as_view(), name='del_likes')]
