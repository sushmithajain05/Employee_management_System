from django.urls import path
from employee_app import views
urlpatterns = [

    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('home/',views.HomePage,name='home'),
    path('add_emp/',views.emp_add,name='add_emp'),
    path('',views.HomePage,name='home'),
    path('table/',views.ListPage,name='table'),
    path('delete/<int:employee_id>/', views.DeletePage, name='delete'),
    path('update/<int:employee_id>/', views.UpdatePage, name='update'),
    path('logout/', views.LogoutPage, name='logout'),
    path('attendance_list/', views.upload_attendance, name='attendance_list'),
    path('upload_attendance/', views.upload_attendance, name='upload_attendance'),
    path('employee_attendance/<int:employee_id>/', views.employee_attendance, name='employee_attendance'),
 
    
]