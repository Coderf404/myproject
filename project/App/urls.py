from . import views
from django.urls import path

urlpatterns = [
  path('', views.PostList.as_view(), name="home"),
  path('blogs/<slug:slug>/', views.DetailView.as_view(), name="post_detail"),
  path("register", views.register_request, name="register"),
  path("login", views.login_request, name="login"),
  path('blogs/new', views.AddPostView.as_view(), name='blogs_new'),
  path('logout', views.logout_request, name='logout'),
]