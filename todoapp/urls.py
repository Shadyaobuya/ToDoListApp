from django.urls import path
from . import views
urlpatterns=[
    
    path('login/',views.login_page,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout_page,name='logout'),
    path('mytasks/',views.my_tasks,name="index"),
    path('addtask/', views.addTask,name="addtask"),
    path('', views.homepage,name='home')
]