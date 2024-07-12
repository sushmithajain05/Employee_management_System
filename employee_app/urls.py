from django.urls import path
from employee_app import views
urlpatterns = [

    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('add_emp/',views.emp_add,name='add_emp'),
    path('',views.HomePage,name='home'),
    path('table/',views.ListPage,name='table'),
    path('delete/<int:employee_id>',views.DeletePage,name='delete'),
    path('update/<int:employee_id>',views.UpdatePage,name='update'),
]