from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import Employee
# @login_required(login_url='login')
# Create your views here.
def HomePage(request):
    return render(request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        if password1!=password2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user=User.objects.create_user(username=username,password1=password1)
            my_user.save()
            return redirect('login')
    
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('signup')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def emp_add(request):
    if request.method=='POST':
        employees_id=request.POST.get("employee_id")
        employees_name=request.POST.get("employee_name")
        email=request.POST.get("employee_email")
        print(email)
        phone_number=request.POST.get("phone_number")
        job_title=request.POST.get("job_title")

        e=Employee()
        e.employee_id=employees_id
        e.employee_name=employees_name
        e.email=email
        e.phone_number=phone_number
        e.job_title=job_title
        e.save()
        return redirect("/home/")
    return render(request,"add_emp.html",{})

def ListPage(request):
    emp=Employee.objects.all()
    return render(request,"table.html",{'emp':emp})

def DeletePage(request,employee_id):
    e=Employee.objects.get(pk=employee_id)
    e.delete()
    return redirect("/home")

def UpdatePage(request,employee_id):
    e=Employee.objects.get(pk=employee_id)
    return render(request,"update.html",{'emp':emp})

