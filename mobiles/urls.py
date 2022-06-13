from django.urls import path
from mobiles import views

urlpatterns=[
    path('add',views.AddMobileView.as_view(),name='add-mob'),
    path('home', views.HomeView.as_view(),name='home'),
    # path('login', views.LoginView.as_view(),name='emp-login'),
    # path('profile/add',views.EmpCreateView.as_view(),name='emp-add')
]